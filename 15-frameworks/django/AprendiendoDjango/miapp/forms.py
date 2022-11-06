from django import forms
from django.core import validators


class FormArticle(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={  # html attributes
                'placeholder': 'Mete el titulo',
                'class': 'title_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$', 'El titulo esta mal formado', 'invalid_title')
            # validation characters
        ]
    )

    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(50, 'Te has pasado, has puesto mucho texto')
        ]
    )
    content.widget.attrs.update({  # html attributes
        'placeholder': 'Mete el contenido',
        'class': 'content_form_article',
        'id': 'contenido_form'
    })

    public_options = [
        (1, 'si'), (0, 'no')
    ]
    public = forms.TypedChoiceField(
        choices=public_options,
        label='¿Publicado?'
    )
