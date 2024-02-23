from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField()

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    add_date = forms.DateField()
    image = forms.ImageField()