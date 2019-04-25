from django.urls import path, include
from .views import HomeView, ExchangeFormView, SuccessView

urlpatterns = [

    path('', HomeView.as_view() ,name='home-page'),
    path('intercambio', ExchangeFormView.as_view(), name='exchange-form'),
    path('success', SuccessView.as_view(), name="success")
]
