from django.shortcuts import render


def main_view(request):
    return render(request, "main.html")


def cookies_view(request):
    return render(request, "cookies.html")


def privacy_view(request):
    return render(request, "privacy.html")
