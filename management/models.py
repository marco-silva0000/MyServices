# -*- coding: UTF-8 -*-
# from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate = models.CharField(max_length=50, blank=True, null=True)
    drivers = models.ManyToManyField(User)
    image = models.ImageField()

    # @python_2_unicode_compatible
    def __str__(self):
        return u'%s %s' % (self.brand, self.model)


class FuelCharge(models.Model):
    GAS95 = "GAS95"
    GAS98 = "GAS98"
    GAS95P = "GAS95P"
    GAS98P = "GAS98P"
    DIESEL = "DIESEL"
    DIESELP = "DIESELP"
    GPL = "GPL"

    FUELTYPES = (
        (GAS95, "Gasolina 95"),
        (GAS98, "Gasolina 98"),
        (GAS95P, "Gasolina 95+"),
        (GAS98P, "Gasolina 9p+"),
        (DIESEL, "Diesel"),
        (DIESELP, "Diesel+"),
        (GPL, "GPL"),
    )

    date = models.DateTimeField(default=timezone.now)
    price = models.FloatField()
    quantity = models.FloatField()
    brand = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(choices=FUELTYPES, max_length=50, null=True, blank=True)
    car = models.ForeignKey(Car)
    kms = models.DecimalField(decimal_places=0, max_digits=10)

    # @python_2_unicode_compatible
    def __str__(self):
        return u"%0.3f€ on %s. %0.3fL at %0.3f€/L" % (self.price * self.quantity, self.date, self.quantity, self.price)
