from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage


def home(request):
    return render(request, 'home.html')


@require_POST
def contact_submit(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    phone = request.POST.get('number', '').strip()  # matching current 'number' field name in template
    message = request.POST.get('content', '').strip()  # matching current 'content' field name in template

    if not name or not email or not message:
        return JsonResponse({
            'success': False,
            'message': 'Please fill in all required fields (Name, Email, and Message).'
        }, status=400)

    if '@' not in email or '.' not in email:
        return JsonResponse({
            'success': False,
            'message': 'Please provide a valid email address.'
        }, status=400)

    try:
        # Save to Database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Send Email Notification
        subject = f"New Portfolio Message from {name}"
        body = (
            f"You received a new message from your portfolio website:\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone if phone else 'N/A'}\n\n"
            f"Message:\n{message}\n"
        )
        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.PORTFOLIO_CONTACT_EMAIL],
                fail_silently=False,
            )
        except Exception:
            # Silence email errors to ensure database save succeeds regardless of SMTP settings
            pass

        return JsonResponse({
            'success': True,
            'message': 'Your message has been sent successfully. Thank you!'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'An error occurred while saving your message. Please try again.'
        }, status=500)