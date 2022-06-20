from django import forms

class EmployeeForm(forms.Form):
    emp_id=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter id"}))
    emp_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter name"}))
    designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter designation"}))
    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"enter salary"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email"}))
    experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"enter experience"}))
    def clean(self):
        cleaned_data=super().clean()
        exp=cleaned_data.get("experience")
        if exp<0:
            msg="invalid exp"
            self.add_error("experience",msg)