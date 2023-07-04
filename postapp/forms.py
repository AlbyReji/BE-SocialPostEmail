from django.forms import ModelForm
from django import forms 
from django.contrib.auth import authenticate, get_user_model
from django.forms import ValidationError
from .models import Post

User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(label = 'First Name')
    Last_name = forms.CharField(label = 'Last Name')
    email = forms.EmailField(label='Email address')
    phone_number = forms.CharField(label='Phone number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'Last_name',
            'email',
            'phone_number',
            'password',
            'password2',
        ]
    
    def clean(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        Last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email has already been registered")
        
        return super(UserRegisterForm, self).clean(*args, **kwargs)




class PostForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.TextInput,max_length=100)
    description = forms.CharField(widget=forms.TextInput)
    image = forms.ImageField(widget=forms.ClearableFileInput)
    


    class Meta:
        model = Post
        fields = ['caption', 'description', 'image']
