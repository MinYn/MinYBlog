"""MinYBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from blog import views as main_view

router = routers.DefaultRouter()
router.register(r'users', main_view.UserViewSet)
router.register(r'blog', main_view.BlogListViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_view.index),
    url(r'^about/', main_view.about),
    url(r'^contact/', main_view.contact),
    url(r'^post/(?P<post_id>\d+)/$', main_view.post),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)