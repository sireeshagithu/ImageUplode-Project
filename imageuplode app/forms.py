from django import forms
from imageuplodeapp.models import ImageUplodeModel

class ImageUplodeForm(forms.ModelForm):
    class Meta:
        model = ImageUplodeModel
        fields = '__all__'
