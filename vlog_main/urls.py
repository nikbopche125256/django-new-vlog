
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.http import HttpResponse
from blogs import views as blogsviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/',include('blogs.urls')),
    path('<slug:slug>/', blogsviews.blogs, name='blogs'),

    #search endpoint
    path('blogs/search/',blogsviews.search, name='search'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
