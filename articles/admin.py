from django.contrib import admin
from .models import Content,Metadata
from django.db.utils import ProgrammingError
import logging

admin.site.register(Metadata)



# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    date_hierarchy = 'article_date'
    list_display = ('article_title', 'article_date','article_author')
    prepopulated_fields = {"slug": ("article_title",)}
    #list_display_links = ('')
    #list_editable = ('article_title','article_author','article_author')
    class Meta:
        model = Content

try:
	admin.site.register(Content, ContentAdmin)
except ProgrammingError as e:
    logger.warning('Some migrations are not applied!')
