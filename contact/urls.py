from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # CRUD Contact
    path('contact/create', views.create, name='create'),
    path('contact/<int:contact_id>/details', views.contact, name='contact'),

    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
