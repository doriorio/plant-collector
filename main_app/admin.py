from django.contrib import admin

# Register your models here.
from .models import Plant, Use


admin.site.register(Plant)
admin.site.register(Use)