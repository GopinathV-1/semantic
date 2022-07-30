from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.WebApiSalesView),
    path('review/', views.WebApiReviewView)
]