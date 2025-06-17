from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactForm

def contact_inquiry(request):
    """
    Handle the contact form submission and process the inquiry.
    
    This view function processes the contact form data, saves it to the database,
    and sends notification emails to both the admin and the customer.
    
    Args:
        request (HttpRequest): The HTTP request object containing form data if POST
        
    Returns:
        HttpResponseRedirect: Redirects to the contact page after processing
        
    Note:
        - POST requests will process form data and send emails
        - GET requests will redirect to the contact page
        - All form fields (name, email, phone, subject, message) are required
    """
    if request.method == 'POST':
        # print("Contact form submitted")
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save the inquiry to the database
        inquiry = ContactForm(
            name=name,
            email=email,
            phone_number=phone,
            subject=subject,
            message=message
        )
        inquiry.save()
        print
        
        # Send email notification
        admin_email_sent = mail_to_admin(name, email, phone, subject, message)    
                 
        # Send confirmation email to the customer
        customer_email_sent = mail_to_customer(name, email, subject, message)
        
        # Add a success message
        if admin_email_sent and customer_email_sent:
            messages.success(request, "Thank you for your message! We have received your inquiry and will contact you soon.")
        elif customer_email_sent:
            messages.success(request, "Thank you for your message! We have received your inquiry and will contact you soon.")
        else:
            messages.warning(request, "Your inquiry has been saved, but there was an issue sending email notifications. We'll still process your request.")

        return redirect('/contact')
    
    else:
        return redirect('/contact')  



def mail_to_admin(name, email, phone, subject, message):
    """
    Send a notification email to the admin about a new contact form submission.
    
    This function composes and sends an email to the site administrator
    containing details of the new contact form submission.
    
    Args:
        name (str): The name of the person who submitted the form
        email (str): The email address of the person who submitted the form
        phone (str): The phone number of the person who submitted the form
        subject (str): The subject of the inquiry
        message (str): The detailed message/inquiry from the customer
        
    Returns:
        bool: True if the email was sent successfully, False otherwise
        
    Note:
        - Uses the site's DEFAULT_FROM_EMAIL setting for sending
        - Logs success or failure of email sending to the console
        - Email is sent to the address specified in DEFAULT_FROM_EMAIL
    """
    email_subject = f"New Contact Form Submission: {subject}"
    email_message = f"""
    You have received a new contact form submission from your website:

    Name: {name}
    Email: {email}
    Phone: {phone}
    Subject: {subject}

    Message:
    {message}

    This message has been saved to your database.
"""
    # Send to admin
    try:
        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],  # Send to site admin email
            fail_silently=False,
        )
        print("Email sent to admin successfully.")
        return True
        
    except Exception as e:
        # Handle any errors that occur during email sending
        print(f"Error sending email to admin: {e}")
        return False


def mail_to_customer(name, email, subject, message):
    """
    Send a confirmation email to the customer who submitted the contact form.
    
    This function composes and sends an acknowledgment email to the customer,
    confirming receipt of their inquiry and providing a summary of their
    submission details.
    
    Args:
        name (str): The name of the customer
        email (str): The email address to send the confirmation to
        subject (str): The original subject of the customer's inquiry
        message (str): The original message from the customer
        
    Returns:
        bool: True if the email was sent successfully, False otherwise
        
    Note:
        - Uses the site's DEFAULT_FROM_EMAIL setting as the sender
        - Logs success or failure of email sending to the console
        - The email includes the original inquiry details for reference
    """
    customer_subject = "Thank you for contacting Dwarkesh Events"
    customer_message = f"""
    Dear {name},

    Thank you for contacting Dwarkesh Events. We have received your inquiry and will get back to you shortly.

    Your message details:
    Subject: {subject}
    Message: {message}

    Best regards,
    Dwarkesh Events Management Team
"""
    try:
        send_mail(
            customer_subject,
            customer_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],  # Send to customer's email
            fail_silently=False,
        )
        print("Confirmation email sent to customer successfully.")
        return True
    except Exception as e:
        print(f"Error sending email to customer: {e}")
        return False