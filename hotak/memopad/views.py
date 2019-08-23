from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from memopad.models import MemoAppModel
from memopad.pageManager import pageManager

rows = 2
def home(request):   
    memo_list = MemoAppModel.objects.order_by('-id')[0:rows]
    cur_page =1
    total_cnt = MemoAppModel.objects.all().count()
    print ('home total_cnt', total_cnt)
    print ('home total_cnt type', type(total_cnt))
    PageManager = pageManager()
    page_list = PageManager.GetTotalPageList(total_cnt, rows)
    return render_to_response('test.html', {'memo_list': memo_list, 'total_cnt': total_cnt, 'cur_page':cur_page ,'page_list':page_list} )

def ViewAddMemo(request):
    return render_to_response('memo.html')

@csrf_exempt
def AddMemo(request):
    _memo = MemoAppModel(
                    title = request.POST['title'],
                    nickname = request.POST['nickname'],
                    create_date = timezone.now(),
                    memo = request.POST['memo'],
                    hits = 0
                    )
    _memo.save()

    url = '/update_memo_list?current_page=1'
    return HttpResponseRedirect(url)

def UpdateMemoList(request):
    cur_page = request.GET['current_page']
    cur_page = int(cur_page)

    total_cnt = MemoAppModel.objects.all().count()

    print ('total_cnt', total_cnt)
    
    memo_list = MemoAppModel.objects.order_by('-id')[0:rows]

    print('######################################################')
    print(memo_list)
    print('######################################################')

    PageManager = pageManager()
    page_list = PageManager.GetTotalPageList(total_cnt, rows)

    return render_to_response('test.html', {'memo_list': memo_list, 'total_cnt': total_cnt, 'cur_page':cur_page ,'page_list':page_list} )


def ViewMemo(request):
    memo_id = request.GET['memo_id']
    cur_page = request.GET['current_page']
    search_str = request.GET['search_str']

    memo_info = MemoAppModel.objects.get(id=memo_id)

    MemoAppModel.objects.filter(id=memo_id).update(hits = memo_info.hits + 1)
    
    return render_to_response('view.html', {'memo_id': memo_id, 'cur_page': cur_page, 'search_str': search_str, 'memo_info': memo_info})

@csrf_exempt
def ModifyMemo(request):
    memo_id = request.POST['memo_id']
    current_page = request.POST['current_page']

    MemoAppModel.objects.filter(id=memo_id).update(title= request.POST['title'], memo= request.POST['memo'])

    url = '/update_memo_list?current_page=' + str(current_page)
    return HttpResponseRedirect(url)

def ViewModifyMemo(request):
    memo_id = request.GET['memo_id']
    cur_page = request.GET['current_page']
    search_str = request.GET['search']

    memo_info = MemoAppModel.objects.get(id=memo_id)

    return render_to_response('viewmdifymemo.html', {'memo_id': memo_id, 'cur_page': cur_page, 'search_str': search_str, 'memo_info': memo_info})

def DeleteMemo(request):
    
    memo_id = request.GET['memo_id']
    cur_page = request.GET['current_page']
    cur_page = int(cur_page)
    
    MemoAppModel.objects.filter(id=memo_id).delete()
    
    total_cnt = MemoAppModel.objects.all().count()

    PageManager = pageManager()
    page_list = PageManager.GetTotalPageList(total_cnt, rows)
    
    if not (cur_page in page_list):
        cur_page = cur_page - 1

    url = '/update_memo_list?current_page=' + str(cur_page)
    return HttpResponseRedirect(url)