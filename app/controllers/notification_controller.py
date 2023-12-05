from ..models.product import Product
from flask_mail import Message, Mail
from app.controllers import user_controller

def notify_product_change(product: Product) -> None:
    msg_tittle = 'Notification'
    body = product.name + ' was updated'
    sender = 'noreply@app.com'
    recipients = [email[0] for email in user_controller.get_all_users_emails()]
    print(recipients)
    msg  = Message(msg_tittle,sender=sender,recipients=recipients, body=body)
    Mail().send(msg)


