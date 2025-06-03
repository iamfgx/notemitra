from django.shortcuts import render,redirect,HttpResponse
from .models import Subject, Note, Feedback, syllabus
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
    syllabu = syllabus.objects.all().order_by('-uploaded_at')  # latest first
    return render(request, 'syllabus_list.html', {'syllabu': syllabu})