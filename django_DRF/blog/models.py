from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    vlog_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    commnet = models.CharField(max_length=255,null=True, default="No comment")

    def __str__(self):
        return f'Comment on {self.commnet}'