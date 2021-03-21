from django.contrib import admin
from .models import Board, Comment

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Board, BoardAdmin)  #admin에 게시판 등록
admin.site.register(Comment)