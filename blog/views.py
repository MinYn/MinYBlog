from django.shortcuts import get_object_or_404, render
from blog.models import bloglist
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def index(request):

    blog_list = bloglist.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'blog_list': blog_list,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def post(request, post_id):
    blogpost = get_object_or_404(bloglist, pk=post_id)
    return render(request, 'blog/post.html', {'blog_post': blogpost})
