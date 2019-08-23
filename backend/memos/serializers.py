# posts/serializers.py
from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    # memo = MemoSerializer()

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'memo',
        )
        # fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    # memo = MemoSerializer()

    class Meta:
        model = models.Like
        fields = '__all__'


class MemoSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True)
    # likes = LikeSerializer(many=True)

    class Meta:
        model = models.Memo
        fields = (
            'id',
            'title',
            'content',
            'comments',
            'likes',
        )

