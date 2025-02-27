from .models import *
from django import forms

class registerForm(forms.ModelForm):
    class Meta:
        model = register
        fields = ('username', 'first_name', 'last_name','profile_picture', 'bio', 'phno','email', 'password', 'reg_type')
    
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
    
class ModifyAccountForm(forms.ModelForm):
    class Meta:
        model = register
        fields = ['first_name', 'last_name', 'profile_picture', 'bio', 'phno', 'email']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'phno': forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Enter your phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }
        
class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class blogForm(forms.ModelForm):
    class Meta:
        model = blogs
        fields = ('title', 'content', 'image')

