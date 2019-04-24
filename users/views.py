from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from .models import User,Student, Faculty
from .serializers import UserSerializer, StudentSerializer, FacultySerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})


class FacultyViewSet(viewsets.ModelViewSet):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()

    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})
