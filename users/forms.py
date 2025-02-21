from django import forms
from users.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length = 20,    # 길이제한 
        min_length = 2,
        widget = forms.TextInput(
            attrs = {"placeholder":"사용자명 (2자리 이상)"},
        )
    )

    password = forms.CharField(
        min_length = 4,
        widget = forms.PasswordInput(
            attrs = {"placeholder":"비밀번호 (4자리 이상)"},
        )
    )