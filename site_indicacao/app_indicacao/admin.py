from django.contrib import admin

# Register your models here.

from django.contrib import admin
from app_indicacao.models import Cupom, Leads

class ListaCupon(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cupom')
    list_display_links = ('id','nome')
    search_fields = ('nome','cupom')

admin.site.register(Cupom, ListaCupon)

class ListaLead(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cupom')
    list_display_links = ('id','nome')
    search_fields = ('nome','cupom')

admin.site.register(Leads,ListaLead)
