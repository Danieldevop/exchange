from django.contrib import admin
from .models import ContactForm, ExchangeForm

# Register your models here.


@admin.register(ContactForm)
class ContactForm(admin.ModelAdmin):
	list_display = ('id', 'name', 'phone')
	fields = ('name', 'surname', 'phone', 'email', 'message')


@admin.register(ExchangeForm)
class ContactForm(admin.ModelAdmin):
	list_display = ('id', 'name', 'phone')


