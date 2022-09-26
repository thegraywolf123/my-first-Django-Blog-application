from xml.dom.minidom import Document
from django.urls import path
from .import views
from blogproject.settings import DEBUG, STATIC_URL, STATICFILES_DIR, MEDIA_URL,MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [
    
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.post_single, name='post_single'),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATICFILES_DIR)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT )