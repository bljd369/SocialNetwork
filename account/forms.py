from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from account.models import UserProfile

class SignUpForm(ModelForm):
    dob = forms.DateField()
    gender = forms.CharField(max_length=1)
    email_confirmation = forms.EmailField()
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget = forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=20, widget = forms.PasswordInput())



    class Meta:
        model =  User
        fields = ('username', 'first_name', 'last_name', 'email', 'email_confirmation', 'password')


    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
   
        password = cleaned_data.get("password", None)
        password_confirmation = cleaned_data.get('password_confirmation', None)
       
        if password != password_confirmation:
            raise forms.ValidationError("Password and password confirmation should be same")

        email = cleaned_data.get('email', None)
        email_confirmation = cleaned_data.get('email_confirmation', None)
        
        if email != email_confirmation:
            raise forms.ValidationError("Email and email confirmation should be same")
        return cleaned_data

    

    def clean_username(self):
        username = self.cleaned_data.get('username', None)

        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Username is already in use")
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("Email is already in use")
        except User.DoesNotExist:
            return email




    def save(self):
        instance = super(SignUpForm, self).save(commit=False)
       # instance.username = instance.email
        instance.set_password(instance.password)
        instance.save()
        UserProfile.objects.create(user=instance, gender=self.cleaned_data['gender'], dob=self.cleaned_data['dob'])
        return instance