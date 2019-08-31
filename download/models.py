from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=30)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='books/pdf')

    def __str__(self):
        return self.title

class Music(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    song = models.FileField(upload_to='music/mp3')
    

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=30)
    clip = models.FileField(upload_to='video')

    def __str__(self):
        return self.title