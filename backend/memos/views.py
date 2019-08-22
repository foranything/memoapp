# from django.shortcuts import render
# from . import models

# Create your views here.
# posts/views.py
# from rest_framework import generics
# from .models import Memo
# from .serializers import MemoSerializer
from rest_framework.views import APIView
from . import models, serializers
from rest_framework.response import Response
from rest_framework import status


class MemoList(APIView):
    def get(self, request, format=None):

        all_memos = models.Memo.objects.all()

        serializer = serializers.MemoSerializer(all_memos, many=True)

        return Response(data=serializer.data)


class CommentList(APIView):
    def get(self, request, memo_id, format=None):
        print(memo_id)

        all_comments = models.Comment.objects.filter(memo=memo_id)

        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serializer.data)


class LikeList(APIView):
    def get(self, request, memo_id, format=None):
        print(memo_id)

        all_likes = models.Like.objects.filter(memo=memo_id)

        serializer = serializers.LikeSerializer(all_likes, many=True)

        return Response(data=serializer.data)


class LikeMemo(APIView):
    def post(self, request, memo_id, format=None):
        print('Like:' + str(memo_id))
        try:
            found_memo = models.Memo.objects.get(id=memo_id)
            # serializer = serializers.MemoSerializer(found_memo, many=True)
        except models.Memo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # for element in found_memo:
        # print(found_memo[0])
        # print(found_memo)

        new_like = models.Like.objects.create(
            memo=found_memo
        )
        new_like.save()

        return Response(status=200)


class UnlikeMemo(APIView):
    def post(self, request, memo_id, format=None):
        print('Unlike:' + str(memo_id))

        return Response(status=200)




# class MemoList(generics.ListAPIView):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer


# class MemoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer

# class MemoDetail(models.Model):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer