from django.db import models


class Coffee(models.Model):
    name = models.CharField("Название кофе", max_length=20)
    value = models.CharField("Объем", max_length=5)
    cost = models.IntegerField("Цена", default=100)

    def __str__(self):
        return self.name + ', ' + self.value + ' литра, стоимость: ' + str(self.cost) + ' рублей'

    class Meta:
        verbose_name = "Кофе"


class Shop(models.Model):
    name = models.CharField("Название торговой точки", unique=True, max_length=30)
    location = models.CharField("Адрес торговой точки", max_length=150)

    def __str__(self):
        return self.name + ', адрес: ' + self.location

    class Meta:
        verbose_name = "Точка"
        verbose_name_plural = "Точки"


class Order(models.Model):
    STATE = (
        (1, 'Исполняется'),
        (2, 'Готов'),
    )
    status = models.IntegerField("Статус заказа", default=1, choices=STATE)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, verbose_name='Выберите напиток', default=None)
    client_name = models.CharField("Как в Вам обращаться?", max_length=20, default=None)
    number_phone = models.CharField("Введите номер телефона", max_length=20, default=None)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Откуда заберете", default=None)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
