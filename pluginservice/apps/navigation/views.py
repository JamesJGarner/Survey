from django.views.generic import DetailView
from .models import Page

class PageDetail(DetailView):
    model = Page
    template_name = 'site/navigation-page.html'
    slug_field = 'slug'
    slug_url_kwarg = 'page_slug'