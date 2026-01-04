from django.shortcuts import render , redirect,get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from .models import Blog, Category , Comment
from django.db.models import Q
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


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug,  status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment= request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)# this will redirect you to the page where you came from

    #comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()



    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword =request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    # i contains is used to search for a keyword in a case insensitive manner
    context={
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html' , context)    