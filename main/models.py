from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    tags = models.ManyToManyField(Tag, related_name="posts")
    text = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.author.name}: {self.title}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return f'{self.author.name} - {self.text}'
