from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] # 제목으로 질문을 검색한다.


# Register your models here.

admin.site.register(Question,QuestionAdmin) # 검색기능을 추가한다.
