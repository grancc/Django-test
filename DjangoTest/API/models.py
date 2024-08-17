from django.db import models


FUEL_CHOICES = (
    ('бензин', 'бензин'),
    ('дизель', 'дизель'),
    ('гибрид', 'гибрид'),
    ('электричество', 'электричество'),
)

TRANSMISSION_CHOICES = (
    ('механическая', 'механическая'),
    ('автоматическая', 'автоматическая'),
    ('робот', 'робот'),
    ('вариатор', 'вариатор'),
)


class Cars(models.Model):

    brand = models.CharField(max_length=100, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    fuel_type = models.CharField(
        max_length=100, choices=FUEL_CHOICES, verbose_name="Тип топлива")
    transmission_type = models.CharField(
        max_length=100, choices=TRANSMISSION_CHOICES, verbose_name="Тип коробки передач")
    mileage = models.IntegerField(verbose_name="Пробег")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.brand} {self.model}"
