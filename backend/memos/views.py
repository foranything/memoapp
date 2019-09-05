from rest_framework.views import APIView
from . import models, serializers
from rest_framework.response import Response
from rest_framework import status


class MemoList(APIView):
    def get(self, request, format=None):
        all_memos = models.Memo.objects.all().order_by('-updated_at')
        serializer = serializers.MemoSerializer(all_memos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        password = request.data['password']
        title = request.data['title']
        content = request.data['content']
        new_memo = models.Memo.objects.create(
            password=password,
            title=title,
            content=content,
        )
        new_memo.save()
        filtered_memos = models.Memo.objects.filter(
            password=password,
            title=title,
            content=content).order_by('-updated_at')
        serializer = serializers.MemoSerializer(filtered_memos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MemoDetail(APIView):
    def get(self, request, memo_id, format=None):
        target_memo = models.Memo.objects.filter(id=memo_id).order_by('-updated_at')
        if not target_memo:
            print('empty')
            return Response(status=status.HTTP_404_NOT_FOUND)
        filtered_memos = models.Memo.objects.filter(id=memo_id).order_by('-updated_at')
        serializer = serializers.MemoSerializer(filtered_memos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, memo_id, format=None):
        title = request.data['title']
        content = request.data['content']
        target_memo = models.Memo.objects.filter(id=memo_id).order_by('-updated_at')
        if not target_memo:
            print('empty')
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        else:
            target_memo[0].id = memo_id
            target_memo[0].title = title
            target_memo[0].content = content
            target_memo[0].save()
        filtered_memos = models.Memo.objects.filter(id=memo_id).order_by('-updated_at')
        serializer = serializers.MemoSerializer(filtered_memos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, memo_id, format=None):
        target_memo = models.Memo.objects.filter(id=memo_id)
        if not target_memo:
            print('empty')
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        target_memo.delete()
        filtered_memos = models.Memo.objects.filter(id=memo_id).order_by('-updated_at')
        serializer = serializers.MemoSerializer(filtered_memos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentList(APIView):
    def get(self, request, memo_id, format=None):
        target_memo = models.Memo.objects.filter(id=memo_id)
        if not target_memo:
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        filtered_comments = models.Comment.objects.filter(memo=memo_id).order_by('-updated_at')
        serializer = serializers.CommentSerializer(filtered_comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, memo_id, format=None):
        message = request.data['message']
        target_memo = models.Memo.objects.filter(id=memo_id)
        if not target_memo:
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        new_comment = models.Comment.objects.create(
            message=message,
            memo=target_memo[0],
        )
        new_comment.save()
        filtered_comments = models.Comment.objects.filter(message=message, memo=memo_id).order_by('-updated_at')
        serializer = serializers.CommentSerializer(filtered_comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentDetail(APIView):
    def get(self, request, memo_id, comment_id, format=None):
        target_memo = models.Memo.objects.filter(id=memo_id)
        if not target_memo:
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        target_comment = models.Comment.objects.filter(memo=memo_id, id=comment_id).order_by('-updated_at')
        if not target_comment:
            print('empty')
            return Response(data="comment not found",status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.CommentSerializer(target_comment, many=True)
        return Response(data=serializer.data,  status=status.HTTP_200_OK)

    def put(self, request, memo_id, comment_id, format=None):
        message = request.data['message']
        target_memo = models.Memo.objects.filter(id=memo_id)
        if not target_memo:
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        target_comment = models.Comment.objects.filter(memo=memo_id, id=comment_id).order_by('-updated_at')
        if not target_comment:
            print('empty')
            return Response(data="comment not found", status=status.HTTP_404_NOT_FOUND)
        else:
            target_comment[0].id = comment_id
            target_comment[0].message = message
            target_comment[0].save()
        target_comment = models.Comment.objects.filter(memo=memo_id, id=comment_id).order_by('-updated_at')
        serializer = serializers.CommentSerializer(target_comment, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, memo_id, comment_id, format=None):
        print('get comments: ' + str(comment_id) + ' from memo id: '+ str(memo_id))
        target_comment = models.Comment.objects.filter(memo=memo_id, id=comment_id)
        if not target_comment:
            print('empty')
            return Response(status=status.HTTP_404_NOT_FOUND)
        target_comment.delete()
        filtered_comments = models.Comment.objects.filter(memo=memo_id, id=comment_id).order_by('-updated_at')
        serializer = serializers.CommentSerializer(filtered_comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LikeList(APIView):
    def get(self, request, memo_id, format=None):
        filtered_likes = models.Like.objects.filter(memo=memo_id).order_by("-updated_at")
        serializer = serializers.LikeSerializer(filtered_likes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, memo_id, format=None):
        target_memo = models.Memo.objects.filter(id=memo_id)
        if not target_memo:
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        new_like = models.Like.objects.create(
            memo=target_memo[0],
        )
        new_like.save()
        filtered_likes = models.Like.objects.filter(memo=memo_id).order_by('-updated_at')
        serializer = serializers.LikeSerializer(filtered_likes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, memo_id, format=None):
        target_memo = models.Memo.objects.filter(id=memo_id)
        if not target_memo:
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        target_like = models.Like.objects.filter(memo=memo_id).order_by('updated_at')
        if not target_like:
            print('empty')
            return Response(status=status.HTTP_404_NOT_FOUND)
        target_like[0].delete()
        filtered_likes = models.Like.objects.filter(memo=memo_id).order_by('-updated_at')
        serializer = serializers.LikeSerializer(filtered_likes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LikeDetail(APIView):
    def get(self, request, memo_id, like_id, format=None):
        target_memo = models.Memo.objects.filter(id=memo_id)
        if not target_memo:
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        filtered_likes = models.Like.objects.filter(memo=memo_id, id=like_id).order_by('-updated_at')
        serializer = serializers.LikeSerializer(filtered_likes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, memo_id, like_id, format=None):
    #     target_memo = models.Memo.objects.filter(id=memo_id)
    #     if not target_memo:
    #         return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
    #     target_like = models.Like.objects.filter(memo=memo_id, id=like_id).order_by('-updated_at')
    #     if not target_like:
    #         print('empty')
    #         return Response(data="like not found", status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         target_like[0].save()
    #     target_like = models.Like.objects.filter(memo=memo_id, id=like_id).order_by('-updated_at')
    #     serializer = serializers.LikeSerializer(target_like, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, memo_id, like_id, format=None):
        target_memo = models.Memo.objects.filter(id=memo_id)
        if not target_memo:
            return Response(data="memo not found", status=status.HTTP_404_NOT_FOUND)
        target_like = models.Like.objects.filter(memo=memo_id, id=like_id).order_by('updated_at')
        if not target_like:
            print('empty')
            return Response(status=status.HTTP_404_NOT_FOUND)
        target_like.delete()
        filtered_likes = models.Like.objects.filter(memo=memo_id, id=like_id).order_by('-updated_at')
        serializer = serializers.LikeSerializer(filtered_likes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
