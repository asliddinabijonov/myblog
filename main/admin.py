from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', )
    list_editable = ('title', )

@admin.register(Talks)
class TalksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', )
    list_editable = ('title', )