from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pdfplumber
import re

@csrf_exempt
def upload_resume(request):
    if request.method == 'POST':
        if 'resume' not in request.FILES:
            return JsonResponse({"error": "No file uploaded"}, status=400)

        resume_file = request.FILES['resume']
	if not resume_file.name.lower().endswith('.pdf'):
    return JsonResponse(
        {"error": "Only PDF files are supported"},
        status=400
    )


        text = ""
        try:
            with pdfplumber.open(resume_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
        except Exception:
            return JsonResponse({"error": "Unable to read PDF"}, status=400)

        # extract email and phone
        email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
        phone_match = re.search(r'\b\d{10}\b', text)

        email = email_match.group(0) if email_match else ""
        phone = phone_match.group(0) if phone_match else ""

        return JsonResponse({
            "name": "",
            "email": email,
            "phone": phone
        })

    return JsonResponse({"error": "Only POST method allowed"}, status=405)
