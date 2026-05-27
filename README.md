# Apple-Inspired Full-Stack Portfolio & AI Hub

An ultra-premium, responsive portfolio website designed in the minimalist dark aesthetic of Apple product pages. This project highlights a full-stack Django architecture integrated with a customized SQLite/MySQL database, interactive front-end components, and optimized capabilities for Generative AI and Large Language Model (LLM) workflows.

---

## 🚀 Live Demo & Repository
* **Live Website**: [django-portfolio-hub.onrender.com](https://django-portfolio-hub.onrender.com/)
* **Local Workspace**: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)
* **GitHub Repository**: [github.com/dhairyashilmore/djprojects](https://github.com/dhairyashilmore/djprojects)

---

## 🛠️ Technology Stack
* **Backend**: Django (Python), Django REST Framework, FastAPI
* **Generative AI**: LLM APIs (OpenAI GPT-4, Anthropic Claude), Retrieval-Augmented Generation (RAG), Vector Databases (ChromaDB, Pinecone, FAISS)
* **Frontend**: React.js, Vanilla CSS3 (Glassmorphism, Bento Grid layouts), ES6+ JavaScript
* **Database**: SQLite (Development) / MySQL (Production)
* **Tools & Hosting**: Git & GitHub, AWS, Postman, Linux

---

## ✨ Core Features
* **Apple Pro Dark Aesthetic**: Sleek color palette (`#000000` base, translucent glassmorphism panels, and clean capsule outline accents).
* **AI-First Skills Hub**: Interactive dashboard dynamically comparing skill proficiencies across AI & Gen AI, Backend, Languages, and Tools.
* **Responsive Bento Grid**: Beautiful layout showcasing academic credentials and Generative AI specializations.
* **Projects Showcase**: Apple-style sliding showcase panels highlighting project mockups, specifications, and repositories:
  * **AI Trace Finder** (OpenCV, Machine Learning)
  * **AI-Powered Job Tracker** (React, Django, MySQL, LLM APIs)
  * **Food Connect** (HTML, CSS, JS, Node.js, Firebase)
* **Full-Stack Contact form**: Asynchronous AJAX form submitting messages to a custom database model without page reloading.
* **Email Notification Logging**: Automatic server email dispatching logic that notifies you upon new form submissions (currently configured to print to the terminal console).

---

## 💻 Local Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/dhairyashilmore/djprojects.git
cd djprojects/portfolio
```

### 2. Set up virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django
# Add any other project requirements if applicable
```

### 4. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver 8080
```
Open [http://127.0.0.1:8080/](http://127.0.0.1:8080/) in your browser to view the live local page.

---

## 📧 Email Notification Setup (SMTP)
To switch notifications from the terminal console to real email delivery, open `portfolio/settings.py` and replace the console backend with your SMTP settings:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password' # App password generated in Google account settings
```
