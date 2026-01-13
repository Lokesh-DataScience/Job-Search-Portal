from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply consistent widget classes/placeholders for styling
        self.fields['username'].widget.attrs.update({'class':'auth-input', 'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class':'auth-input', 'placeholder':'Email address'})
        self.fields['password1'].widget.attrs.update({'class':'auth-input', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'auth-input', 'placeholder':'Confirm password'})
        # Remove strict Django help text and validators for demo simplicity
        self.fields['password1'].help_text = ''

    def clean_password2(self):
        """Relaxed validation for demo: only check match and minimal length (>=3)."""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        if password1 and len(password1) < 3:
            raise forms.ValidationError("Password must be at least 3 characters long")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user