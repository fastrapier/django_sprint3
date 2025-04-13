from django.http import Http404
from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html', )


def post_detail(request, post_id):
    # for post in posts:
    #     if post['id'] == post_id:
    #         return render(request, 'blog/detail.html', {
    #             'post': post,
    #         })
    raise Http404('Post not found')


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {
        'category': category_slug
    })
