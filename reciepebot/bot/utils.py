# Description: This file contains the template of pdf file which is ssent to the user.


import os
import pdfkit
from django.conf import settings

def generate_order_pdf_pdfkit(order_items, file_name):
    # Ensure MEDIA_ROOT directory exists
    output_path = os.path.join(settings.MEDIA_ROOT, file_name)

    # HTML content for the PDF
    html_content = """
    <html>
    <head>
        <title>Order Details</title>
        <style>
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid #ddd; padding: 8px; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Vikrant's Bot</h1>
        <h2>Order Details</h2>
        <table>
            <thead>
                <tr>
                    <th>Quantity</th>
                    <th>Description</th>
                    <th>Price</th>
                    <th>Total</th>
                </tr>
            </thead>
            <tbody>
    """
    total_cost = 0
    for item in order_items:
        item_total = item.quantity * item.price
        total_cost += item_total
        html_content += f"<tr><td>{item.quantity}</td><td>{item.description}</td><td>${item.price:.2f}</td><td>${item_total:.2f}</td></tr>"
    
    html_content += f"""
            </tbody>
        </table>
        <p><strong>Total Cost:</strong> ${total_cost:.2f}</p>
    </body>
    </html>
    """

    # Convert HTML to PDF
    pdfkit.from_string(html_content, output_path)

    return file_name
