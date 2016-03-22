from django import forms
from .models import Tracker, TrackerUser, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class TrackerForm(forms.ModelForm):

    class Meta:
        model = Tracker
        fields = ('requester_name', 'email', 'accession', 'source', 'cancer_type', 'specimen_type', 'adult_or_pediatric', 'samples', 'study_link', 'PMID', 'citation', 'details', 'group', 'level', 'confirmation', 'subscription')
        widgets = {'myfield': forms.TextInput(attrs={'div': 'field-style-vert'})}
        help_texts = {
            'requester_name': 'Jane Doe',
            'email': 'janedoe@company.com',
            'accession':'EGA-000123456',
            'source': 'TCGA',
            'cancer_type': 'Breast Adenocarinoma',
            'specimen_type': 'patient, cell line, xenograft',
            'study_link': 'http://www.ncbi.nlm.nih.gov',
            'PMID': '000001',
            'citation': 'Doe et. al, Journal 2012',
            'details': 'RNA-seq, expression median z-Score',
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_id', '%s')
        kwargs.setdefault('label_suffix', '')
        super(TrackerForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'placeholder': field.help_text
                })


class LoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput,label="Email")
    password = forms.CharField(widget=forms.PasswordInput,label="Password")
    username = forms.EmailField(widget=forms.TextInput,label="Username")
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = User
        fields = ('email', 'username', 'password',)
        widgets = {'myfield': forms.TextInput(attrs={'div': 'field-style-vert'})}
        widgets = {'myfield': forms.PasswordInput(attrs={'div': 'field-style-vert'})}
"""
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
"""
class TrackerUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(TrackerUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = TrackerUser
        fields = ()
    """
    username = forms.EmailField(widget=forms.TextInput,label="Username")
    email = forms.EmailField(widget=forms.TextInput,label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput,label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,label="Password (again)")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'myfield': forms.PasswordInput(attrs={'div': 'field-style-vert'})}

    def __init__(self, *args, **kwargs):
        super(TrackerUserCreationForm, self).__init__(*args, **kwargs)
        #username_temp = kwargs['email']
        del self.fields['username']

    def clean(self):
        cleaned_data = super(TrackerUserCreationForm, self).clean()
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
        new_user = super(TrackerUserCreationForm, self).save(commit=False)
        new_user.set_password(self.cleaned_data['password1'])
        if commit:
            new_user.save()
            trackeruser = TrackerUser(user = new_user)
            trackeruser.save()
        return new_user
    """

class TrackerUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(TrackerUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['email']

    class Meta:
        model = TrackerUser
        fields = ("email",)


class RegisterForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput,label="Name")
    email = forms.EmailField(widget=forms.TextInput,label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput,label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,label="Password (again)")

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
        widgets = {'myfield': forms.PasswordInput(attrs={'div': 'field-style-vert'})}

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        #username_temp = kwargs['email']
        #del self.fields['username']

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

class DocumentForm(forms.Form):
    rawfile = forms.FileField(
        label='raw',
        help_text='max. 42 megabytes'
    )
    stagingfile = forms.FileField(
        label='staging',
        help_text='max. 42 megabytes'
    )
