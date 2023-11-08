from django.shortcuts import render


def home(request):
    return render(request,'index.html')


def shop(request):
    return render(request,'shop.html')


def blog(request):
    return render(request,'blog.html')