from django.forms import ModelForm
from cloudinary.forms import CloudinaryJsFileField
from .models import Photo

# forms


class PhotoDirectForm(ModelForm):
    class Meta:
        model = Photo
    image = CloudinaryJsFileField(
        attrs={'style': "margin-top: 30px", 'multiple': 1},
        options={
            'tags': "directly_uploaded",
            'crop': 'limit', 'width': 1000, 'height': 1000,
            'eager': [{'crop': 'fill', 'width': 150, 'height': 100}],
        })
