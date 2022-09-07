from django.contrib import admin
from .models import testing

# Register your models here.

class texts(admin.ModelAdmin):
 list_display = ('id', 'text')

admin.site.register(testing, texts)