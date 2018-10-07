# from itertools import chain

# from bootstrap_select import BootstrapSelect
from django import forms
# from easy_select2 import select2_modelform, Select2, Select2Multiple
from ams import models
# from ams.views import department
# from ams.models import Assets, Assign
# from ams.models import GENDER
from ams_project import settings


class HardwareForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Laptop'}))
    purchase_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Hardware
        fields = ('description', 'serial_number', 'brand', 'model_number', 'status', 'purchase_date',
                  'comments')


class SoftwareForm(forms.ModelForm):
    purchase_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),
                                    input_formats=settings.DATE_INPUT_FORMATS)
    expiry_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Software
        fields = ('description', 'purchase_date', 'expiry_date', 'status', 'comments')


class InformationForm(forms.ModelForm):
    publish_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Information
        fields = ('description', 'published_by', 'publish_date', 'attachment', 'status')


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


"""
class AssignForm(forms.ModelForm):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Assign
        fields = ('staff', 'assets', 'date_assigned')
"""


class HardwareAssignForm(forms.ModelForm):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.HardwareAssign
        fields = ('staff', 'assets', 'date_assigned')


class SoftwareAssignForm(forms.ModelForm):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.SoftwareAssign
        fields = ('staff', 'assets', 'date_assigned')


class InformationAssignForm(forms.ModelForm):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.InformationAssign
        fields = ('staff', 'assets', 'date_assigned')


class InfrastructureAssignForm(forms.ModelForm):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.InfrastructureAssign
        fields = ('staff', 'assets', 'date_assigned')


class DepartmentLeadForm(forms.ModelForm):
    lead_start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.DepartmentLead
        fields = ('staff', 'lead_start_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['staff'].queryset = models.Staff.objects.filter(deleted=False)


"""        
class Form(forms.Form):
    field = forms.ModelMultipleChoiceField(queryset=qs, widget=Select2Multiple(
        select2attrs={'width': 'auto'}
    ))
"""