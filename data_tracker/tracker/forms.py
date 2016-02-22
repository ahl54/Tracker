from django import forms
from .models import Tracker, TrackerUser, User
from django.contrib.auth.forms import UserCreationForm

class TrackerForm(forms.ModelForm):

    class Meta:
        model = Tracker
        fields = ('requester_name', 'email', 'accession', 'study_name', 'source', 'link', 'samples', 'tissue', 'adult_or_pediatric', 'citation', 'details', 'priority', 'confirmation', 'subscription', 'summary')
        widgets = {'myfield': forms.TextInput(attrs={'div': 'field-style-vert'})}

class LoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput,label="Email")
    password = forms.CharField(widget=forms.PasswordInput,label="Password")
    username = forms.EmailField(widget=forms.TextInput,label="Username")
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        widgets = {'myfield': forms.TextInput(attrs={'div': 'field-style-vert'})}
        widgets = {'myfield': forms.PasswordInput(attrs={'div': 'field-style-vert'})}

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput,label="Username")
    email = forms.EmailField(widget=forms.TextInput,label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput,label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,label="Password (again)")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'myfield': forms.PasswordInput(attrs={'div': 'field-style-vert'})}

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        # Verifies that the user doesn't already exist
        try:
            if 'email' in self.cleaned_data:
                u = User.objects.get(email=email)
                email = u.TrackerUser.email
                if self.cleaned_data['email'] == email:
                    raise forms.ValidationError("This email address is already registered.")
        except:
            print(self.cleaned_data['email'])
        else:
            # Verifies that the values entered into the password fields match
            if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
                if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                    raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        new_user = super(RegisterForm, self).save(commit=False)
        new_user.set_password(self.cleaned_data['password1'])
        if commit:
            new_user.save()
            trackeruser = TrackerUser(user = new_user)
            trackeruser.save()
        return new_user
