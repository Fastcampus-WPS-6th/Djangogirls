from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def post_list(request):
    # post_list view가 published_date가 존재하는 Post목록만 보여주도록 수정
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        # posts key의 value는 QuerySet
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


# View(Controller) 구현
# post_detail기능을 하는 함수를 구현
# 'post'라는 key로 Post.objects.first()에 해당하는 Post객체를 전달
# 템플릿은 'blog/post_detail.html'을 사용
def post_detail(request, pk):
    # Post인스턴스 1개만 가져옴, 변수명은 posts가 아닌 단일객체를 나타내는 post사용

    # get에 실패했을때 발생하는 예외
    #   Post.DoesNotExist
    # HTTP로 문자열을 돌려주려면
    #   HttpResponse
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('No post', status=404)

    # 'post'key값으로 Post인스턴스 하나 전달
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    if request.method == 'POST':
        return HttpResponse('POST request')
    elif request.method == 'GET':
        context = {

        }
        return render(request, 'blog/post_form.html', context)
