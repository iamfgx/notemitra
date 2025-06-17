from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'contact', 'subject', 'notes', 'notes_list', 'feedback', 'syllabus_list', 'upload_view', 'upload_syllabus']

    def location(self, item):
        return reverse(item)
