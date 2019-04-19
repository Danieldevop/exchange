from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ContactForm

class HomeView(TemplateView):
	template_name = "pages/index.html"

class ContactView(TemplateView):
	template_name = "pages/contact.html"

	def post(self, request):
		pass

class DevView(TemplateView):
	template_name = "pages/developers.html"