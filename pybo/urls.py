from django.urls import path

from . import views

app_name = 'pybo' # 현재 사용중인 앱

urlpatterns = [ # url 매핑과정
    path('',views.index,name='index'), # url 별칭은 name으로 준다. 1대1로 대응시킴.
    path('<int:question_id>/',views.detail,name='detail'), # 질문의 id값으로 url주소를 매핑한다.
    path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'), # 답변 등록 url 매핑
    path('question/create/',views.question_create,name='question_create'), # 질문 등록 url매핑
]