from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ваше имя',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ваш пароль',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите электронную почту',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

#
# class EditProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'price', 'image',)
#         widgets = {
#
#             'name': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'description': forms.Textarea(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'price': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'image': forms.FileInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }
#
# class ProductFilterForm(forms.Form):
#     title = forms.CharField(label='Поиск по названию', required=False)
#     # category = forms.ModelChoiceField(label='Категория',queryset=Ad.objects.values_list('category', flat=True).distinct(), required=False)
#     price_min = forms.DecimalField(label='Минимальная цена', required=False)
#     price_max = forms.DecimalField(label='Максимальная цена', required=False)