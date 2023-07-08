from django.shortcuts import render


def cookies_view(request):
    return render(request, 'cookies.html')


def privacy_view(request):
    return render(request, 'privacy.html')
