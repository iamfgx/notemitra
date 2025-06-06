from django.db import models
from .supabase_upload import upload_to_supabase
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Note(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='temp_uploads/')
    pdf_url = models.URLField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pdf_file and not self.pdf_url:
            filename = f"notes_pdfs/{self.pdf_file.name}"
            self.pdf_url = upload_to_supabase(self.pdf_file, filename)
        super().save(*args, **kwargs)
    
class Syllabus(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"