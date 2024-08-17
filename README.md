# Тестовое задние для Djnago

Endpoints:
1. Добавление автомобиля:
     POST /api/cars/ 

   Response:
    { "brand": "Toyota", "model": "Camry", "year": 2020, "fuel_type": "бензин", "transmission_type": "автоматическая", "mileage": 50000, "price": 25000 }
   
      * brand - марка автомобиля (строка, числа возможны, обязательное поле)
      * model - модель автомобиля (строка, числа возможны, обязательное поле)
      * year - год выпуска (целое число, больше нуля, обязательное поле)
      * fuel_type - тип топлива (бензин, дизель, электричество, гибрид)
      * transmission_type - тип КПП (механическая, автоматическая, вариатор, робот)
      * mileage - пробег (целое число, больше либо равно нулю, обязательное поле)
      * price - цена (целое число, больше нуля, обязательное поле)

3. Получение списка автомобилей по фильтрам:

   GET /api/cars/?brand=Toyota&model=Camry&year=2020&fuel_type=бензин&transmission=автоматическая&mileage_min=40000&mileage_max=60000&price_min=20000&price_max=30000
  
  
    возможные фильтры:
      * brand
      * model
      * year
      * year_from (с года)
      * year_to (по год)
      * mileage
      * mileage_min (пробег с)
      * mileage_max (пробег по)
      * price
      * price_min (цена с)
      * price_max (цена по)
      * page (пагинация, страница с которой выводить, по умолчанию - 1)
      * onPageCount (пагинация, количество на одной странице, по умолчанию - 3)
    


4. Получение деталей конкретного автомобиля по ID.
   
    GET /api/cars/{CAR_ID}/
   

   
