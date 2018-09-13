from bootstrap_select import BootstrapSelect
from django import forms
from easy_select2 import select2_modelform, Select2, Select2Multiple
from ams import models
from ams.models import Assets, Assign
from ams.models import GENDER


class HardwareForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Laptop'}))
    purchase_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Hardware
        fields = ('description', 'serial_number', 'brand', 'model_number', 'status', 'purchase_date',
                  'comments')


class SoftwareForm(forms.ModelForm):
    purchase_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    expiry_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Software
        fields = ('description', 'purchase_date', 'expiry_date', 'status', 'comments')


class InformationForm(forms.ModelForm):
    publish_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Information
        fields = ('description', 'published_by', 'publish_date', 'attachment')


class InfrastructureForm(forms.ModelForm):
    class Meta:
        model = models.Infrastructure
        fields = ('description', 'status', 'comments')


class StaffForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    # gender = forms.ModelChoiceField(queryset=models.Department.objects.all(), widget=Select2())

    class Meta:
        model = models.Staff
        fields = ('first_name', 'last_name', 'work_email', 'work_phone', 'home_phone', 'gender', 'residential_address',
                  'date_of_birth', 'department')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = models.Department.objects.filter(deleted=False)


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ('name', 'description', 'team_leads')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team_leads'].queryset = models.DepartmentLead.objects.filter(deleted=False)


class AssignForm(forms.ModelForm):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Assign
        fields = ('staff', 'assets', 'date_assigned')
        widgets = {'assets': Select2,
                   }

"""        
class Form(forms.Form):
    field = forms.ModelMultipleChoiceField(queryset=qs, widget=Select2Multiple(
        select2attrs={'width': 'auto'}
    ))
"""