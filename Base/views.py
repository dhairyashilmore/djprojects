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


@require_POST
def chat_respond(request):
    message = request.POST.get('message', '').strip().lower()

    if not message:
        return JsonResponse({'response': "I didn't receive a message. How can I help you today?"})

    # Rule-based matching logic
    if any(k in message for k in ['hi', 'hello', 'hey', 'greetings', 'hola', 'sup']):
        response = "Hello! I am Dhairyashil's virtual assistant. Ask me about his technical skills, projects, work experience, education, or certifications!"
    elif any(k in message for k in ['skill', 'tech', 'languages', 'backend', 'frontend', 'framework', 'database']):
        response = "Dhairyashil is a Python Full Stack & AI Engineer. His primary skills include:\n\n" \
                   "• **Backend**: Python, Django, Django REST Framework, FastAPI, REST APIs, JWT Auth\n" \
                   "• **Frontend**: React (basics), HTML5, CSS3, JavaScript\n" \
                   "• **Databases**: MySQL, MongoDB, Vector Databases (ChromaDB, Pinecone)\n" \
                   "• **AI / Gen AI**: Generative AI APIs (OpenAI, Claude), RAG Pipelines, Machine Learning"
    elif any(k in message for k in ['project', 'code', 'github', 'portfolio', 'work']):
        response = "He has worked on several key projects:\n\n" \
                   "1. **AI Trace Finder**: Forensic ML app analyzing sensor pattern noise to identify image scanners.\n" \
                   "2. **AI-Powered Job Tracker**: Django & React tracking system integrated with an LLM outreach drafting agent.\n" \
                   "3. **Food Connect**: Real-time food distribution platform utilizing Node.js and Firebase.\n\n" \
                   "Check out his repositories on [GitHub](https://github.com/dhairyashilmore)."
    elif any(k in message for k in ['experience', 'job', 'work', 'history', 'company', 'insurance', 'support', 'trainee']):
        response = "Dhairyashil's professional history includes:\n\n" \
                   "• **Application Support Engineer** at Bajaj Allianz Life Insurance (Jan 2026 – Present): Technical support, database validation, policy mappings, log analysis, and troubleshooting.\n" \
                   "• **Python Developer Trainee** at Kiran Academy (Jul 2025 – Dec 2025): Full-stack training, API design, and schema optimizations."
    elif any(k in message for k in ['education', 'college', 'degree', 'cgpa', 'university', 'diploma']):
        response = "His educational qualifications:\n\n" \
                   "• **B.E. in Artificial Intelligence & Data Science** (2025) from P. R. Pote Patil College of Engineering, Amravati. CGPA: 8.27/10.\n" \
                   "• **Diploma in Computer Science** (2022) from Shreeyash College of Engineering, Chhatrapati Sambhajinagar. Percentage: 82%."
    elif any(k in message for k in ['certification', 'certify', 'nptel', 'aws', 'iit']):
        response = "His certifications include:\n\n" \
                   "• **Python Full Stack Development** (Kiran Academy, 2025)\n" \
                   "• **Python for Data Science** (NPTEL & IIT Madras, 2024)\n" \
                   "• **AWS Academy Cloud Foundations** (Amazon Web Services, 2024)"
    elif any(k in message for k in ['contact', 'email', 'phone', 'hire', 'talk', 'connect', 'reach']):
        response = "You can contact Dhairyashil directly through:\n\n" \
                   "• **Email**: dhairyashilmore2003@gmail.com\n" \
                   "• **Phone**: +91-9823563994\n\n" \
                   "Or send a message through the 'Get in Touch' form at the bottom of the page!"
    elif any(k in message for k in ['resume', 'cv', 'download']):
        response = "You can view and download his latest resume PDF by clicking the 'View Resume' button at the top of the page."
    else:
        response = "I'm not sure about that. Feel free to ask me about his 'skills', 'projects', 'work experience', 'education', or 'how to contact' him!"

    return JsonResponse({'response': response})