from django.shortcuts import render
from viewApp.models import Student
from viewApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
# When pagination is enabled at the class level:
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from rest_framework import generics, mixins
from rest_framework import viewsets


# Create your views here.
# Only when a custom  number of pages is required at the class level


class StudentPagination(PageNumberPagination):
    page_size = 1


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # When pagination is enabled at the class level but it is using the global number of pages:
    # pagination_class = PageNumberPagination
    # If we want to use a different number of pages at the class level, the new
    # class Student pagination is needed
    pagination_class = StudentPagination
    #pagination_class = LimitOffsetPagination


# As an alternative for only READ purposes:
'''
class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
'''
