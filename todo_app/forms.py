from django.forms import ModelForm
from .models import ToDoList, ToDoItem


class ToDoListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(ToDoListForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ToDoItemForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'due_date']

    def __init__(self, *args, **kwargs):
        super(ToDoItemForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})