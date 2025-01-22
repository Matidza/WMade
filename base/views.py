from django.conf import settings
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        # Get input data from the form
        fullname = request.POST.get('fullname', '').strip()
        subject = request.POST.get('subject', '').strip()
        email = request.POST.get('email', '').strip().lower()
        message = request.POST.get('message', '').strip()

        try:
            # Construct the email to the website owner
            email = EmailMessage(
                subject=f"Room Inquiry: {subject}",  # Include "Room Inquiry" to make it clear
                body=f"Message from {fullname} ({email}):\n\n{message}",  # The message content
                from_email=settings.EMAIL_HOST_USER,  # Must match the SMTP email
                to=[settings.EMAIL_HOST_USER],  # Send to the website owner
                reply_to=[email],  # Reply goes to the user who filled out the form
            )

            email.send(fail_silently=False)

            success_message = "Your inquiry has been sent successfully!"
            return render(request, 'index.html', {'success_message': success_message})

        except BadHeaderError:
            error_message = "Invalid header found."
        except Exception as e:
            error_message = f"An error occurred: {e}"

        return render(request, 'index.html', {'error_message': error_message})

    # Render the form for GET requests
    return render(request, 'index.html')








# Test configuration
''''
def email(request):    
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',] 

    send_mail( subject, message, email_from, recipient_list ) 

    return redirect('redirect to a new page')
'''

def my_view(request):
    ascii_art = """
                /_/\
                ( o.o )
                > ^ <
                """
    return HttpResponse(ascii_art, content_type='text/plain')