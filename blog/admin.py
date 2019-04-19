from django.contrib import admin
from blog.models import bloglist
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(bloglist)
class BlogEditorAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
class BlogListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'subject', 'pub_date']
    list_display_links = ['id', 'title']
    list_per_page = 5
    list_filter = ['pub_date']

#admin.site.register(bloglist, BlogAdmin)