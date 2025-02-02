# forms.py
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'input input-bordered w-full'})
    )
    user_type = forms.ChoiceField(
        choices=[('DOCTOR', 'Doctor'), ('PATIENT', 'Patient')],
        widget=forms.Select(attrs={'class': 'select select-bordered w-full'})
    )
    phone_number = forms.IntegerField(
        # max_length=15, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'input input-bordered w-full'})
    )
    password1 = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'user_type', 'phone_number', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user
        

class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input input-bordered w-full'})
    ) 
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)
        self.fields['password'] = forms.CharField(
            label="Password",
            strip=False,
            widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class': 'input input-bordered w-full'})
        )
        
class CustomAdminUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True
    )
    user_type = forms.ChoiceField(
        choices=[('ADMIN', 'Admin'), ('DOCTOR', 'Doctor'), ('PATIENT', 'Patient')]
    )
    phone_number = forms.IntegerField(
        # max_length=15, 
        required=True
    )
    password1 = forms.CharField(
        label='Enter Password'
    )
    password2 = forms.CharField(
        label='Confirm Password'
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'user_type', 'phone_number', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user