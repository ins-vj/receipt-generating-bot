# receipt-generating-bot
 Django-based WhatsApp bot for placing and managing orders. Users interact with the bot to specify product details, and it generates PDFs of their orders using 'pdfkit'. It also supports retrieving previous order summaries.
# WhatsApp Bot Project

This project is a WhatsApp bot built with Django. Follow the steps below to set up your environment and get the bot running.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setting Up the Project

### 1. Clone the Repository

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up Virtual environment
```bash
python -m venv env![WhatsApp Image 2024-08-16 at 10 48 00 PM](https://github.com/user-attachments/assets/8cc684cb-3c9d-4310-bda5-87c9e45e6b73)

source env/bin/activate  # On Windows use `env\Scripts\activate`

```
### 4. Configure settings.py
       add your credentials in settings.py

### 5. Set up ngrok

### 6. Set up twilio on their website

### 7. Migrate the database
```bash
python manage.py migrate
```

### 8. Start Django Server
```bash
python manage.py runserver
```

# Walkthrough
## Starting
![WhatsApp Image 2024-08-16 at 10 48 00 PM](https://github.com/user-attachments/assets/42886493-0d39-4bd2-8317-54eb81da8bec)

## Adding more items
![WhatsApp Image 2024-08-16 at 10 48 04 PM](https://github.com/user-attachments/assets/fd3bb952-8da8-400c-9f4a-60db3fd796a1)

## PDF
![WhatsApp Image 2024-08-16 at 10 48 10 PM](https://github.com/user-attachments/assets/9a28938a-f2cc-45cc-9350-40436e41a98d)

## Previous Receipt
![WhatsApp Image 2024-08-16 at 10 48 15 PM](https://github.com/user-attachments/assets/06e7941f-36dc-4f4d-a28a-f65cf4767062)

##Server side
![Screenshot from 2024-08-16 22-47-28](https://github.com/user-attachments/assets/a3d07bc4-c880-44b5-88fc-dbcd34b7f47e)
