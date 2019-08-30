from django.test import TestCase, Client
from django.urls import resolve, reverse
from django.http import HttpRequest
import json
from ..serializers import MemoSerializer
from ..models import Memo
from rest_framework import status
from ..views import MemoList


# initialize the APIClient app
client = Client()


class Test_MemoList(TestCase):
    def setUp(self):
        Memo.objects.create(
            username='dwnusa', title='ABC', content='Hello world ABC')
        Memo.objects.create(
            username='hotak', title='abc', content='Hello world abc')

    def test_root_url_resolves_to_MemoList_view(self):
        response = client.get('/api/v1/memos/')
        # response = client.get(reverse('MemoList'))
        memos = Memo.objects.all().order_by('-updated_at')
        serializer = MemoSerializer(memos, many=True)
        # print(response.data)
        # print('\n')
        # print(serializer.data)
        # print(response.data == serializer.data)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_save_a_POST_request(self):
        response = self.client.post('/api/v1/memos/',
                             data={'username': 'jlkinspection',
                                   'title': '123',
                                   'content': 'Hello world 123'})
        memos = Memo.objects.filter(username='jlkinspection').order_by('-updated_at')
        serializer = MemoSerializer(memos, many=True)
        # print(response.data)
        # print('\n')
        # print(serializer.data)
        # print(response.data == serializer.data)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
