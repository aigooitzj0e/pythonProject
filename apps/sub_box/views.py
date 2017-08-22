# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages



def index(request):
	return render(request, 'sub_box/index.html')

def main(request):
	return render(request,'sub_box/index.html')


def login(request):
	errors=User.objects.LoginValid(request.POST)
	if type(errors) ==dict:
		for error in errors.itervalues():
			messages.error(request, error)
		return redirect('/')
	request.session['user_id']=errors
	messages.success(request, "You are logged in!")
	return redirect('/travels')
# 		return redirect('/success')





def register(request):
	errors=User.objects.RegValid(request.POST)
	print errors,type(errors)

	if type(errors)==dict:
		for error in errors.itervalues():
			messages.error(request, error)
		return redirect('/')
	request.session['user_id']=errors
	messages.success(request, "You are registered!")
	return redirect('/travels')	

def logout(request):
	request.session.clear()
	return redirect('/')