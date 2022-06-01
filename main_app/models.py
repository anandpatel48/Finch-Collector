from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharFielf(max_length = 100)
    img = models.CharField(max_length = 300)
    bio = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']