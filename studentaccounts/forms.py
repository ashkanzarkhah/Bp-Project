from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    studentnumber = forms.IntegerField(required=True, label='StudentNumber')

    class Meta:
        model = User
        fields = ("username", "email","studentnumber", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.studentnumber = self.cleaned_data["studentnumber"]
        if commit:
            user.save()
        return user
class AuthenticationForm(AuthenticationForm):
    def clean_username(self):
        username = self.data['username']
        if '@' in username:
            try:
                username = User.objects.get(email=username).username
            except ObjectDoesNotExist:
                raise ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username':self.username_field.verbose_name},
                )
        return username