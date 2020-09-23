from django.conf import settings
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    lastname = models.CharField(max_length=255, verbose_name="Фамилия")
    middlename = models.CharField(max_length=255, verbose_name="Отчество")  
    description = models.CharField(max_length=255, verbose_name="Описание")   
    dob = models.DateField(max_length=8)
    mobile = models.CharField(max_length=255, verbose_name="Мобильный номер", null=True, blank=True)
    work = models.CharField(max_length=255, verbose_name="Рабочий номер", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    socials = models.CharField(max_length=255, verbose_name="Соц. Сети") 
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.name