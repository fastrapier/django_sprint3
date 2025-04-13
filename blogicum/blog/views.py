from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Category, Post


def index(request):
    current_time = timezone.now()

    post_list = Post.objects.filter(is_published=True, category__is_published=True,
                                    pub_date__lt=current_time).order_by('-created_at')[:5]

    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    current_time = timezone.now()
    post = get_object_or_404(Post, id=post_id, is_published=True,
                             category__is_published=True, pub_date__lt=current_time)

    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    current_time = timezone.now()
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lt=current_time
    ).order_by('-created_at')

    context = {
        'category': category,
        'post_list': post_list,
    }

    return render(request, 'blog/category.html', context)
