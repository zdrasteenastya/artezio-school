# -*- coding: utf-8 -*-

from django.db import models


class Junior(models.Model):
    username = models.CharField(max_length=200, verbose_name=u"ФИО")
    phone_number = models.CharField(max_length=12, verbose_name=u"Номер телефона")
    email = models.CharField(max_length=50, verbose_name=u"E-mail")
    link_sns = models.CharField(max_length=200, verbose_name=u"Ссылка на профиль в соц сетях")
    education = models.CharField(max_length=200, verbose_name=u"Образование")
    english = models.CharField(max_length=200, verbose_name=u"Уровень английского языка")
    languages = models.TextField(verbose_name=u"Языки программирования")
    experience = models.TextField(verbose_name=u"опыт ")
    link_code = models.TextField(verbose_name=u"Ссылка на ваш публичный репозиторий")
    agreement = models.BooleanField(default=False, verbose_name=u"Cогласен на обработку персональных данных")
    file = models.FileField(upload_to='user_files/', verbose_name=u"Файл")

    def __str__(self):
        return self.username.encode('utf-8')