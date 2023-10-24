from django.contrib import admin
from .models import Entidad
from .models import User
from .models import Comunicado
from .models import TIPO_CHOICES

# Register your models here.

admin.site.register(Entidad)
admin.site.register(User)
admin.site.register(Comunicado)