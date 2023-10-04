from django import forms
from .models import UserData,PostData


class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['First_Name','Last_Name','UserName', 'EmailId' ,'Password','Confirm_Password']
        
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model=PostData
        fields=['Post','UserName']        