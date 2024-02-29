from django.forms import ModelForm

from .models import UsersModel


class UserForm(ModelForm):
    class Meta:
        model = UsersModel
        fields = "__all__"
        exclude = ["", ""]
