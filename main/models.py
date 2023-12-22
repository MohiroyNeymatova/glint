from django.db import models

# Create your models here.


class BannerImage(models.Model):
    photo = models.ImageField(upload_to='banners/')


class Banner(models.Model):
    image = models.ManyToManyField(BannerImage)
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name


class AboutFeatures(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to='abouts/')
    text = models.CharField(max_length=500)
    features = models.ManyToManyField(AboutFeatures)
    video_url = models.URLField()


class Team(models.Model):
    photo = models.ImageField(upload_to='photos/')
    name = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    text = models.TextField()
    fb = models.URLField()
    tw = models.URLField()
    inst = models.URLField()
    github = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name


class Project(models.Model):
    photo = models.ImageField(upload_to='projects/')
    is_left = models.BooleanField(default=False)
    name = models.CharField(max_length=250)
    description = models.TextField()
    url = models.URLField()
    author_words = models.TextField()
    author = models.CharField(max_length=250)
    author_photo = models.ImageField(upload_to='authors/')

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='reviews/')
    name = models.CharField(max_length=250)
    job = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class StudioGallery(models.Model):
    photo = models.ImageField(upload_to='studio/')


class Info(models.Model):
    about = models.TextField()
    fb = models.URLField()
    tw = models.URLField()
    inst = models.URLField()
    linkedin = models.URLField()
    logo = models.ImageField(upload_to='logos/')


class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name


class Subscriber(models.Model):
    first_name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.email