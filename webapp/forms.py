# webapp/forms.py

from django import forms

class ImageUploadForm(forms.Form):
    original_image = forms.ImageField(label='Select Original Image')
