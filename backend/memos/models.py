from django.db import models

# Create your models here.

from django.db import models

class Memo(models.Model):
    # userId = models.IntegerField(blank=True, null=True)
    userId = models.CharField(max_length=50, default='anonymous')
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title