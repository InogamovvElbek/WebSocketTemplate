from django.shortcuts import render

from .models import Category


def chat(request):
    return render(request, 'chat.html')


def category_list(request):
    categories = Category.objects.order_by('title')
    return render(request, 'category-list.html', {'categories': categories})


def score_list(request):
    return render(request, 'score-list.html')
