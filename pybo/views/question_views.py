from django.contrib import messages
from django.contrib.auth.decorators import login_required  # 로그인 요청 임포트
from django.shortcuts import render, get_object_or_404, redirect  # 템플릿, 객체 받아옴, 데이터를 찾을 수 없다는 오류, 페이지 이동 임포트
from django.utils import timezone  # 현재시간 리턴을 위함

from ..forms import QuestionForm, AnswerForm  # 폼 객체들 임포트
from ..models import Question, Answer  # Question, Answer모델 사용


@login_required(login_url='common:login') # 로그인이 필요한 함수
def question_create(request):
    if request.method == 'POST': # Post방식의 요청일 시 ( 저장하기 )

        form = QuestionForm(request.POST) # 사용자가 입력한 내용이 담겨있음
        if form.is_valid(): # 폼이 유효하면
            question = form.save(commit=False) # 임시 저장하여 리턴받는다.
            question.author = request.user # author 속성에 로그인 계정 저장
            question.create_date = timezone.now() # 실제 저장을 위한 작성일시 설정
            question.save() # 데이터를 실제로 저장
            return redirect('pybo:index') # 해당 url별칭이 가리키는 곳으로 이동

    else: # get 방식의 요청일 시 (질문 등록하기)
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url="common:login") # 로그인이 필요한 함수
def question_modify(request,question_id): # 질문 수정
    question = get_object_or_404(Question,pk=question_id)

    if request.user != question.author:
        messages.error(request,'수정권한이 없습니다') # 넌필드오류를 발생시킨다.
        return redirect('pybo:detail',question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST,instance=question) # post형식으로 데이터를 받아서 form에 저장
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now() # 수정일시 저장
            question.save()
            return redirect('pybo:detail',question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form':form}
    return render(request,'pybo/question_form.html',context)


@login_required(login_url="common:login") # 로그인이 필요한 함수
def question_delete(request,question_id): # 질문 삭제
    question = get_object_or_404(Question,pk=question_id)
    if request.user != question.author:
        messages.error(request,'삭제권한이 없습니다')
        return redirect('pybo:detail',question_id=question.id)
    question.delete()
    return redirect('pybo:index') # 기본화면으로 이동


@login_required(login_url='common:login')
def question_vote(request, question_id): # 질문 추천
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        question.voter.add(request.user) # add함수로 추천인 추가
    return redirect('pybo:detail', question_id=question.id)

