from django.urls import path
from .views import home,about,contact,notes,subject,feedback_view,notes_list,syllabus_list, note_view, syllabus_upload_view
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
urlpatterns = [
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('notes/',notes, name='notes'),
    path('subject/',subject, name='subject'),
    path('feedback/', feedback_view, name='feedback'),
    path('notes_list/', notes_list, name='notes_list'),
    path('syllabus_list/', syllabus_list, name='syllabus_list'),
    path('upload_notes_view/', note_view, name='upload_view'),
    path('upload_syllabus/', syllabus_upload_view, name='upload_syllabus'),
    path("ping/", lambda request: HttpResponse("pong")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
