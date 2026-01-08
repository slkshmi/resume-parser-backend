# Resume Parsing API (Django Backend)
##  Project Overview
This project is a Django backend API that allows users to upload resume PDF files.
The system extracts important details such as email address and phone number from the resume
and returns the extracted data in JSON format.
##  Tech Stack
- Python 3.12
- Django
- pdfplumber (for reading PDF files)
- Regular Expressions (for data extraction)
- Postman (for API testing)

##  Features
- Upload resume files in PDF format
- Extract readable text from the uploaded PDF
- Automatically find email address from the resume
- Automatically find phone number from the resume
- Send the extracted details as a JSON response
- Basic validation and error handling for invalid or unsupported files


## API Details

### Resume Upload API
This API endpoint is used to upload a resume in PDF format.
Once the file is uploaded, the backend processes the resume and extracts basic contact information.

- **Endpoint URL:** /api/upload-resume/
- **HTTP Method:** POST
- **Request Type:** form-data
- **Form Key:** resume
- **File Type:** PDF

### Sample API Response
After successfully processing the resume, the API returns a JSON response like the example below:

```json
{
  "name": "",
  "email": "example@gmail.com",
  "phone": "9876543210"
}

##  How to Run the Project Locally

1. Clone the repository from GitHub

2. Open the project folder and create a virtual environment

3. Activate the virtual environment

4. Install the required dependencies

5. Run the Django development server

6. Test the API using Postman at  http://127.0.0.1:8000/api/upload-resume/





