from django.contrib.auth.models import User
from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from demo.models import *





class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_queryset(self):
        try:
            return School.objects.filter(school_name__in=Route.objects.all())
        except School.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    # def list(self,request, *args, **kwargs):
    #     queryset=self.queryset.all()
    #     school=School.objects.filter()
    #     print(school)
    #     for school in school:
    #         print(school)

    #         return Response(
    #             {
    #                 'school_id':self.get_serializer(queryset.filter(school_id=school), many=True).data
    #             }
    #         )

        # try:
        #     obj=Route.objects.filter(school_id=1)
            
        #     print(obj)
        #     return Route.objects.filter(school_id=1)
        # except Route.DoesNotExist as e:
        #     return Response(status=status.HTTP_404_NOT_FOUND)