
from __future__ import unicode_literals
from django.db import models
from datetime import date
import bcrypt, re, datetime
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9+._-]+@[a-zA-Z0-9+._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'^[A-Za-z]\w+$')
ADDRESS_REGEX=re.compile(r'^[0-9]+[A-Za-z]+[A-Za-z]+$')
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

		try:
			postData['bday']
			bday= datetime.datetime.strptime(postData['bday'], "%Y-%m-%d")
			min_age= datetime.timedelta(weeks =52*21)
			if datetime.datetime.now() - bday < min_age:
				errors['bday'] = "You must be 21 to join"

		except:
			pass

		if postData['bday']:

			if len(postData['bday'])<1:
				errors['bday'] = "Must enter birthdate"
			if datetime.datetime.strptime(postData['bday'],"%Y-%m-%d")>datetime.datetime.today():
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

		if len(postData['address'])<0:
			errors['address'] = "Please provide address"
		# elif not re.match(ADDRESS_REGEX, postData['address']):
		# 	errors['address'] = "Invalid address"

		if len(postData['city'])<0:
			errors['city'] = "Please provide city"

		if len(postData['state'])<0:
			errors['state'] = "Please provide state"

		if len(postData['zipcode'])<5:
			errors['zipcode'] = "Zip code must be at least 5 digits"



		if len(errors) == 0:
			hash1 = bcrypt.hashpw((postData['password'].encode()),bcrypt.gensalt(5))

			new_user=User.objects.create(
				first_name=postData['first_name'],
				last_name=postData['last_name'],
				bday=postData['bday'],
				email=postData['email'],
				password=hash1,
				address=postData['address'],
				city=postData['city'],
				state=postData['state'],
				zipcode=postData['zipcode'],
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
			errors['login_email'] = "Incorrect login info"
		if errors:
			return errors
		return user.id

	def SubValid(self,postData):
		# errors ={}
		#
		# if len(postData['subscribe']):
		# 	subscribe=User.objects.create(
		# 		subscribe=postData['subscribe'],
		# 	)
		# 	return subscribe.id
		# if errors:
		# 	return errors
		# else:
		# 	User.objects.get(id=id).update(subscribe=True)
		pass


class PlanManager(models.Manager):
	def PlanValid(self, postData, id):
		errors = {}
		if len(postData['strain']): #get strain
			strain=Plan.objects.create(
				strain=postData['strain'],

			)
		pass

	def UnsubValid(self, postData):
		# choice ={}
		# if len(postData['yes']):
		# 	Plan.objects.filter(subscribed__id=id).delete()
		# elif len(postData['no']):
		# 	return choice
		pass



class User(models.Model):
	first_name  = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	subscribe = models.BooleanField(default=False)
	bday = models.DateField(null=True)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	city= models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	zipcode = models.IntegerField()
	admin = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	def __unicode__(self):
		return self.first_name + " " + self.last_name

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

	def __unicode__(self):
		return self.strain + "-" + self.user.first_name + " " + self.user.last_name
