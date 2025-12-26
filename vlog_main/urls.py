
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
    path('blogs/<slug:slug>/', blogsviews.blogs, name='blogs'),
    #search endpoint
    path('blogs/search/',blogsviews.search, name='search'),
    # Registration and Login URLs
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
