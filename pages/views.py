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
		return HttpResponseRedirect("%s?amount=%s" % (reverse('exchange-form'), request.POST['envias']))

class ExchangeFormView(TemplateView):
	template_name = "pages/exchangeForm.html"

	def get(self, request):
		amount = request.GET.get("amount", None)

		return render(request, self.template_name,{'amount': amount})

	def post(self, request):
		with connection.cursor() as cursor:
			cursor.execute(
				'''
				INSERT INTO pages_exchangeform (amount_to_exchange, name, surname, email, phone)
				VALUES (%s, %s, %s, %s, %s)
				''',	
				[
					request.POST['amount_to_exchange'], 
					request.POST['name'], 
					request.POST['surname'], 
					request.POST['email'], 
					request.POST['phone']
				]
			)

		return HttpResponseRedirect(reverse('success'))

class SuccessView(TemplateView):
	template_name = "pages/success.html"
