from django.test import TestCase
from ..models import Memo, Comment, Like


class MemoTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Memo.objects.create(
            username='dwnusa', title='ABC', content='Hello world ABC')
        Memo.objects.create(
            username='hotak', title='abc', content='Hello world abc')

    def test_title_content(self):
        memo_dwnusa = Memo.objects.get(username='dwnusa')
        memo_hotak = Memo.objects.get(username='hotak')
        self.assertEqual(
            memo_dwnusa.get_title_content(), "dwnusa has title : ABC, and content : Hello world ABC")
        self.assertEqual(
            memo_hotak.get_title_content(), "hotak has title : abc, and content : Hello world abc")


class CommentTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Memo.objects.create(
            username='dwnusa', title='ABC', content='Hello world ABC')
        self.memo_dwnusa = Memo.objects.get(username='dwnusa')

        Memo.objects.create(
            username='hotak', title='abc', content='Hello world abc')
        self.memo_hotak = Memo.objects.get(username='hotak')

        Comment.objects.create(
            message='hello dwnusa1', memo=self.memo_dwnusa) # comment id: 1
        Comment.objects.create(
            message='hello dwnusa2', memo=self.memo_dwnusa) # comment id: 2
        Comment.objects.create(
            message='hello dwnusa3', memo=self.memo_dwnusa) # comment id: 3
        Comment.objects.create(
            message='hello hotak1', memo=self.memo_hotak) # comment id: 4
        Comment.objects.create(
            message='hello hotak2', memo=self.memo_hotak) # comment id: 5

    def test_message(self):
        comment_dwnusa1 = Comment.objects.get(id=1)
        comment_dwnusa2 = Comment.objects.get(id=2)
        comment_dwnusa3 = Comment.objects.get(id=3)
        comment_hotak1 = Comment.objects.get(id=4)
        comment_hotak2 = Comment.objects.get(id=5)

        self.assertEqual(
            comment_dwnusa1.get_message(), 'memo (title:' + self.memo_dwnusa.title + ') has comment : hello dwnusa1')
        self.assertEqual(
            comment_dwnusa2.get_message(), 'memo (title:' + self.memo_dwnusa.title + ') has comment : hello dwnusa2')
        self.assertEqual(
            comment_dwnusa3.get_message(), 'memo (title:' + self.memo_dwnusa.title + ') has comment : hello dwnusa3')
        self.assertEqual(
            comment_hotak1.get_message(), 'memo (title:' + self.memo_hotak.title + ') has comment : hello hotak1')
        self.assertEqual(
            comment_hotak2.get_message(), 'memo (title:' + self.memo_hotak.title + ') has comment : hello hotak2')


class LikeTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Memo.objects.create(
            username='dwnusa', title='ABC', content='Hello world ABC')
        self.memo_dwnusa = Memo.objects.get(username='dwnusa')

        Memo.objects.create(
            username='hotak', title='abc', content='Hello world abc')
        self.memo_hotak = Memo.objects.get(username='hotak')

        Like.objects.create(
            memo=self.memo_dwnusa) # like id: 1
        Like.objects.create(
            memo=self.memo_dwnusa) # like id: 2
        Like.objects.create(
            memo=self.memo_hotak) # like id: 3
        Like.objects.create(
            memo=self.memo_hotak) # like id: 4
        Like.objects.create(
            memo=self.memo_hotak) # like id: 5

    def test_message(self):
        like_dwnusa1 = Like.objects.get(id=1)
        like_dwnusa2 = Like.objects.get(id=2)
        like_hotak1 = Like.objects.get(id=3)
        like_hotak2 = Like.objects.get(id=4)
        like_hotak3 = Like.objects.get(id=5)

        self.assertEqual(
            like_dwnusa1.get_memo(), 'memo title: ' + self.memo_dwnusa.title)
        self.assertEqual(
            like_dwnusa2.get_memo(), 'memo title: ' + self.memo_dwnusa.title)
        self.assertEqual(
            like_hotak1.get_memo(), 'memo title: ' + self.memo_hotak.title)
        self.assertEqual(
            like_hotak2.get_memo(), 'memo title: ' + self.memo_hotak.title)
        self.assertEqual(
            like_hotak3.get_memo(), 'memo title: ' + self.memo_hotak.title)
