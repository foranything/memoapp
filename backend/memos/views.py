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
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, memo_id, format=None):
        msg = request.data['message']
        print('Memo_id: ' + str(memo_id) + ' , Comment: ' + str(msg))
        found_memo = models.Memo.objects.filter(id=memo_id)
        if not found_memo:
            return Response(status=status.HTTP_404_NOT_FOUND)

        new_comment = models.Comment.objects.create(
            message=msg,
            memo=found_memo[0]
        )
        new_comment.save()
        all_comments = models.Comment.objects.filter(memo=memo_id)
        serializer = serializers.CommentSerializer(all_comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentDelete(APIView):
    def get(self, request, memo_id, comment_id, format=None):
        print('get comments: ' + str(comment_id) + ' from memo id: '+ str(memo_id))
        target_comment = models.Comment.objects.filter(memo=memo_id, id=comment_id)
        if not target_comment:
            print('empty')
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.CommentSerializer(target_comment, many=True)
        return Response(data=serializer.data,  status=status.HTTP_200_OK)

    def delete(self, request, memo_id, comment_id, format=None):
        print('get comments: ' + str(comment_id) + ' from memo id: '+ str(memo_id))
        target_comment = models.Comment.objects.filter(memo=memo_id, id=comment_id)
        if not target_comment:
            print('empty')
            return Response(status=status.HTTP_404_NOT_FOUND)
        target_comment.delete()
        all_comments = models.Comment.objects.filter(memo=memo_id)
        serializer = serializers.CommentSerializer(all_comments, many=True)
        return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)


class LikeList(APIView):
    def get(self, request, memo_id, format=None):
        print(memo_id)
        all_likes = models.Like.objects.filter(memo=memo_id)
        serializer = serializers.LikeSerializer(all_likes, many=True)
        return Response(data=serializer.data)

    def post(self, request, memo_id, format=None):
        print('Like:' + str(memo_id))
        try:
            found_memo = models.Memo.objects.get(id=memo_id)
        except models.Memo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        new_like = models.Like.objects.create(
            memo=found_memo
        )
        new_like.save()
        all_likes = models.Like.objects.filter(memo=memo_id)
        serializer = serializers.LikeSerializer(all_likes, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete(self, request, memo_id, format=None):
        print('Unlike:' + str(memo_id))

        try:
            preexisting_like = models.Like.objects.filter(
                memo=memo_id
            ).order_by('id').first()
            preexisting_like.delete()
            all_likes = models.Like.objects.filter(memo=memo_id)
            serializer = serializers.LikeSerializer(all_likes, many=True)
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


# class LikeMemo(APIView):
#     def post(self, request, memo_id, format=None):
#         print('Like:' + str(memo_id))
#         try:
#             found_memo = models.Memo.objects.get(id=memo_id)
#         except models.Memo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         new_like = models.Like.objects.create(
#             memo=found_memo
#         )
#         new_like.save()
#         return Response(status=status.HTTP_200_OK)
#
#
# class UnlikeMemo(APIView):
#     def delete(self, request, memo_id, format=None):
#         print('Unlike:' + str(memo_id))
#         try:
#             found_memo = models.Memo.objects.get(id=memo_id)
#         except models.Memo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         try:
#             preexisting_like = models.Like.objects.filter(
#                 memo=found_memo
#             ).order_by('id').first()
#             preexisting_like.delete()
#             return Response(status=status.HTTP_202_ACCEPTED)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)



# class MemoList(generics.ListAPIView):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer


# class MemoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer

# class MemoDetail(models.Model):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer