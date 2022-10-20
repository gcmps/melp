import statistics
from django.http import HttpResponse
from django.views import View
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework import generics


class IndexView(View):

    def index(request):

        return HttpResponse("Hello Intelimétrica!")


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class StatisticsList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_fields = ('lat', 'lng')
    name = 'statistics'