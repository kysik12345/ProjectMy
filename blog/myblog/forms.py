from django import forms
from .models import Post


#class PostForm(forms.Form):
    #author = forms.CharField(max_length=50, label="Автор")
    #title = forms.CharField(max_length=20, label="Заголовок")
    #text = forms.CharField(label='Текст поста', widget=forms.Textarea)

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        author = kwargs.pop('author', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if author:
            self.fields['author'].initail = author
            self.fields['author'].disadled = True

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'image']