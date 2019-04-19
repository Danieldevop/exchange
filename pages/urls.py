from django.urls import path, include
from .views import HomeView, ContactView, DevView

urlpatterns = [

    path('', HomeView.as_view() ,name='home-page'),
    path('desarrolladores', DevView.as_view(), name="developers"),
    path('contacto', ContactView.as_view(), name='contact')
]
