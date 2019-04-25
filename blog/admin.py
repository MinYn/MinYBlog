from django.contrib import admin
from blog.models import bloglist
from django_summernote.admin import SummernoteModelAdmin


@admin.register(bloglist)
class BlogListAdmin(SummernoteModelAdmin):
    list_display = ['id', 'Title', 'SubTitle', 'pub_date']
    list_display_links = ['id', 'Title']
    list_per_page = 5
    list_filter = ['pub_date']
    search_fields = (
        'Title', 'SubTitle', 'Subject'
    )
    summernote_fields = '__all__'