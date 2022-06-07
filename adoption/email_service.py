from django.core.mail import send_mail


def sendEmailConfirmation(adoption):
    subject = "The adoption was sucessfull"
    content = f"Congrats {adoption.email},  you have saved {adoption.pet.name}, by $ {adoption.price} per month."
    sender = "adoptpetpytho@gmail.com"
    receiver = [adoption.email]
    send_mail(subject, content, sender, receiver)
