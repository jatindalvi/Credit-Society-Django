from django import forms
from django.contrib.auth.models import User
from .models import Account
from .models import interests


class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('accountnumber','username','name','sapid','dateofjoining','teachingstaff','nonteachingstaff','sharevalue','sharesstartingnumber','sharesendingnumber')

class NewUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','first_name','last_name','email')

class FDUpdateForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('username','fdcapital','fdmaturitydate')

class ShareUpdateForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('username','sharevalue')

class LongLoanUpdateForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('username','islongloantaken','longloanamount','longloanperiod')

class EmerLoanUpdateForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('username','isloanemertaken','emerloanamount','emerloanperiod')

class MessengerForm(forms.Form):
    fmessage=forms.CharField(widget=forms.TextInput)

class SecretkeyForm(forms.Form):
    fchairmankey=forms.IntegerField()
    fsecretarykey=forms.IntegerField()
