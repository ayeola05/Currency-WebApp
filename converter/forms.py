from django import forms

# from .models import

class UserInputForm(forms.Form):
    currency1= forms.CharField(max_length= 250,label="Enter the currency you want to convert")
    currency2 = forms.CharField(max_length=250, label="Enter the currency you want to convert to")
    value= forms.FloatField( label="Enter the Value")
