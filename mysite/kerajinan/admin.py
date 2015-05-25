from django.contrib import admin
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Category
from .models import Product
from .models import Static, Cart, CartItem
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,ReadOnlyPasswordHashField


from kerajinan.models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            UserProfile._default_manager.get(username=username)
        except UserProfile.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        #ngecek kalo kedua password itu bener
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        #ngesave password pake hash format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label="password",
                                         help_text="""Raw passwords are not stored, so there is no way to see this
                                         user's password, but you can change the password using <a href=\"password/\">
                                         this form</a>.""")

    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields = ('username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'user_permissions')

    def clean_password(self):
        return self.initial["password"]

class MyUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name','date_of_birth','profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart

admin.site.register(UserProfile,MyUserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Static)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
