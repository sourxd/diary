from django.contrib import admin
from users.models import User, Notes

admin.site.register(User)
admin.site.register(Notes)