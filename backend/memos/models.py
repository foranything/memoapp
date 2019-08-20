from django.db import models

# Create your models here.

from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Memo(TimeStampedModel):
    userId = models.CharField(max_length=50, default='anonymous')
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title + "  -  " + self.content
