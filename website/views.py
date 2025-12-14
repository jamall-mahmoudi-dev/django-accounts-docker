from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # نمایش جدیدترین‌ها اول
    return render(request, 'website/home.html', {'posts': posts})
    # posts = Post.objects.all()
    # return render(request, 'website/home.html', {'posts': posts})
