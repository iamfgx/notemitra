from django.contrib import admin
from .models import Subject, Note, Feedback, Syllabus
from .supabase_upload import upload_to_supabase
# Register your models here.
class subject_admin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Subject,subject_admin)


class notes_admin(admin.ModelAdmin):
    list_display = ['subject','title','pdf_url','pdf_file','uploaded_at']
    fields = ['subject', 'title', 'pdf_file']

    def save_model(self, request, obj, form, change):
        if 'pdf_file' in request.FILES:
            file = request.FILES['pdf_file']
            filename = f"notes_pdfs/{file.name}"
            file_url = upload_to_supabase(file, filename)
            obj.pdf_url = file_url
        super().save_model(request, obj, form, change)
admin.site.register(Note,notes_admin)



class Syllabus_admin(admin.ModelAdmin):
    list_display = ['subject','title','pdf_url','pdf_file','uploaded_at']
    fields = ['subject', 'title', 'pdf_file']

    def save_model(self, request, obj, form, change):
        if 'pdf_file' in request.FILES:
            file = request.FILES['pdf_file']
            filename = f"syllabus_pdfs/{file.name}"
            file_url = upload_to_supabase(file, filename)
            obj.pdf_url = file_url
        super().save_model(request, obj, form, change)
admin.site.register(Syllabus,Syllabus_admin)




admin.site.register(Feedback)