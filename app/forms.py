from app import models
from .models import Traveller,Houseown,Review, Comment, Post
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       PasswordResetForm, SetPasswordForm,
                                       UserCreationForm, UsernameField)
from django.contrib.auth.models import User
from django.forms import widgets
from django.utils.translation import gettext_lazy as _


class ProfileRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model =User
        fields=['username','email','password1','password2']
        labels = { 'email':'Email'}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
    def save(self, commit=True):
        user = super(ProfileRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user


class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofous':True, 'class' : 'form-control'}))
    password = forms.CharField(label =_("Password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class' : 'form-control'}))

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label =_("Old Password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class' : 'form-control'})) 

    new_password1 = forms.CharField(label =_("New Password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class' : 'form-control'}),
    help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label =_(" Confrim New Password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class' : 'form-control'}))



class PasswordresetForm(PasswordResetForm):
    email=forms.EmailField(label =_("Email"),max_length=233,
    widget=forms.EmailInput(attrs={'autocomplete':'email', 'class' : 'form-control'}))


class PasswordSetForm(SetPasswordForm):

   new_password1 = forms.CharField(label =_("New Password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class' : 'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
   new_password2 = forms.CharField(label =_(" Confrim New Password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class' : 'form-control'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Traveller
        fields = ['name','contact_no','image', 'verification']
        widgets = {

            
            'contact_no':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'verification':forms.FileInput(attrs={'class':'form-control'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']

        widgets = {
            'comment': forms.Textarea(attrs = {'rows':3, 'cols':40}),
            


        }
    


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subtitle','title','content','image']
        widgets = {
           'title':forms.TextInput(attrs={  'class':'form-control'}),
           'content' :forms.Textarea(attrs={'class':'form-control'}),
           'subtitle' :forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            

        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'comment': forms.Textarea(attrs = {'rows':3, 'cols':40})
        }
    





