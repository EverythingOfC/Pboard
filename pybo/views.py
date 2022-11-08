from django.shortcuts import render,get_object_or_404,redirect # 템플릿, 객체 받아옴, 데이터를 찾을 수 없다는 오류, 페이지 이동 임포트
from .models import Question # Question 모델 사용
from django.utils import timezone # 현재시간 리턴을 위함
from .forms import QuestionForm,AnswerForm # 폼 객체들 임포트
from django.http import HttpResponseNotAllowed # 오류 전달을 위함
from django.core.paginator import Paginator # 페이징

def index(request):
    page = request.GET.get('page','1') # get방식으로 호출된 url에서 page값을 가져올 때 사용, 디폴트는 1
    question_list = Question.objects.order_by('-create_date') # 질문 모델의 객체를 생성날짜 역순으로 정렬(-기호)
    paginator = Paginator(question_list,10) # 페이지당 10개씩 보여준다
    page_obj = paginator.get_page(page) # 요청된 페이지에 해당하는 페이징 객체 생성
    context = {'question_list':page_obj}
    return render(request,'pybo/question_list.html',context)
    # 파이썬 데이터를 템플릿에 적용하여 HTML로 반환한다.


def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id) # 있으면 객체리턴, 없으면 404 오류메시지 리턴
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)


def answer_create(request, question_id): # url매핑에 의한 question_id값이 전달된다.
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST': # 답변 등록은 post방식으로만
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail',question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible')
    context = {'question':question,'form':form}
    return render(request,'pybo/question_detail.html',context)

def question_create(request):
    if request.method == 'POST': # Post방식의 요청일 시 ( 저장하기 )

        form = QuestionForm(request.POST) # 사용자가 입력한 내용이 담겨있음
        if form.is_valid(): # 폼이 유효하면
            question = form.save(commit=False) # 임시 저장하여 리턴받는다.
            question.create_date = timezone.now() # 실제 저장을 위한 작성일시 설정
            question.save() # 데이터를 실제로 저장
            return redirect('pybo:index') # 해당 url별칭이 가리키는 곳으로 이동

    else: # Get방식의 요청일 시( 질문 등록하기 )
            form = QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html',context)


