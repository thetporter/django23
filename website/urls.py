from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),


    path('logout/', logoutUser, name='logoutUser'),
    path('register/', register, name='register'),
    path('login/', loginUser, name='loginUser'),

    path('account/', account, name='account'),
    path('account/create-blog/', createBlog, name='createBlog'),
    path('account/<int:blog_pk>/delete', deleteBlog, name='deleteBlog'),
    path('account/<int:blog_pk>/red', changeBlog, name='changeBlog'),

    path('blog/', include('main.urls')),
    path('blog/', blog, name='blog'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)