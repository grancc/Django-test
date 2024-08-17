from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import CarsSerializer
from rest_framework import status
from django.http import JsonResponse
from .models import Cars



class CarsViewSet(ViewSet):
    serializer_class = CarsSerializer
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        try:

            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            car = serializer.save()
            serialized_car = self.serializer_class(car).data
           
            return Response({
                "Success": "Объект успешно создан",
                "car": serialized_car,
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        try:
            car = Cars.objects.get(pk=pk)
            serializer = CarsSerializer(car)
            return Response(serializer.data)
        except Cars.DoesNotExist:
            return JsonResponse({'error': 'Такого объекта не существует'}, status=status.HTTP_400_BAD_REQUEST)
        
    



