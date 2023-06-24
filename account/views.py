from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

from .services import get_redirect_name
from .forms import AccountAuthenticationForm


def index(request):
    return render(request, "account/account.html")


def logout_view(request):
	"""
    Function to logout from an account and redirect to the home page
    """
	logout(request)
	return redirect("home")


def login(request, *args, **kwargs):
	"""
    Function to login as the user and redirect to the home page
    """
	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("account")

	destination = get_redirect_name(request)

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				if destination:
					return redirect(destination)
				return redirect("account")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "account/login.html", context)
