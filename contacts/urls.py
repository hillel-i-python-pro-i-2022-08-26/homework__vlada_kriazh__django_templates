from django.urls import path
from contacts import views

app_name = 'contacts'

urlpatterns = [
    path('', views.get_contacts, name='index'),
    path('contact/new/', views.contact_new, name='contact_new'),
    path('contact/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/<int:pk>/details/', views.contact_details, name='contact_details'),
    path('contact/<int:pk>/delete/', views.contact_delete, name='contact_delete')
]
