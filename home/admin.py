from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,RescueComplaint,Feedback_Note

# Register your models here.
UserAdmin.fieldsets += ('Custom fields set', {'fields': ('email_number', 'rescue','shelter','age')}),
admin.site.register(User, UserAdmin)
admin.site.register(RescueComplaint)
admin.site.register(Feedback_Note)