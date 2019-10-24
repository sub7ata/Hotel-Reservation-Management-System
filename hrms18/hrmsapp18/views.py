from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ManagerSerializer,GuestSerializer,HotelSerializer,RoomSerializer
from .models import Hotel, Manager, Guest, Booking, Room

from  rest_framework import generics
from  rest_framework.permissions import IsAdminUser

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def perform_create(self, serializer):
        try:
            room = Room.objects.get(room_no = self.request.data['room_no'])
            if room:
                raise ValueError("already exist!")

        except Room.DoesNotExist:
            pass
        serializer.save(room_no = self.request.data['room_no'], room_type = self.request.data['room_type'])

    # def list(self,request):
    #     queryset =self.get_queryset()
    #     serializer =RoomSerializer(queryset,many =True)
    #     return Response(serializer.data)

class HotelView(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
# Create your views here.

class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()

class GuestView(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

@api_view(['GET', ])
def api_hotel_list_view(request):
    hotels = Hotel.objects.all()
    if request.method == 'GET':
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

#
# class BookingView(viewsets.ModelViewSet):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()
#
# class RoomView(viewsets.ModelViewSet):
#     serializer_class = RoomSerializer
#     queryset = Room.objects.all()



# @api_view(['GET', ])
# def api_manager_list_view(request):
#     manager = Manager.objects.all()
#     if request.method == 'GET':
#         serializer = ManagerSerializer(manager, many=True)
#         return Response(serializer.data)

@api_view(['GET'])
def api_manager(request, id):
    if request.method == 'GET':
        try:
            manager = Manager.objects.get(id=id)
        except Manager.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = ManagerSerializer(manager)
    return Response(serializer.data)

@api_view(['GET', ])
def api_manager_list_view(request):
    managers = Manager.objects.all()
    if request.method == 'GET':
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def api_manager_put(request, id):
    try:
        manager = Manager.objects.get(id=id)
    except Manager.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ManagerSerializer(manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'update done'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def api_manager_post(request,id):
    try:
        manager = Manager.objects.get(id=id)
    except Manager.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method =='POST':
        serializer=ManagerSerializer(manager,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data ={}
            data['success'] = 'post successfull'

            return Response(status.HTTP_201_CREATED)

    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_delete(request,id):

    try:
        manager = Manager.objects.get(id=id)
    except Manager.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    data = {}
    if request.method == 'DELETE':
        operation = manager.delete()
        if operation:
            data['success'] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data, status=status.HTTP_200_OK)
    # else:
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
