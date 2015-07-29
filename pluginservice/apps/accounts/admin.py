from django.contrib import admin
from .models import UserProfile, EmailNotification

admin.site.register(UserProfile)
admin.site.register(EmailNotification)
