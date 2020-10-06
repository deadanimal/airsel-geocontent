from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Role, Geotag

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserUpdateForm(ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name','email']

class RoleUpdateForm(ModelForm):
    class Meta:
        model = Role
        fields = ['role', 'create_access', 'read_access', 'delete_access', 'update_access']

class GeotagCreateForm(ModelForm):
    class Meta:
        model = Geotag
        fields = '__all__'

class GeotagUpdateForm(ModelForm):
    class Meta:
        model = Geotag
        fields = '__all__'