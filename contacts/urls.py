# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from contacts import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='index'),
    # path('contacts/new/', views.contact_new, name='contact_new'),
    path('contacts/new/', login_required(views.ContactCreateView.as_view()), name='contact_new'),
    path('contacts/<int:pk>/edit/', login_required(views.ContactUpdate.as_view()), name='contact_edit'),
    path('contacts/<int:pk>/details/', views.contact_details, name='contact_details'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    # path('contacts/<int:pk>/edit/', login_required(views.ContactUpdate.as_view()), name='contact_edit'),
]
