from django.db import models
from django.contrib.auth.models import AbstractUser

class register(AbstractUser):
    choices=(['Creator', 'Creator'],['Viewer', 'Viewer'])
    reg_type=models.CharField(max_length=10,choices=choices)
    email = models.EmailField(max_length=255)
    phno=models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    pass
    def __str__(self):
        return self.username

class blogs(models.Model):
    author_id = models.ForeignKey(register, on_delete=models.CASCADE)
    author_name=models.CharField(max_length=100, default='none')
    title = models.CharField(max_length=100)
    image=models.ImageField(null=True, upload_to='img/')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
