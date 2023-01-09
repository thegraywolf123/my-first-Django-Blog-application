from django.urls import path, include
# from .views import index, home_api, post_single
from .import views
from blogproject.settings import DEBUG, STATIC_URL, STATICFILES_DIR, MEDIA_URL,MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [
    
    path('', views.index, name ='index'),
    path('home/', views.home,name = 'home'),
    path('<slug:post>/', views.post_single, name ='post_single'),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATICFILES_DIR)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT )