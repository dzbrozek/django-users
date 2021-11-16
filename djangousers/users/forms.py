from typing import cast

from django import forms
from django.forms import widgets
from users.models import User


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'birthday']
        widgets = {'password': widgets.PasswordInput()}
        help_texts = {
            'birthday': "Format: yyyy-mm-dd",
        }

    def save(self, commit: bool = True) -> User:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return cast(User, user)
