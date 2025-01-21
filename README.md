# Gen AI Project

## Overview
The **Gen AI Project** is a comprehensive application showcasing advanced Generative AI capabilities. This all-in-one platform provides multiple functionalities, including a **Streamlit interface** for interactive usage and partially converted **Django components** for robust backend operations. It is designed to serve as a versatile tool for AI-driven solutions, making it suitable for a variety of use cases.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment setup (recommended)
- Node.js (if applicable for frontend asset builds)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Gen-AI-Project
Set Up Virtual Environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run Streamlit App: Navigate to the streamlit directory and start the Streamlit server:

bash
Copy
Edit
cd streamlit
streamlit run app.py
Run Django Backend: Navigate to the django directory and start the Django development server:

bash
Copy
Edit
cd django
python manage.py runserver
Access the Application:

Streamlit UI: http://localhost:8501
Django Admin Panel: http://localhost:8000/admin
