# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from training1.models import Service1, Log


@admin.register(Service1)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('input1', 'input2', 'input3', 'input4', 'input5')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('action_code', 'application_code', 'user', 'alt_module_name', 'input_detail', 'output_detail')


admin.autodiscover()
