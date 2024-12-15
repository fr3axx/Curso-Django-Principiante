from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de Tarea", max_length=200)
    description = forms.CharField(label="Descripcion de la Tarea", widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200)