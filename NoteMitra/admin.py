from django.contrib import admin
from .models import Subject, Note, Feedback, Syllabus
# Register your models here.
class subject_admin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Subject,subject_admin)
class notes_admin(admin.ModelAdmin):
    list_display = ['subject','title','pdf_url','pdf_file','uploaded_at']
admin.site.register(Note,notes_admin)

class Syllabus_admin(admin.ModelAdmin):
    list_display = ['subject','title','pdf_url','uploaded_at']
admin.site.register(Syllabus,Syllabus_admin)
admin.site.register(Feedback)