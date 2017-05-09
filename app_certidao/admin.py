from django.contrib import admin
from app_certidao.models import *


class TipoPessoa(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register (Pessoa, TipoPessoa)