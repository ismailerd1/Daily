from django.db import models

# Create your models here.



class Topic(models.Model):
# Konu başlığı adı
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class News (models.Model):
    sender = models.CharField(max_length=50)
    source = models.CharField(max_length=80)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    title = models.CharField(max_length=125)
    content = models.TextField()
    topics = models.ManyToManyField(Topic, related_name='news')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Feedbacks (models.Model):
    sender = models.CharField(max_length=50)
    title = models.CharField(max_length=125)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    



