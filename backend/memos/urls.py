# memos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.MemoList.as_view(), name='MemoList'),
    path('<int:memo_id>/', views.MemoDetail.as_view(), name='MemoDetail'),
    path('<int:memo_id>/comments/', views.CommentList.as_view(), name='CommentList'),
    path('<int:memo_id>/comments/<int:comment_id>', views.CommentDetail.as_view(), name='CommentDetail'),
    path('<int:memo_id>/likes/', views.LikeList.as_view(), name='LikeList'),
    path('<int:memo_id>/likes/<int:like_id>', views.LikeDetail.as_view(), name='LikeDetail'),

    # path('<int:memo_id>/', views.MemoDetail.as_view(), name='MemoDetail'),
    # path('<int:memo_id>/like/', views.LikeMemo.as_view(), name='LikeMemo'),
    # path('<int:memo_id>/unlike/', views.UnlikeMemo.as_view(), name='UnlikeMemo'),
    # path('<int:pk>/', views.MemoDetail.as_view(), name='MemoDetail'),
    # path('create/', views.MemoCreate.as_view()),
]
