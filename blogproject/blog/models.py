from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=175)
    content = models.TextField()
    author_name = models.CharField(max_length=125, blank=True, null =True)
    published = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author_name}"
    

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=125)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"
    