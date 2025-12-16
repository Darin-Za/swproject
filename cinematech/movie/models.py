from django.db import models

# Movie Table
class Movie(models.Model):
    id = models.AutoField(primary_key=True)    
    title = models.CharField(max_length=200)
    release_year = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    rating = models.FloatField(null=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)


    def __str__(self):
        return self.title