from django.contrib import admin
from .models import ContactForm

# Register your models here.


@admin.register(ContactForm)
class ContactForm(admin.ModelAdmin):
	fields = ('name', 'phone')
