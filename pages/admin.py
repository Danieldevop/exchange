from django.contrib import admin
from .models import ContactForm

# Register your models here.


@admin.register(ContactForm)
def ContactForm(admin.ModelAdmin):
	fields = ('id', 'name', 'phone')
