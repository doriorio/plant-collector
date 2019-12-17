from django.contrib import admin

# Register your models here.
from .models import Plant, Use, Pollinator


admin.site.register(Plant)
admin.site.register(Use)
admin.site.register(Pollinator)