# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages



def index(request):
	return render(request, 'sub_box/index.html')

def main(request):
	return render(request, 'sub_box/register.html')

def login(request):
	errors=User.objects.LoginValid(request.POST)
	if type(errors) ==dict:
		for field, error in errors.iteritems():
			messages.error(request, error, extra_tags=field)
		return redirect('/') #Must redirect to pop up login
	request.session['user_id']=errors
	messages.success(request, "You are logged in!")
	return redirect('/member')




def register(request):
	errors=User.objects.RegValid(request.POST)
	print errors,type(errors)

	if type(errors)==dict:
		for error in errors.itervalues():
			messages.error(request, error)
		return redirect('/')
	request.session['user_id']=errors
	messages.success(request, "You are registered!")
	return redirect('/member')

def unsubscribe(request):
	return redirect('/unsubscribe')

def member(request):
	# errors=User.objects.PlanValid(request.POST)
	# if type(errors)==dict:
	# 	for error in errors.itervalues():
	# 		messages.error(request, error)
	# 	return redirect('/')
	# request.session['user_id']=errors
	# messages.success(request, "You have subscribed!")
	return render(request, "sub_box/member.html")

def cart(request):
	return redirect('/cart')

def logout(request):
	request.session.clear()
	return redirect('/')
