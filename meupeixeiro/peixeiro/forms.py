from django import forms


class LoginForm(forms.Form):
    """
    Login Form.
    """
    username = forms.CharField()
    password = forms.PasswordInput()
