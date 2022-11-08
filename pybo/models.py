from django.db import models

class Question(models.Model): # 테이블 생성 ( 장고에서는 모델 )
    subject = models.CharField(max_length=200) # char형(글자수 제한 O)
    content = models.TextField() # 텍스트 형(글자수 제한 x)
    create_date = models.DateTimeField()

    def __str__(self): # id값 대신 제목을 표시한다.
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문이 있어야 답변이 있으므로 외래키 속성 지정
    content = models.TextField()
    create_date = models.DateTimeField()

# 모델이 신규로 생성되거나 변경되면 makemigrations명령을 사용해야 한다.
# filter: 조건에 해당하는 데이터 모두 리턴
# get: 조건에 해당하는 데이터 한 건만 리턴
