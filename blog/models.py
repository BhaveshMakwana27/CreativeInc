from django.db import models

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.CharField(max_length=50)
    timeStamp = models.DateTimeField()

    def __str__(self):
        return self.title + ' by ' + self.author
    
