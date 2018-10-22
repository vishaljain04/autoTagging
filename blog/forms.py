from django import forms
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

        #adding ids to textboxes
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     for field in self.Meta.fields:
        #         self.fields['text'].widget.attrs.update({
        #         'id': 'textfield'
        # })

# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget = forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ('username', 'password')

# class SignUpForm(forms.ModelForm):
#
#     class Meta:
#         model = SignUp
#         fields = ('Name', 'E-mail', 'Username', 'Password')
