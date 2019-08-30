from django.test import TestCase, Client
from django.urls import resolve, reverse
from django.http import HttpRequest
import json
from ..serializers import MemoSerializer, CommentSerializer, LikeSerializer
from ..models import Memo, Comment, Like
from rest_framework import status
from ..views import MemoList


# initialize the APIClient app
client = Client()


class TestMemoList(TestCase):
    def setUp(self):
        Memo.objects.create(
            username="dwnusa", title="ABC", content="Hello world ABC")
        Memo.objects.create(
            username="hotak", title="abc", content="Hello world abc")

    def test_GET_request(self):
        response = client.get("/api/v1/memos/")
        memos = Memo.objects.all().order_by("-updated_at")
        serializer = MemoSerializer(memos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_POST_request(self):
        response = self.client.post("/api/v1/memos/",
                             data={"username": "jlkinspection",
                                   "title": "123",
                                   "content": "Hello world 123"})
        memos = Memo.objects.filter(username="jlkinspection").order_by("-updated_at")
        serializer = MemoSerializer(memos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestMemoDetail(TestCase):
    def setUp(self):
        Memo.objects.create(
            username="dwnusa", title="ABC", content="Hello world ABC")
        Memo.objects.create(
            username="hotak", title="abc", content="Hello world abc")

    def test_GET_request(self):
        response = client.get("/api/v1/memos/1/")
        filtered_memo = Memo.objects.filter(pk=1).order_by("-updated_at")
        serializer = MemoSerializer(filtered_memo, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_PUT_request(self):
        response = self.client.put("/api/v1/memos/1/",
                                data={"username": "dwnusa",
                                   "title": "ABCDEF",
                                   "content": "Hello world ABCDEF"},
                                content_type="application/json")
        memos = Memo.objects.filter(pk=1).order_by("-updated_at")
        serializer = MemoSerializer(memos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_DELETE_request(self):
        response = self.client.delete("/api/v1/memos/1/")
        memo = Memo.objects.filter(id=1).order_by("-updated_at")
        serializer = MemoSerializer(memo, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCommentList(TestCase):
    def setUp(self):
        memo1 = Memo.objects.create(
            username="dwnusa", title="ABC", content="Hello world ABC")
        memo2 = Memo.objects.create(
            username="hotak", title="abc", content="Hello world abc")
        Comment.objects.create(
            message="ABC's comment!", memo=memo1)
        Comment.objects.create(
            message="comment2 for ABC!", memo=memo1)
        Comment.objects.create(
            message="abc's comment!", memo=memo2)
        Comment.objects.create(
            message="abc's comment!", memo=memo2)
        Comment.objects.create(
            message="abc's comment!", memo=memo2)

    def test_GET_request(self):
        response = client.get("/api/v1/memos/2/comments/")
        filtered_comment = Comment.objects.filter(memo=2).order_by("-updated_at")
        serializer = CommentSerializer(filtered_comment, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_POST_request(self):
        response = self.client.post("/api/v1/memos/1/comments/",
                             data={"message": "message from jlkinspection",
                                   "memo": 1})
        comment = Comment.objects.filter(message="message from jlkinspection").order_by("-updated_at")
        serializer = CommentSerializer(comment, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCommentDetail(TestCase):
    def setUp(self):
        memo1 = Memo.objects.create(
            username="dwnusa", title="ABC", content="Hello world ABC")
        memo2 = Memo.objects.create(
            username="hotak", title="abc", content="Hello world abc")
        Comment.objects.create(
            message="ABC's comment!", memo=memo1)
        Comment.objects.create(
            message="comment2 for ABC!", memo=memo1)
        Comment.objects.create(
            message="abc's comment!", memo=memo2)
        Comment.objects.create(
            message="abc's comment!", memo=memo2)
        Comment.objects.create(
            message="abc's comment!", memo=memo2)

    def test_GET_request(self):
        response = client.get("/api/v1/memos/1/comments/1/")
        filtered_comment = Comment.objects.filter(pk=1,memo=1).order_by("-updated_at")
        serializer = CommentSerializer(filtered_comment, many=True)
        # print(response.data)
        # print(serializer.data)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_PUT_request(self):
        response = self.client.put("/api/v1/memos/1/comments/1/",
                                   data={"message": "update dwnusa"},
                                   content_type="application/json")
        comment = Comment.objects.filter(pk=1, memo=1).order_by("-updated_at")
        serializer = CommentSerializer(comment, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_DELETE_request(self):
        response = self.client.delete("/api/v1/memos/1/comments/1/")
        comment = Comment.objects.filter(memo=1, id=1).order_by("-updated_at")
        serializer = CommentSerializer(comment, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestLikeList(TestCase):
    def setUp(self):
        memo1 = Memo.objects.create(
            username="dwnusa", title="ABC", content="Hello world ABC")
        memo2 = Memo.objects.create(
            username="hotak", title="abc", content="Hello world abc")
        Like.objects.create(memo=memo1)
        Like.objects.create(memo=memo1)
        Like.objects.create(memo=memo2)
        Like.objects.create(memo=memo2)
        Like.objects.create(memo=memo2)

    def test_GET_request(self):
        response = client.get("/api/v1/memos/2/likes/")
        filtered_like = Like.objects.filter(memo=2).order_by("-updated_at")
        serializer = LikeSerializer(filtered_like, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_POST_request(self):
        response = self.client.post("/api/v1/memos/1/likes/",
                             data={"memo": 1})
        like = Like.objects.filter(memo=1).order_by("-updated_at")
        serializer = LikeSerializer(like, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_DELETE_request(self):
        response = self.client.delete("/api/v1/memos/1/likes/")
        like = Like.objects.filter(memo=1).order_by("-updated_at")
        serializer = LikeSerializer(like, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestLikeDetail(TestCase):
    def setUp(self):
        memo1 = Memo.objects.create(
            username="dwnusa", title="ABC", content="Hello world ABC")
        memo2 = Memo.objects.create(
            username="hotak", title="abc", content="Hello world abc")
        Like.objects.create(memo=memo1)
        Like.objects.create(memo=memo1)
        Like.objects.create(memo=memo2)
        Like.objects.create(memo=memo2)
        Like.objects.create(memo=memo2)

    def test_GET_request(self):
        response = client.get("/api/v1/memos/2/likes/1/")
        filtered_like = Like.objects.filter(memo=2, id=1).order_by("-updated_at")
        serializer = LikeSerializer(filtered_like, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_DELETE_request(self):
        response = self.client.delete("/api/v1/memos/1/likes/1/")
        like = Like.objects.filter(memo=1, id=1).order_by("-updated_at")
        serializer = LikeSerializer(like, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
