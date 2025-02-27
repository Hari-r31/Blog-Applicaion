from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name='base'),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('user/<str:username>/', user_blogs, name='user_blogs'),
    path('popular/', popular, name='popular'),
    path('search/', search, name='search'),
    # path('search/', views.search_results, name='search_results'),
    path('', include('myapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)