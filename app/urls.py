from django.urls import path
from app import views


urlpatterns = [
    path('', views.index, name="Home"),
    path('/about/', views.about),
    path('token/', views.token, name="token"),
    path('pay/', views.pay, name="pay"),
    path('stk/', views.stk, name="stk"),
    path('services/', views.services),
    path('contacts/', views.contact)
]
