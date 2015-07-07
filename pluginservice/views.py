from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'site/homepage.html'

class TempProfile(TemplateView):
	template_name = 'site/profile.html'
