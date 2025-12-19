from django.shortcuts import render , redirect,get_object_or_404
from django.http import HttpResponse
from .models import Blog, Category

# Create your views here.


def posts_by_category(request, category_id):
    # fetch the posts that belongs to the category with id=category_id
    posts=Blog.objects.filter(status='Published', category_id=category_id)
    # use try/except when yu want to do some custom actions if the category does not exist 

    # try:
    #     category = Category.objects.get(id=category_id)
    # except:
    #     # redirect user to home page if category not found
    #     return redirect('home')

    # use get_objext_or_404 when you want show 4040 error page

    category = get_object_or_404(Category, id=category_id)

    context={
        'posts':posts,
        'category': category.category_name,
    }
    return render(request, 'posts_by_category.html', context)
    