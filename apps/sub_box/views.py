# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
from .models import User, Plan
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
	request.session['id']=errors
	messages.success(request, "You are logged in!")
	return redirect('/member')

def register(request):
	errors=User.objects.RegValid(request.POST)
	print errors,type(errors)

	if type(errors)==dict:
		for error in errors.itervalues():
			messages.error(request, error)
		return redirect('/')
	request.session['id']=errors
	messages.success(request, "You are registered!")
	return redirect('/member')

def subscribe(request):
	errors=User.objects.SubValid(request.POST)
	if type(errors)==dict:
		for error in errors.itervalues():
			messages.error(request, error)
		return redirect('/cart')
	request.session['subscribe']=errors
	messages.success(request, "You are subscribed!")
	return redirect('/member')

def unsubconfirm(request):
	return render(request,'sub_box/unsubsribe.html')

def unsubscribe(request):
	choice=Plan.objects.UnsubValid()
	return redirect('/unsubscribe')

def member(request):
	try: #checks is user is logged in.
		request.session['id']
	except:
		return redirect('/')
	context = {
		'users':User.objects.all(),
		'main_user': User.objects.get(id = request.session['id']),
		'plan': Plan.objects.get(strain=request.POST['strain']),
		# 'my_sub': Plan.objects.filter(user__id= request.session['id']),

	}
	return render(request, "sub_box/member.html", context)

def cart(request):
	return render(request,'sub_box/cart.html')

def logout(request):
	request.session.clear()
	return redirect('/')

def ordercomplete(request):
	context = {
		'random' : get_random_string(length=14),
		'main_user': User.objects.get(id = request.session['id']),
		
	}
	return render(request, "sub_box/ordercomplete.html", context)
