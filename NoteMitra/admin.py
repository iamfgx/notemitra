from django.contrib import admin
from .models import Subject, Note, Feedback, syllabus
# Register your models here.
class subject_admin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Subject,subject_admin)
class notes_admin(admin.ModelAdmin):
    list_display = ['subject','title','pdf_file','uploaded_at']
admin.site.register(Note,notes_admin)

class syllabus_admin(admin.ModelAdmin):
    list_display = ['subject','title','pdf_file','uploaded_at']
admin.site.register(syllabus,syllabus_admin)
admin.site.register(Feedback)