from django.db import models

# Create your models here.



class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address =models.EmailField(max_length=100, null=False)

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    tag_name=models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.tag_name}"

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    author=models.ForeignKey(Author, on_delete=models.SET_NULL,related_name='post', null=True)
    tags=models.ManyToManyField(Tag, related_name='post')
    excerpt=models.TextField()
    image_name=models.CharField(max_length=100, null=True, blank=True)
    # date automatically updated when post is updated
    date = models.DateTimeField(auto_now=True)
    content=models.TextField()
    slug=models.SlugField(max_length=100,unique=True,blank=True,db_index=True)

    def __str__(self):
        return f"{self.title} - {self.date}"