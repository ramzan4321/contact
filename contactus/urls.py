from django.urls import path
from contactus import views

urlpatterns = [
    path('contact/', views.ContactCreate.as_view()),
    path('contactlist/', views.ContactList.as_view()),
    path('contactlist/<int:pk>', views.ContactRUD.as_view()),
    path('admin_register_/', views.AdminRegister.as_view()),
]