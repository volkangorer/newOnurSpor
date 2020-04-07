from django.contrib import admin

from .models import Database,Galeri,Duyuru,Haber

# Register your models here.

admin.site.register(Galeri) 
admin.site.register(Haber) 
admin.site.register(Duyuru)