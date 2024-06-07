from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "country", "imagen", "birth_date"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apelldio",
            "country": "Pais",
            "imagen": "Imagen de Perfil",
            "birth_date": "Fecha de nacimiento",
        }
        help_texts = {
            "birth_date": " \n Formato de fecha: \n AAAA-MM-DD (ej, 2024-06-07)",
        }
