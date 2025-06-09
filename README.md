# 📚 NoteMitra – College Notes Web App

A smart note-sharing platform where admins can upload **subject-wise notes and syllabus PDFs**, securely stored using **Supabase Storage**, and accessed easily by students.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-Framework-darkgreen?style=flat-square&logo=django)
![Supabase](https://img.shields.io/badge/Supabase-Storage%20Cloud-brightgreen?style=flat-square&logo=supabase)
![Status](https://img.shields.io/badge/Status-Active-blueviolet?style=flat-square)

---

## ✨ Features

- 📁 **Subject-wise PDF Uploads**  
  Upload notes and syllabus PDFs via Django admin.

- ☁️ **Supabase Storage Integration**  
  Store files in public buckets on Supabase, with secure URLs.

- 🔗 **Public Access Links**  
  Auto-generated public download URLs for uploaded files.

- 🔐 **Admin Panel for Management**  
  All uploads managed through Django Admin Interface.

- 🚀 **Render Deployment Ready**  
  Fully configured for deployment on [Render](https://render.com).

---

## 🛠️ Tech Stack

| Area            | Tech/Library         |
|-----------------|----------------------|
| Backend         | Django (Python)      |
| Cloud Storage   | Supabase             |
| Deployment      | Render               |
| Styling         | Bootstrap (CSS)      |
| File Upload     | Supabase Python SDK  |
| PDF Handling    | Django File Upload   |

---

## ⚙️ Setup Instructions

### 🔐 Add Environment Variables in `.env` file:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-supabase-anon-key
SUPABASE_BUCKET=notes-pdfs
SYLLABUS_BUCKET=syllabus-pdfs  # optional
```
---

## 📦 Install Dependencies
```
pip install -r requirements.txt
```
---

## 🔄 Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
---

## 👤 Create Superuser
```
python manage.py createsuperuser
```
---

## ▶️ Run Server
```
python manage.py runserver
```
---

## 🌍 Deployment on Render
```Push code to GitHub.

Create a Web Service on Render.

Add Build & Start commands:

Build: pip install -r requirements.txt

Start: gunicorn collegenotes.wsgi

Set environment variables on Render:

SUPABASE_URL

SUPABASE_KEY

SUPABASE_BUCKET

Deploy and enjoy!
```
---

## 📁 Folder Structure
```
collegenotes/
├── NoteMitra/            # Main App
│   ├── models.py         # Notes & Syllabus Models
│   ├── admin.py          # Admin Config
│   └── views.py, urls.py
├── collegenotes/         # Project Settings
├── supabase_upload.py    # File Upload Handler
├── .env                  # Environment Config
├── requirements.txt
└── README.md
```
---

## 📜 License
```
This project is for educational and demo purposes only.
Feel free to customize and expand it as per your needs.
```
