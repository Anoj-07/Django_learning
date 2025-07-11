from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__' # Include all fields from the Todo model
        # widgets are optional, but can be used to customize the form fields
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description' : forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'status' : forms.Select(choices=[
                ('Done', 'Done'),
                ('In Progress', 'In Progress'),
                ('Not Done', 'Not Done')
            ], 
            attrs={'class': 'form-select mb-3'}),
        }