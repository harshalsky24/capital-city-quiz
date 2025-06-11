from django.urls import path
from .views import GetCountry, CheckCapital

urlpatterns = [
    path('country/', GetCountry.as_view()),
    path('check/', CheckCapital.as_view()),
]
