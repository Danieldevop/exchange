# Django
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.db import connection
# Models
from .models import ContactForm
import pdb

class HomeView(TemplateView):
	template_name = "pages/index.html"

	def post(self, request):
		return HttpResponseRedirect(reverse('exchange-form'))

class ExchangeFormView(TemplateView):
	template_name = "pages/exchangeForm.html"

	def post(self, request):
		with connection.cursor() as cursor:
			cursor.execute(
				'''
				INSERT INTO pages_exchangeform (name, surname, email, phone, message)
				VALUES (%s, %s, %s, %s, %s)
				''',	
				[
					request.POST['name'], 
					request.POST['surname'], 
					request.POST['email'], 
					request.POST['phone'],
					request.POST['message']
				]
			)

		return HttpResponseRedirect(reverse('success'))

class SuccessView(TemplateView):
	template_name = "pages/success.html"
