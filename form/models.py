from django.db import models

# Create your models here.


# paste in your models.py


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    project_id = models.IntegerField()

    def __str__(self):
        return self.title
