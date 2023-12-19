from django.forms import ModelForm, Form, IntegerField, NumberInput, EmailField, TextInput, CharField, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User,  AbstractBaseUser
from django.db.models import EmailField as dbEmailField


class BattleForm(Form):
    user_roll = IntegerField(
        label='Choose number 1..10',
        min_value=1,
        max_value=10,
        required=True,
        widget=NumberInput(attrs={'class': 'form-control'})
    )

class EmailForm(Form):
    email = EmailField(label="enter the email address to send the results",
                       required=True,
                       widget=TextInput(
                           attrs={'class': 'form-control'}
                       ))
    

class CreateUserForm(UserCreationForm):
    email = EmailField(required=True)
    class Meta:
        model = User
        fields = {"username", "email", "password1", "password2"}

class LoginUserForm(Form):
    username = CharField()
    email = EmailField()
    password = CharField(widget=PasswordInput)

class CodeConfirmForm(Form):
    code = CharField()
