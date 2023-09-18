from django import forms


class Wanafunzi(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=30)
    lastname = forms.CharField(label="Enter last name", max_length=30)
    emailaddress = forms.EmailField(label="Enter email address", max_length=30)
    Upload_pic = forms.FileField()
