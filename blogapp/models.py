from email.mime import image
from email.policy import default
from logging.handlers import SYSLOG_UDP_PORT
from optparse import Option
from time import timezone
from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    image = models.ImageField(default='upload')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') 
    content = models.TextField()
    status = models.CharField(max_length=10, choices= options, default='draft')
    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager

    def get_absolute_url(self):
        return reverse('blog:post_single',args=[self.slug])

    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title