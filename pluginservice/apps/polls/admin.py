from django.contrib import admin
from .models import Poll, PollAnswer, PollAnswer


class PollAnswerAdmin(admin.TabularInline):
    extra = 1
    model = PollAnswer

class PollAnswerAdmin(admin.TabularInline):
    extra = 1
    model = PollAnswer


class PollAdmin(admin.ModelAdmin):
    inlines = [PollAnswerAdmin, PollAnswerAdmin]

admin.site.register(Poll, PollAdmin)
