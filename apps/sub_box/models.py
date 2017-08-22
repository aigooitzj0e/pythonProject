from __future__ import unicode_literals

from django.db import models

# Create your models here.
from __future__ import unicode_literals
from django.db import models
import datetime
import bcrypt, re
USERNAME_REGEX=re.compile(r'^[A-Za-z0-9]\w+$')
NAME_REGEX=re.compile(r'^[A-Za-z]+\s+[A-Za-z]\w+$')
# Create your models here.

class UserManager(models.Manager):
	def RegValid(self, postData):
		errors ={}
		if len(postData['name'])< 2:
			errors['name']="Name must be at least 3 characters!"
		elif not re.match(NAME_REGEX, postData['name']):
			errors['name']="Must have first and last name"

		if len(postData['user_name'])< 2:
			errors['username']="Name must be at least 3 characters!"

		if len(postData['password'])<8:
			errors['password']="Password must be at least 8 characters!"
		elif postData['password']!=postData['confirm']:
			errors['confirm']="Password is not valid"

		elif not re.match(USERNAME_REGEX, postData['user_name']):
			errors['pass'] = "Invalid username"

		try:
			User.objects.get(user_name = postData['user_name'])
			errors['duplicate'] = "Username taken"

		except:
			pass

		if len(errors) == 0:
			hash1 = bcrypt.hashpw((postData['password'].encode()),bcrypt.gensalt(5))

			new_user=User.objects.create(
				name=postData['name'],
				user_name=postData['user_name'],
				password=hash1,
				
			)
			return new_user.id
		return errors

class User(models.Model):
	name  = models.CharField(max_length=255)
	user_name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()