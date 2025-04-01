from django import forms
from practice_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tags": forms.SelectMultiple(),
        }
