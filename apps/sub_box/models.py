
from __future__ import unicode_literals
from django.db import models
import datetime
import bcrypt, re
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9+._-]+@[a-zA-Z0-9+._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'^[A-Za-z]\w+$')
# Create your models here.

class UserManager(models.Manager):
	def RegValid(self, postData):
		errors ={}
		if len(postData['first_name'])< 2:
			errors['first_name']="Name must be at least 3 characters!"
		elif not re.match(NAME_REGEX, postData['first_name']):
			errors['first_name']="Name must be letter characters only"
		if len(postData['last_name'])< 2:
			errors['last_name']="Name must be at least 3 characters!"
		elif not re.match(NAME_REGEX, postData['last_name']):
			errors['last_name'] = "Name must be letter characters only"

		if len(postData['bday'])<22:
			errors['bday'] = "Must be 21 and over."
		elif datetime.datetime.strptime(postData['bday'],"%Y-%m-%d")>datetime.datetime.today():
			errors['bday'] = "The date cannot be in the future"

		if len(postData['email'])<1:
			errors['email'] = "Email cannot be blank!"
		elif len(User.objects.filter(email=postData['email']))>0:
			errors['email'] = "Email already in use"
		elif not re.match(EMAIL_REGEX, postData['email']):
			errors['email'] = "Invalid email"

		if len(postData['password'])<8:
			errors['password']="Password must be at least 8 characters!"
		elif postData['password']!=postData['confirm']:
			errors['confirm']="Password is not valid."

		if len(errors) == 0:
			hash1 = bcrypt.hashpw((postData['password'].encode()),bcrypt.gensalt(5))

			new_user=User.objects.create(
				first_name=postData['first_name'],
				last_name=postData['last_name'],
				bday=postData['bday'],
				email=postData['email'],
				password=hash1,

			)
			return new_user.id
		return errors

def LoginValid(self,postData):
		errors ={}
		if len(postData['email']) <1:
			errors['login_email'] = "Enter email"
		try:
			user=User.objects.get(email=postData['email'])
			if not bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
				errors['password']="Email/Password incorrect"
		except:
			errors['loginerror'] = "Incorrect login info. Try again or register an account."
		if errors:
			return errors
		return user.id

class PlanManager(models.Manager):
	def PlanValid(self, postData, id):
		# errors = {}
		# if len(postData['strain']) #get strain
		pass

class User(models.Model):
	first_name  = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
<<<<<<< HEAD
	bday = models.DateField(null=T

	rue)
=======
	bday = models.DateField(null=True)
>>>>>>> 548b94a15fd7e8de10599dfa8aef24ddfa84a7d8
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

class Plan(models.Model):
	STRAIN_CHOICES = (
		('Indica', 'Indica'),
		('Sativa', 'Sativa'),
		('Hybrid', 'Hybrid')
	)

	name = models.CharField(max_length=255)
	strain = models.CharField(max_length=255, choices=STRAIN_CHOICES)
	user = models.ForeignKey(User, related_name="subscribed")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = PlanManager()
