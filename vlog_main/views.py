from django.shortcuts import render
from blogs.models import Category, Blog

from assignments.models import About


def home(request):
    
    featured_posts= Blog.objects.filter(is_featured=True, status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status = 'Published')
    # print(posts)
    # print(featured_posts)

    # fetch About Us information
    try:
        about=About.objects.get() # to fetch only one detail from about model i used get()


    except:
        about = None    
    context={
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
        }
    return render(request,'home.html', context)