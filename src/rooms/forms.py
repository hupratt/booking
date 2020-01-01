from django import forms



class BookingForm(forms.Form):
    check_in = forms.DateField(required=True) 
    check_out = forms.DateField(required=True) 
    adults = forms.CharField(max_length=3, required=True)
    children = forms.CharField(max_length=3, required=True)
    rooms = forms.CharField(max_length=3, required=True)
