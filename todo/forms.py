from django.forms import ModelForm, Form, BooleanField

from .models import Todo


class TodoModelForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

class DeleteConfirmForm(Form):
    check = BooleanField(label='Are you shall?')