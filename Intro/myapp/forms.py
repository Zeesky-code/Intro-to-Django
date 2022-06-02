from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(label='Title', max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label = 'Subject Description',max_length = 200, widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length = 50, widget=forms.TextInput(attrs={'class': 'username'}))
    password = forms.CharField(label='Password', max_length = 50, widget=forms.TextInput(attrs={'class': 'password'}))