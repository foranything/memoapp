# posts/serializers.py
from rest_framework import serializers
from . import models


# `serializer` 클래스를 만들고 그 안에 Meta 클래스를 만듭니다.
class MemoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('userId', 'id', 'title', 'content','created_at', 'updated_at')
        model = models.Memo
