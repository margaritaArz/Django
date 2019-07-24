from django.contrib.auth.forms import UserCreationForm
from authapp.models import ShopUser
from django.forms import forms


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar', 'email')

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field_name, field in self.fiel.items():
            field.widget.attrs['class'] = 'format-control'
            field.help_text = ''
            #if field_name == 'password1' or 'password2':
                #field.widget = forms.HiddenInput()

    def clear_age(self):
        data = self.cleaned_data['age']
        if data > 18:
            raise forms.ValidationError("Вход +18!")

        return data
