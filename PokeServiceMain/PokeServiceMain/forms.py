from django.forms import ModelForm, Form, IntegerField, NumberInput


class BattleForm(Form):
    user_roll = IntegerField(
        label='Choose number 1..10',
        min_value=1,
        max_value=10,
        required=True,
        widget=NumberInput(attrs={'class': 'form-control'})
    )