# 📚 NoteMitra

NoteMitra is a Django-based web application that enables college students to upload, organize, and access subject-wise study materials — including Notes and Important Questions — according to their syllabus. It integrates with Supabase for secure cloud storage of PDF files and is ready for deployment on platforms like Render.

---

## 🚀 Features

- 🔐 **User-friendly Admin Interface** for uploading study content
- ☁️ **Supabase Storage Integration** for secure cloud-based PDF uploads
- 📄 **Subject-wise Categorization** of Notes and Important Questions (IMP Qus.)
- 🌐 **Responsive UI** built with Bootstrap for smooth navigation
- 📥 One-click **PDF Download** functionality for students
- 🔎 Clean and accessible design with a clear separation of views: Notes, Syllabus, Feedback, and Subject Listing

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** PostgreSQL (default Django DB or custom)
- **Storage:** Supabase Storage Buckets
- **Deployment:** Render
- **Others:** Environment variable support using `.env`

---

## 📁 Project Structure

collegenotes/
├── NoteMitra/
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ ├── admin.py
│ ├── models.py
│ ├── urls.py
│ ├── views.py
│ └── ...
├── collegenotes/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── manage.py
├── .env
├── requirements.txt
└── README.md


