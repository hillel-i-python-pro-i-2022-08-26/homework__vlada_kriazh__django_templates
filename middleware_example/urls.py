from django.urls import path
from middleware_example import views

app_name = 'middleware'

urlpatterns = [path('alldata/', views.all_data, name='index'),
               path('userdata/', views.data_by_user, name='user_data'),
               path('sessiondata/', views.data_by_session, name='session_data'),
               ]
