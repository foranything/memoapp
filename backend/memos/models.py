from django.db import models

# Create your models here.

from django.db import models
# from users import models as user_models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Memo(TimeStampedModel):
    # creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.title, self.content)
        # return self.title + "  -  " + self.content


class Comment(TimeStampedModel):
    # creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    message = models.TextField()
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return self.message


class Like(TimeStampedModel):
    # creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE, null=True, related_name='likes')

    def __str__(self):
        return 'Memo Caption: {}'.format(self.memo.content)
