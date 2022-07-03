from django import forms
class CmdForm(forms.Form):
        username = forms.CharField(label='Username')
        password = forms.CharField(widget=forms.PasswordInput())
        ip1 = forms.CharField(label='Ip Address of Router 1')
        ip2 = forms.CharField(label='Ip Address of Router 2')