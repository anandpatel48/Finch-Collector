from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length = 100)
    img = models.CharField(max_length = 300)
    bio = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Game(models.Model):
    opponent = models.CharField(max_length = 150)
    date = models.CharField(max_length = 30)
    points = models.IntegerField()
    finch = models.ForeignKey(Finch, on_delete = models.CASCADE, related_name="games")

    def __str__(self):
        return self.date
