# receipt-generating-bot
 Django-based WhatsApp bot for placing and managing orders. Users interact with the bot to specify product details, and it generates PDFs of their orders using 'pdfkit'. It also supports retrieving previous order summaries.
# WhatsApp Bot Project

This project is a WhatsApp bot built with Django. Follow the steps below to set up your environment and get the bot running.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setting Up the Project

### 1. Clone the Repository

### 2. Set up Virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

```
### 3. Configure settings.py
       add your credentials in settings.py

### 4. Set up ngrok

### 5. Set up twilio on their website

### 6. Migrate the database
```bash
python manage.py migrate
```
### 7. Start Django Server
```bash
python manage.py runserver
```
