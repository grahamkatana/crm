from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path('<int:pk>/',views.clients_details,name='client_details'),
    # path('<int:pk>/delete',views.delete_lead,name='delete_lead'),
    # path('<int:pk>/edit',views.edit_lead,name='edit_lead'),
    # path('<int:pk>/convert',views.convert_to_client,name='convert_to_client'),
    # path('add-lead/',views.add_lead,name='add_lead'),

]
