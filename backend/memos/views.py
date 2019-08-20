from django.shortcuts import render
from . import models

# Create your views here.
# posts/views.py
from rest_framework import generics

from .models import Memo
from .serializers import MemoSerializer


class MemoList(generics.ListAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer


# class MemoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer

# class MemoDetail(models.Model):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer