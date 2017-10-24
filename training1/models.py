# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.conf import settings
from django.db import models

# Create your models here.


IS_BANKASI_CODE = 0
YAPI_KREDI_BANKASI_CODE = 1
ZIRAAT_BANKASI_CODE = 2
MEMBERS = (
    (IS_BANKASI_CODE, "IS BANKASI"),
    (YAPI_KREDI_BANKASI_CODE, "YAPI KREDI BANKASI"),
    (ZIRAAT_BANKASI_CODE, "ZIRAAT BANKASI"),
)

HIZMET_LISTELEME_CODE = 0
HIZMET_EKLEME_CODE = 1
HIZMET_SILME_CODE = 2

alt_module_names = (
    (HIZMET_LISTELEME_CODE, "Hizmet Listeleme"),
    (HIZMET_EKLEME_CODE, "Hizmet Ekleme"),
    (HIZMET_SILME_CODE, "Hizmet Silme"),
)

choices = (
    (0, "Choice 1"),
    (1, "Choice 2"),
    (2, "Choice 3"),
)


class Service1(models.Model):
    input1 = models.CharField(max_length=50)
    input2 = models.CharField(max_length=50)
    input3 = models.IntegerField(choices=choices)
    input4 = models.FloatField()
    input5 = models.IntegerField()


class Log(models.Model):
    action_code = models.UUIDField("islem kodu", default=uuid.uuid4)
    application_code = models.BigIntegerField(editable=False, default=510)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    alt_module_name = models.CharField(max_length=50, choices=alt_module_names)
    input_detail = models.TextField(max_length=20000)
    output_detail = models.TextField(max_length=20000)
