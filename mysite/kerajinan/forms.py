from django import forms
from registration.forms import RegistrationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from kerajinan.models import Product, Category

class PostForm(forms.ModelForm):
	class Meta:
		model 	= Product
		fields 	= ('category','title', 'price','image', 'description')

class SliderForm(forms.ModelForm):
	class Meta:
		model 	= Product
		fields 	= ('title', 'image', 'description')

class CategoryForm(forms.ModelForm):
	class Meta:
		model 	= Product
		fields 	= ('title','description')
