# memos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.MemoList.as_view(), name='MemoList'),
    # path('<int:pk>/', views.MemoDetail.as_view(), name='MemoDetail'),
    # path('create/', views.MemoCreate.as_view()),
]
