from django.forms import ModelForm, Form, IntegerField, NumberInput, EmailField, TextInput


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