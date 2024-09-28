from django import forms
from .models import Reservation 
from . models import Customer


# class ReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['name', 'email', 'date', 'time', 'guests', 'message']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'guests', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name','style': 'font-size: 18px;' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder': 'Your Email','style': 'font-size: 18px;'}),
            'date': forms.DateInput(attrs={ 'class': 'form-control',  'type': 'date', 'placeholder': 'Reservation Date'}),
            'time': forms.TimeInput(attrs={  'class': 'form-control', 'type': 'time', 'placeholder': 'Reservation Time'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Number of Guests'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any Special Requests', 'rows': 4 }),
        }


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=['name','village','city','mobile','state','pincode']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'village':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'pincode':forms.NumberInput(attrs={'class':'form-control'}),
        }