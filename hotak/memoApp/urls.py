"""memoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from memopad import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('^$', views.home),
    # path('^view_add_memo/$', views.ViewAddMemo),
    # path('^add_memo/$', views.AddMemo),
    # path('^update_memo/$', views.UpdateMemo),
    path('', views.home),
    path('view_add_memo/', views.ViewAddMemo),
    path('add_memo/', views.AddMemo),
    path('update_memo_list/', views.UpdateMemoList),
    path('view_memo/', views.ViewMemo),
    path('view_modify_memo/', views.ViewModifyMemo),
    path('modify_memo/', views.ModifyMemo),
    path('delete_memo/', views.DeleteMemo),
]
