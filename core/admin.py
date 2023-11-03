from django.contrib import admin
from core.models import Units, PayData, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Units)
admin.site.register(PayData)
