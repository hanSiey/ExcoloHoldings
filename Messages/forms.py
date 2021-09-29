from django import forms
from .models import GetQuote, ContactMessage

class Quote(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'booking-name', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'booking-name', 
            'type': 'text',
            'name': 'surname',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-input',
            'id': 'booking-name', 
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Required',
        }
    ))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'booking-name', 
            'type': 'text',
            'name': 'phone',
            'data-constraints': '@Numeric',
        }
    ))
    class Meta:
        model = GetQuote
        fields = '__all__'

class Message(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-name', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-email', 
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
        }
    ))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-phone', 
            'type': 'text',
            'name': 'phone',
            'data-constraints': '@Numeric',
        }
    ))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs = {
            'class': 'form-input',
            'id': 'contact-message', 
            'type': 'text',
            'name': 'message',
            'data-constraints': '@Required',
        }
    ))
    class Meta:
        model = ContactMessage
        fields = '__all__'