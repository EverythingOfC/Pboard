from django import forms
from pybo.models import Question,Answer


class QuestionForm(forms.ModelForm):
    class Meta: # 사용할 모델과 속성을 저장하는 클래스
        model = Question # 사용할 모델
        fields = ['subject','content'] # Question form에서 사용할 Question모델의 속성
        labels = {
            'subject':'제목',
            'content':'내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels={
            'content':'답변내용'
        }