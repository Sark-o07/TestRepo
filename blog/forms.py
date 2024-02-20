from django import forms
from .models import PostModel, Comment, CategoryModel


choice_list = [(None, 'None')]  # Add a None option
choice_list += list(CategoryModel.objects.all().values_list('name', 'name'))

class PostModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False

    class Meta:
        model = PostModel
        fields = ('title', 'content', 'category')

        widgets = {
            'content': forms.Textarea(attrs={'rows': 8, 'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }
 
        
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add comments here...'}))
    class Meta:
        model = Comment
        fields = ('content',)