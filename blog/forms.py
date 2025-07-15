from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
            model = Post
            fields = ['title', 'content', 'published']
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del post'}),
                'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            }
        # Validación personalizada
    def clean_title(self):
            title = self.cleaned_data['title']
            if "prohibido" in title.lower():
                raise forms.ValidationError("No se permite usar la palabra 'prohibido' en el título.")
            return title 
    
    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get("content")
        title = cleaned_data.get("title")
        if title and content and title in content:
            self.add_error("content", "El contenido no puede incluir el título literal.")