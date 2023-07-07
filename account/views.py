import logging

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import AccountAuthenticationForm, AccountRegisterForm
from .services import get_redirect_name

logger = logging.getLogger(__name__)

def index_view(request):
    """
	View function render the account page for an user
	"""
    return render(request, "account/account.html")


def logout_view(request):
	"""
    Function to logout from an account and redirect to the home page
    """
	logout(request)
	return redirect("home")


def login_view(request, *args, **kwargs):
	"""
    Function to login as an user and redirect to the account page
    """
	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("account")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			nickname = form.cleaned_data['nickname']
			password = form.cleaned_data['password']
			account = authenticate(nickname=nickname, password=password)
			if account:
				login(request, account)
				logger.info(f"User \"{account}\" has been login")
				return redirect("account")
	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "account/login.html", context)


def register_view(request, *args, **kwargs):
	"""
	View function to create and register an account
	"""
	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("account")
	
	if request.POST:
		form = AccountRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			nickname = form.cleaned_data['nickname'].lower()
			raw_password = form.cleaned_data['password1']
			account = authenticate(nickname=nickname, password=raw_password)
			logger.info(f"New user {account} has been registered")
			login(request, account)
			return redirect('account')
	else:
		form = AccountRegisterForm()

	context['signup_form'] = form

	return render(request, "account/register.html", context)
