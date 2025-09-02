from django import forms
from django.forms import BooleanField


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class AppointmentForm(StyleFormMixin, forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ваше ФИО'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Ваша электронная почта'})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона'})
    )
    msg_subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Тема'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 8, 'placeholder': 'Описание случая'})
    )