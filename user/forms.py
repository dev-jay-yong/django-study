from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Please enter your email address'
        },
        max_length=64,
        label='Email Address'
    )

    password = forms.CharField(
        error_messages={
           'required': 'Please enter your password'
        },
        widget=forms.PasswordInput,
        label='Password'
    )

    re_password = forms.CharField(
        error_messages={
           'required': 'Please re-enter your password'
        },
        widget=forms.PasswordInput,
        label='Retyped Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        print(re_password)
        print(password)

        if password and re_password and password != re_password:
            self.add_error('password', 'Passwords do not match')
