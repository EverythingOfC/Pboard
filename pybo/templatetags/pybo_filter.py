import markdown # 글쓰기 도구
from django import template
from django.utils.safestring import mark_safe

register = template.Library() # 템플릿 라이브러리 객체를 생성한다.

# 템플릿 필터 함수 annotation
@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def mark(value): # 입력 문자열을 HTML로 변환하는 함수
    extensions = ['nl2br','fenced_code'] # 줄바꿈문자를 <br>로 , 마크다운의 소스코드 표현에 필요함.
    return mark_safe(markdown.markdown(value,extensions=extensions))
