from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    url = models.URLField(blank=True, default='')

    def __str__(self):
        return "Title: {} Status: {}".format(self.title, self.completed)
