from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.db.models import ImageField
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class Category(models.Model):
	title			= models.CharField(max_length=50)
	slug 			= models.CharField(max_length=200, null=True, blank=True)
	description		= models.CharField(max_length=250, null=True, blank=True)
	created_date 	= models.DateTimeField(auto_now_add=True)

	
	def __str__(self):
		return self.title;

class Product(models.Model):
	# author 			= models.ForeignKey(settings.AUTH_USER_MODEL)
	category 		= models.ForeignKey('Category')
	userprofile		= models.ForeignKey('UserProfile')
	title			= models.CharField(max_length=50)
	slug 			= models.CharField(max_length=200, null=True, blank=True)
	price			= models.DecimalField(max_digits=10, decimal_places=2)
	image			= models.ImageField(upload_to='media')
	description		= models.TextField()
	created_date	= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now_add=False, auto_now=True)

	def save(self):
		slug = slugify(self.title)
		if self.slug != slug:
			self.slug = slug
		return super(Product,self).save()

	def get_price(self):
		return self.price

	def __str__(self):
		return self.title;

class MyUserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			username = username,
			email    = self.normalize_email(email),
		)
		user.is_active	= True
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, username, email, password):
		user = self.create_user(username=username, email=email, password=password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user 

class UserProfile(AbstractBaseUser, PermissionsMixin):

 	alphanumeric 	= RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')
	username 		= models.CharField(unique=True, max_length=20, validators=[alphanumeric])
	email 			= models.EmailField(verbose_name='email address', unique=True, max_length=244)
	first_name 		= models.CharField(max_length=30, null=True, blank=True)
	last_name 		= models.CharField(max_length=50, null=True, blank=True)
	date_of_birth 	= models.DateField(null=True);
	date_joined 	= models.DateTimeField(auto_now_add=True)
	is_active 		= models.BooleanField(default=True, null=False)
	is_staff 		= models.BooleanField(default=False, null=False)


	profile_image 	= models.ImageField(upload_to="profile")

	objects 		= MyUserManager()

	USERNAME_FIELD 	= 'email'
	REQUIRED_FIELDS	= ['username']

	def get_full_name(self):
		fullname = self.first_name+" "+self.last_name
		return self.fullname

	def get_short_name(self):
		return self.username

	def __str__(self):
		return self.email

class Static(models.Model):
	title			= models.CharField(max_length=50)
	description		= models.TextField()
	images			= models.ImageField(upload_to="slider")
	images2			= models.ImageField(upload_to="slider")

	def __str__(self):
		return self.title

class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')

	def colors(self):
		return self.all().filter(category='color')

VAR_CATEGORIES = (
	('size','size'),
	('color','color'),
	('package', 'package'),
	)

class Variation(models.Model):
	product 		= models.ForeignKey(Product)
	category 		= models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	title 			= models.CharField(max_length=120)
	price 			= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	updated 		= models.DateTimeField(auto_now_add=False, auto_now=True)
	active 			= models.BooleanField(default=True)

	objects 		= VariationManager()

	def __str__(self):
		return self.title

class Cart(models.Model):
	total 			= models.DecimalField(max_digits=65, decimal_places=2, default=0.00)
	timestamp 		= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 		= models.DateTimeField(auto_now_add=False, auto_now=True)
	active 			= models.BooleanField(default=True)

	def __str__(self):
		return "Card id: %s" %(self.id)

class CartItem(models.Model):
	cart 			= models.ForeignKey('Cart', null=True, blank=True)
	product 		= models.ForeignKey(Product)
	variations 		= models.ManyToManyField(Variation, null=True, blank=True)
	quantity 		= models.IntegerField(default=1)
	line_total 		= models.DecimalField(default=10.99, max_digits=65, decimal_places=2)
	notes 			= models.TextField(null=True, blank=True)
	timestamp 		= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 		= models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		try:
			return str(self.cart.id)
		except:
			return self.product.title

			