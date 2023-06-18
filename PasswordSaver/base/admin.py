from django.contrib import admin

# Register your models here.

from .models import User,WebAppPassword,CardPassword

admin.site.register(User)
admin.site.register(WebAppPassword)
admin.site.register(CardPassword)


