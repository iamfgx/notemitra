from django.shortcuts import render,redirect,HttpResponse
from .models import Subject, Note, Feedback, Syllabus
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def notes(request):
    return render(request, 'notes.html')

def subject(request):
    return render(request, 'subject.html')



def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to DB
        Feedback.objects.create(name=name, email=email, message=message)

        return render(request, 'feedback_success.html')
    else:
        return render(request, 'contact.html', {'error': 'Galat entry fir se fill kar.'})
    return render(request, 'contact.html')


def notes_list(request):
    notes = Note.objects.all().order_by('-uploaded_at')  # latest first
    return render(request, 'notes_list.html', {'notes': notes})

def syllabus_list(request):
    syllabu = Syllabus.objects.all().order_by('-uploaded_at')  # latest first
    return render(request, 'syllabus_list.html', {'syllabu': syllabu})



from .supabase_upload import upload_to_supabase

def note_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        subject_id = request.POST.get('subject_id')
        file = request.FILES['pdf_file']

        filename = f"notes_pdfs/{file.name}"
        file_url = upload_to_supabase(file, filename)

        subject_obj = Subject.objects.get(id=subject_id)
        Note.objects.create(subject=subject_obj, title=title, pdf_url=file_url)

        return redirect('notes_list')  # Or any success page

    subjects = Subject.objects.all()
    return render(request, 'upload_note.html', {'subjects': subjects})

# SYLLABUS UPLOAD VIEW

def syllabus_upload_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        subject_id = request.POST.get('subject_id')
        file = request.FILES['pdf_file']

        filename = f"syllabus_pdfs/{file.name}"
        file_url = upload_to_supabase(file, filename)

        subject_obj = Subject.objects.get(id=subject_id)
        Syllabus.objects.create(subject=subject_obj, title=title, pdf_url=file_url)

        return redirect('syllabus_list')

    subjects = Subject.objects.all()
    return render(request, 'upload_syllabus.html', {'subjects': subjects})


# SEO configuration

from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        f"Sitemap: https://notemitra.onrender.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
