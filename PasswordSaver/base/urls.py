from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='Login'),
    path('register/', views.register, name='Register'),
    path('about/',views.about,name='About'),
    path('home',views.home,name='Home'),
    path('website',views.website,name='Website'),
    path('card',views.card,name='Card'),
    path('add_web_password',views.add_web_pass,name='Add Details For Website'),
    path('website_details/<str:pk>/',views.website_details,name='Details of Website'),
    path('add_card_password',views.add_card_pass,name='Add Details For Card'),
    path('card_details/<str:pk>/',views.card_details,name='Details of Card'),
    path('website_delete/<str:pk>/',views.website_delete,name='Delete a Website'),
    path('card_delete/<str:pk>/',views.card_delete,name='Delete a Card'),

]