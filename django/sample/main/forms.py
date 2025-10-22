from django.forms import ModelForm
from main.models import profile
class personform(ModelForm):
    class Meta:
        model=profile
        fields='__all__'