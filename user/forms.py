<<<<<<< HEAD
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
=======
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
>>>>>>> 6463235276beeb7b320d35990b989260ea8036c4
        fields = ['username','email','password1','password2']