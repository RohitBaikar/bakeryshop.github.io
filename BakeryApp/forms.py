from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from . models import Products , ContactUs , CategoryModel

class RegisterForm(UserCreationForm):

    address = forms.CharField(label='Enter address',widget=forms.TextInput(attrs={'class':'form-control'}))

    contact = forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','address','contact','password1','password2']

        labels = {'username':'Enter Username','first_name':'First Name','last_name':'Last Name','email':'Email-ID','password1':'Enter Password','password2':'Confirm Password'}

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            
            # 'Qua':forms.Select(attrs={'class':'form-control'}),
        }




class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Enter Username',widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))



class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['img_title','details', 'image','price', 'cat','Qua']

        labels = {
            'img_title': 'Enter Image Title',
            'details':'Enter Product Details',
            'image': 'Upload Image',
            'price':'Product Price',
            'cat': 'Select Category',
            'Qua':'Enter Quantity',
        }

        widgets = {
            'img_title':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'cat':forms.Select(attrs={'class':'form-control'}),
            # 'Qua':forms.Select(attrs={'class':'form-control'}),
            
        }

class ContactForm(forms.ModelForm):

    contact = forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = ContactUs
        fields = ['name','email','contact','help']

        labels = {
            'name':'Enter Name',
            'email':'Email-ID',
            'contact':'Contact',
            'help':'How i help you'
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            # 'contact':forms.TextInput(attrs={'class':'form-control'}),
            'help':forms.Textarea(attrs={'class':'form-control'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['title']

        label = {
            'title':'Enter New Category'

        }

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
        }

