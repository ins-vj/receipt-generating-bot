from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from .models import UserSession, OrderItem, OrderArchive
from django.conf import settings
import os
from twilio.rest import Client
from .utils import generate_order_pdf_pdfkit


def calculate_total_cost(order_items):
    """Calculates the total cost of a list of order items."""
    return sum(item.quantity * item.price for item in order_items)


from .models import UserSession, OrderItem, OrderArchive

@csrf_exempt
def whatsapp_reply(request):
    if request.method == 'POST':
        from_number = request.POST.get('From')
        incoming_msg = request.POST.get('Body', '').strip()
        
        response = MessagingResponse()
        msg = response.message()

        # Retrieve or create the user session
        session, created = UserSession.objects.get_or_create(
            from_number=from_number, 
            defaults={'state': 'waiting_for_quantity'}
        )

        if incoming_msg.lower() == 'hi':
            msg.body("Hello! How can I assist you today? Please provide the quantity of products you want to order.")
            session.state = 'waiting_for_quantity'
            session.save()
            return HttpResponse(str(response), content_type='text/xml')

        elif incoming_msg.lower() == 'previous':
            try:
                last_order = OrderArchive.objects.filter(from_number=from_number).latest('created_at')
                media_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, last_order.pdf_path))
                
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                    from_=settings.TWILIO_WHATSAPP_NUMBER,
                    body="Here is the PDF for your previous order.",
                    to=from_number,
                    media_url=[media_url]
                )

                msg.body("The PDF of your previous order has been sent to you.")
                
            except OrderArchive.DoesNotExist:
                msg.body("You have no previous orders.")

        elif session.state == 'waiting_for_quantity':
            try:
                quantity = float(incoming_msg)
                order_item = OrderItem.objects.create(quantity=quantity, description='', price=0.0)
                session.order_items.add(order_item)
                session.state = 'waiting_for_description'
                session.save()
                msg.body("Please provide a description of the product.")
            except ValueError:
                msg.body("Please send a valid number for quantity.")
        
        elif session.state == 'waiting_for_description':
            current_order_item = session.order_items.last()
            if current_order_item:
                current_order_item.description = incoming_msg
                current_order_item.save()
                session.state = 'waiting_for_price'
                session.save()
                msg.body("Please send the price per product.")
            else:
                msg.body("No order item found. Please start over.")

        elif session.state == 'waiting_for_price':
            try:
                price = float(incoming_msg)
                current_order_item = session.order_items.last()
                if current_order_item:
                    current_order_item.price = price
                    current_order_item.save()
                    session.state = 'waiting_for_add_another'
                    session.save()
                    msg.body("Do you want to add another item? (yes/no)")
                else:
                    msg.body("No order item found. Please start over.")
            except ValueError:
                msg.body("Please send a valid price.")

        elif session.state == 'waiting_for_add_another':
            if incoming_msg.lower() == 'yes':
                session.state = 'waiting_for_quantity'
                session.save()
                msg.body("Please send the quantity of the next product.")
            elif incoming_msg.lower() == 'no':
                order_items = session.order_items.all()
                file_name = f"order_{session.id}.pdf"
                generate_order_pdf_pdfkit(order_items, file_name)

                file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                media_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, file_name))
                
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                    from_=settings.TWILIO_WHATSAPP_NUMBER,
                    body=f"The total cost for your order is: ${calculate_total_cost(order_items)}.",
                    to=from_number,
                    media_url=[media_url]
                )

                msg.body("The order details have been sent to you as a PDF.")

                # Archive the order before deleting the session
                OrderArchive.objects.create(
                    from_number=from_number,
                    pdf_path=file_name
                )

                session.delete()

            else:
                msg.body("Please send 'yes' or 'no'.")

        else:
            msg.body("Sorry, I couldn't understand that. Please send the quantity of the product you want to order.")
            session.state = 'waiting_for_quantity'
            session.save()
            
        return HttpResponse(str(response), content_type='text/xml')
