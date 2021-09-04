from rest_framework import serializers
from demo.models import *




class SchoolSerializer(serializers.ModelSerializer):
    def get_stops(self,obj):
        stops = Route.objects.filter(school_id=obj.id)

        return RouteSerializer(stops, many=True).data
    
    stops = serializers.SerializerMethodField()



    class Meta:
        model = School
        fields = '__all__'



class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'