import json

from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from rest_framework import viewsets, pagination
from blog.serializers import BlogListSerializer, UserSerializer
from blog.models import bloglist
# Create your views here.


def index(request):
    blog_list = bloglist.objects.order_by('-pub_date')
    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page', 1)
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'blog_list': blog_list})

'''
class BlogListView(ListView):
    model = bloglist
    paginate_by = 5
    context_object_name = 'blog_list'
    template_name = 'blog/index.html'
'''

def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def post(request, post_id):
    blogpost = get_object_or_404(bloglist, pk=post_id)
    return render(request, 'blog/post.html', {'blog_post': blogpost})


class BlogListViewSet(viewsets.ModelViewSet):
    queryset = bloglist.objects.all().order_by('-pub_date')
    serializer_class = BlogListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

