from django import forms
class NetForm(forms.Form):
        address = forms.CharField(label='Address',required=False)
        mask = forms.CharField(label='Wildcard Mask',required =False)
        area = forms.CharField(label='Area',required=False)