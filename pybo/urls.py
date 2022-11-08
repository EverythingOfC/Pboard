from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'pybo' # 현재 사용중인 앱

urlpatterns = [ # url 매핑과정  **** ( 어떤 모듈의 뷰파일 함수인지를 명시해준다.) ****
    path('',base_views.index,name='index'), # url 별칭은 name으로 준다. 1대1로 대응시킴.
    path('<int:question_id>/',base_views.detail,name='detail'), # 질문의 id값으로 url주소를 매핑한다.

    path('question/create/',question_views.question_create,name='question_create'), # 질문 등록 url매핑
    path('question/modify/<int:question_id>/',question_views.question_modify,name='question_modify'), # 질문 수정 url매핑
    path('question/delete/<int:question_id>/',question_views.question_delete,name='question_delete'), # 질문 삭제 url매핑
    path('question/vote/<int:question_id>/',question_views.question_vote,name='question_vote'), # 질문 추천 url 매핑

    path('answer/create/<int:question_id>/',answer_views.answer_create,name='answer_create'), # 답변 등록 url 매핑
    path('answer/modify/<int:answer_id>/',answer_views.answer_modify,name='answer_modify'), # 답변 수정 url매핑
    path('answer/delete/<int:answer_id>/',answer_views.answer_delete,name='answer_delete'), # 답변 삭제 url매핑
    path('answer/vote/<int:answer_id>/',answer_views.answer_vote,name='answer_vote'),
]

