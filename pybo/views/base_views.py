from django.shortcuts import render,get_object_or_404,redirect # 템플릿, 객체 받아옴, 데이터를 찾을 수 없다는 오류, 페이지 이동 임포트
from ..models import Question,Answer # Question, Answer모델 사용
from django.core.paginator import Paginator # 페이징
from django.db.models import Q

def index(request): # 기본화면 뷰
    page = request.GET.get('page','1') # get방식으로 호출된 url에서 page값을 가져올 때 사용, 디폴트는 1
    kw = request.GET.get('kw','') # get방식으로 호출된 url에서 검색어를 가져올 때
    question_list = Question.objects.order_by('-create_date') # 생성일자 역순으로 정렬한다.
    if kw:
        question_list = question_list.filter( # filter함수에서 모델 속성에 접근하기 위해서는 __를 이용하여 하위 속성에 접근할 수 있다.
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct() # 중복 제거를 위함
    paginator = Paginator(question_list,10) # 페이지당 10개씩 보여줌
    page_obj = paginator.get_page(page)
    context={'question_list':page_obj,'page':page,'kw':kw}
    return render(request,'pybo/question_list.html',context)


def detail(request,question_id): # detail 뷰
    question = get_object_or_404(Question,pk=question_id) # 있으면 객체리턴, 없으면 404 오류메시지 리턴
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)

