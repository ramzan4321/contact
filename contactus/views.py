from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializer import ContactSerializer, UserSerializer
from django.contrib.auth.models import User
# Create your views here.

class ContactList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactCreate(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRUD(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AdminRegister(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()