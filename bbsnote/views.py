from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page = request.GET.get('page',1)    #page로 넘어오는 값이 없으면 1로 초기화

    #조회
    board_list = Board.objects.order_by('-create_date')

    #page
    paginator = Paginator(board_list, 5)
    page_obj = paginator.get_page(page)

    context = {'board_list' : page_obj} # board_list 라는 이름으로 페이징 단위 값 넘겨줌
    # return HttpResponse("bbsnote에 오신것을 환영합니다.");
    return render(request, 'bbsnote/board_list.html', context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id)  #Board 클래스의 id값을 저장
    context = {'board':board}   #JSON형식으로 변수저장
    return render(request, 'bbsnote/board_detail.html', context)

def comment_create(request, board_id):
    board = Board.objects.get(id=board_id)
    # comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
    # comment.save()
    board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())   #foreign key 등록 시 사용가능
    return redirect('bbsnote:detail', board_id=board_id)

def board_create(request):
    if request.method == 'POST':    #POST 방식만 처리하도록 설정
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.create_date = timezone.now()
            board.save()
            return redirect('bbsnote:index')
    else:
        form = BoardForm()
    return render(request, 'bbsnote/board_form.html',{'form':form})
