from django import forms
from todolist_app.models import TodoList

class TaskList(forms.ModelForm):
    class Meta:
        model=TodoList
        fields=['task','done']