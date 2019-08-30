from django.db import models

# Create your models here.

from django.db import models
# from django.contrib.auth.models import AbstractUser
# from users import models as user_models50)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Memo(TimeStampedModel):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def get_title_content(self):
        return self.username + ' has title : ' + self.title + ', and content : ' + self.content

    def __str__(self):
        return '{} : {} : {}'.format(self.username, self.title, self.content)
        # return self.title + "  -  " + self.content


class Comment(TimeStampedModel):
    message = models.TextField()
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE, null=True, related_name='comments')

    def get_message(self):
        return 'memo (title:' + self.memo.title + ') has comment : ' + self.message

    def __str__(self):
        return self.message


class Like(TimeStampedModel):
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE, null=True, related_name='likes')

    def get_memo(self):
        return 'memo title: ' + self.memo.title

    def __str__(self):
        return 'Memo Caption: {}'.format(self.memo.content)
