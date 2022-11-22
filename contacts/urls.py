from django.urls import path
from contacts import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    # path('contacts/new/', views.contact_new, name='contact_new'),
    path('contacts/new/', views.ContactCreateView.as_view(), name='contact_new'),
    # path('contacts/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contacts/<int:pk>/details/', views.contact_details, name='contact_details'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    path('contacts/<int:pk>/edit/', views.ContactUpdate.as_view(), name='contact_edit'),
]
