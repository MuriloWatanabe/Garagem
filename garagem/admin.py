from django.contrib import admin

from .models import Marcas
from .models import Categoria

admin.site.register(Marcas)
admin.site.register(Categoria)
