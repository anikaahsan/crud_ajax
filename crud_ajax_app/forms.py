from django import forms 

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['name','address','phone_number']
        widgets={
            'name':forms.TextInput(attrs={'id':'nameid'}),
            'address':forms.Textarea(attrs={'id':'addressid'}),
            'phone_number':forms.TextInput(attrs={'id':'phoneid'})
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control form-inline'   