from django.contrib import admin
from .models import *

admin.site.register(Todo)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Daily)
admin.site.register(Priority)
admin.site.register(User)
admin.site.register(Status)