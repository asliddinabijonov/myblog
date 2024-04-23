from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    text = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs"


class Talks(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Talk"
