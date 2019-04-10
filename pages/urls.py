from django.urls import path, include
from .views import HomeView, ContactView

urlpatterns = [

    path('', HomeView.as_view() ,name='home-page'),
    path('contacto', ContactView.as_view(), name='contact')
]
