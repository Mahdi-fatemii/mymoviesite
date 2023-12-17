from django.db import models

# Create your models here.


class MovieData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    genres = models.CharField(max_length=300, default='unspecified')
    duration = models.FloatField()
    rating = models.FloatField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='Images/', default="Images/None/NoImg.jpg")


