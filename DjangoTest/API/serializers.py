from rest_framework import serializers
from .models import Cars
from .models import FUEL_CHOICES, TRANSMISSION_CHOICES


class CarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = ['brand', 'model', 'year', 'fuel_type', 'transmission_type', 'mileage', 'price']
        extra_kwargs = {
            'fuel_type': {
                'error_messages': {
                    'invalid_choice': 'Выберите из списка: "бензин", "дизель", "гибрид", "электричество"',
                    'required': 'Тип топлива является обязательным полем'
                }
            },
            'transmission_type': {
                'error_messages': {
                    'invalid_choice': 'Выберите из списка: "механическая", "автоматическая", "робот", "вариатор"',
                    'required': 'Тип коробки пеередач является обязательным полем'
                }
            },
            'model': {
                'error_messages': {
                    'invalid_choice': 'поле не может быть пустым',
                    'required': 'поле не может быть пустым'
                }
            },
            'brand': {
                'error_messages': {
                    'invalid_choice': 'поле не может быть пустым',
                    'required': 'поле не может быть пустым'
                }
            },
            'mileage': {
                'error_messages': {
                    'invalid_choice': 'поле не может быть пустым',
                    'required': 'поле не может быть пустым'
                }
            },
            'price': {
                'error_messages': {
                    'invalid_choice': 'поле не может быть пустым',
                    'required': 'поле не может быть пустым'
                }
            }
        }

    