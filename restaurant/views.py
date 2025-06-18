from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


class BookingView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MenuView(APIView):
    def get(self, request):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

def index(request): 
     return render(request, 'index.html', {})

def home(request):
    return render(request, 'home.html', {})