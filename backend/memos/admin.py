from django.contrib import admin

# Register your models here.

from django.contrib import admin
from . import models
# from . models import Memo
#
# admin.site.register(Memo)


@admin.register(models.Memo)
class MemoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass