from django.db import models
from django.contrib.auth.models import User

class Question(models.Model): # 테이블 생성 ( 장고에서는 모델 )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') # 유저의 질문이므로 유저가 삭제되면 질문도 삭제
    subject = models.CharField(max_length=200) # char형(글자수 제한 O)
    content = models.TextField() # 텍스트 형(글자수 제한 x)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True,blank=True) # null값이나 입력 데이터 검증 시 값을 비워둘 수 있음
    voter = models.ManyToManyField(User,related_name='voter_question')  # 추천인 추가 (다대다 관계)
    def __str__(self): # id값 대신 제목을 표시한다.
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문이 있어야 답변이 있으므로 질문이 삭제되면 답변도 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # null값이나 입력 데이터 검증 시 값을 비워둘 수 있음
    voter = models.ManyToManyField(User,related_name='voter_answer')  # 추천인 추가

# 모델이 신규로 생성되거나 변경되면 cmd에서 makemigrations명령을 사용해야 한다.
# filter: 조건에 해당하는 데이터 모두 리턴
# get: 조건에 해당하는 데이터 한 건만 리턴
