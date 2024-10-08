from django.shortcuts import render
from django.http import JsonResponse
from main.utils import get_likes_and_loves

def index(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'index',
    }
    return render(request, 'index.html', context)

def clubs(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'clubs & extra',
    }
    return render(request, 'clubs.html', context)
