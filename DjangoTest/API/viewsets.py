from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import CarsSerializer
from rest_framework import status
from django.http import JsonResponse
from .models import Cars
from django.db.models import Q


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

    def list(self, request):
        try:
            fuel_type = request.query_params.get("fuel_type", None)
            transmission_type = request.query_params.get("transmission_type", None)

            brand = request.query_params.get('brand', None)
            model = request.query_params.get('model', None)

            year = request.query_params.get('year', None)
            year_from = request.query_params.get('year_from', None)
            year_to = request.query_params.get('year_to', None)

            mileage = request.query_params.get('mileage', None)
            mileage_min = request.query_params.get('mileage_min', None)
            mileage_max = request.query_params.get('mileage_max', None)

            price = request.query_params.get('price', None)
            price_min = request.query_params.get('price_min', None)
            price_max = request.query_params.get('price_max', None)

            page = int(request.query_params.get("page", 1))
            onPageCount = int(request.query_params.get("onPageCount", 12))

            filter = Q()

            if fuel_type:
                filter &= Q(fuel_type=fuel_type)

            if transmission_type:
                filter &= Q(transmission_type=transmission_type)

            if brand:
                filter &= Q(brand=brand)

            if model:
                filter &= Q(model=model)

            if year and int(year) > 0:
                filter &= Q(year=int(year))
            else: 
                raise ValueError

            if year_from and int(year_from) > 0:
                filter &= Q(year__gte=int(year_from))
            else: 
                raise ValueError

            if year_to and int(year_to)>0:
                filter &= Q(year__lte=int(year_to))
            else: 
                raise ValueError

            if mileage and int(mileage) >= 0:
                filter &= Q(mileage=int(mileage))
            else: 
                raise ValueError

            if mileage_min and int(mileage_min)>=0:
                filter &= Q(mileage__gte=int(mileage_min))
            else: 
                raise ValueError
            
            if mileage_max and int(mileage_max)>=0:
                filter &= Q(mileage__lte=int(mileage_max))
            else: 
                raise ValueError

            if price and int(price)>0:
                filter &= Q(price=int(price))
            else: 
                raise ValueError

            if price_min and int(price)>0:
                filter &= Q(price__gte=int(price_min))
            else: 
                raise ValueError

            if price_max and int(price)>0:
                filter &= Q(price__lte=int(price_max))
            else: 
                raise ValueError


            offset = (page - 1) * onPageCount
            filtered = (
                Cars.objects.filter(filter).order_by()[offset : offset + onPageCount]
            )

            serialized_data =  self.serializer_class(filtered, many=True).data

            return Response({"cars": serialized_data})
        
        except ValueError:
            return JsonResponse({'error': 'Год, цена, должны быть числами больше нуля. Пробег должен быть числом большим, либо равным нулю'}, status=status.HTTP_400_BAD_REQUEST)

