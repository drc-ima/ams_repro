# from itertools import chain

# from bootstrap_select import BootstrapSelect
from django import forms
# from easy_select2 import select2_modelform, Select2, Select2Multiple
from ams import models
# from ams.views import department
# from ams.models import Assets, Assign
# from ams.models import GENDER


class HardwareForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Laptop'}))
    serial_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. B89474'}))
    brand = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. HP'}))
    model_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. 89755467854'}))
    status = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. functional'}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Any comments?'}))
    purchase_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Hardware
        fields = ('description', 'serial_number', 'brand', 'model_number', 'status', 'purchase_date',
                  'comments')


class SoftwareForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. SoapUI'}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Any comments?'}))
    purchase_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    expiry_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Software
        fields = ('description', 'purchase_date', 'expiry_date', 'status', 'comments')


class InformationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Contract Between Akaditi and '
                                                                               'Pentium Tech'}))
    status = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. updated'}))
    publish_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Information
        fields = ('description', 'published_by', 'publish_date', 'file_type', 'status')


class InfrastructureForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Red Table'}))
    status = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Not Broken'}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'any comment?'}))

    class Meta:
        model = models.Infrastructure
        fields = ('description', 'status', 'comments')


class StaffForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Victor'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Amoah'}))
    work_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'eg. email@example.com'}))
    work_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. 024 456 4789'}))
    residential_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Hse No 63/1 WL Kasoa,'
                                                                                       ' Central Region'}))
    home_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. 024 456 4789'}))
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
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. We train people to be agile'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'eg. Services'}))

    class Meta:
        model = models.Department
        fields = ('name', 'description', 'team_leads')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['team_leads'].queryset = models.DepartmentLead.objects.filter(deleted=False)


class HardwareAssignForm(forms.ModelForm, forms.SelectMultiple):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    # assets = forms.ChoiceField(widget=forms.SelectMultiple)

    class Meta:
        model = models.HardwareAssign
        fields = ('staff', 'assets', 'date_assigned')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets'].queryset = models.Hardware.objects.filter(deleted=False)
        self.fields['staff'].queryset = models.Staff.objects.filter(deleted=False)


class HardwareApproveForm(forms.ModelForm):
    approve = forms.BooleanField(required=True, label='Check to confirm this!', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = models.HardwareAssign
        fields = ('approve', )


class HardwareOwnerForm(forms.ModelForm, forms.SelectMultiple):
    # date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    # assets = forms.ChoiceField(widget=forms.SelectMultiple)

    class Meta:
        model = models.HardwareOwner
        fields = ('department_lead', 'assets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets'].queryset = models.Hardware.objects.filter(deleted=False)
        self.fields['department_lead'].queryset = models.DepartmentLead.objects.all()


class SoftwareAssignForm(forms.ModelForm):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.SoftwareAssign
        fields = ('staff', 'assets', 'date_assigned')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets'].queryset = models.Software.objects.filter(deleted=False)
        self.fields['staff'].queryset = models.Staff.objects.filter(deleted=False)


class SoftwareApproveForm(forms.ModelForm):
    approve = forms.BooleanField(required=True, label='Check to confirm this!', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = models.SoftwareAssign
        fields = ('approve', )


class SoftwareOwnerForm(forms.ModelForm, forms.SelectMultiple):
    # date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    # assets = forms.ChoiceField(widget=forms.SelectMultiple)

    class Meta:
        model = models.SoftwareOwner
        fields = ('department_lead', 'assets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets'].queryset = models.Software.objects.filter(deleted=False)
        self.fields['department_lead'].queryset = models.DepartmentLead.objects.all()


class InformationAssignForm(forms.ModelForm):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.InformationAssign
        fields = ('staff', 'assets', 'date_assigned')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets'].queryset = models.Information.objects.filter(deleted=False)
        self.fields['staff'].queryset = models.Staff.objects.filter(deleted=False)


class InformationApproveForm(forms.ModelForm):
    approve = forms.BooleanField(required=True, label='Check to confirm this!', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = models.InformationAssign
        fields = ('approve', )


class InformationOwnerForm(forms.ModelForm, forms.SelectMultiple):
    # date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    # assets = forms.ChoiceField(widget=forms.SelectMultiple)

    class Meta:
        model = models.InformationOwner
        fields = ('department_lead', 'assets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets'].queryset = models.Information.objects.filter(deleted=False)
        self.fields['department_lead'].queryset = models.DepartmentLead.objects.all()


class InfrastructureAssignForm(forms.ModelForm):
    date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.InfrastructureAssign
        fields = ('staff', 'assets', 'date_assigned')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets'].queryset = models.Infrastructure.objects.filter(deleted=False)
        self.fields['staff'].queryset = models.Staff.objects.filter(deleted=False)


class InfrastructureApproveForm(forms.ModelForm):
    approve = forms.BooleanField(required=True, label='Check to confirm this!', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = models.InfrastructureAssign
        fields = ('approve', )


class InfrastructureOwnerForm(forms.ModelForm, forms.SelectMultiple):
    # date_assigned = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    # assets = forms.ChoiceField(widget=forms.SelectMultiple)

    class Meta:
        model = models.InfrastructureOwner
        fields = ('department_lead', 'assets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets'].queryset = models.Infrastructure.objects.filter(deleted=False)
        self.fields['department_lead'].queryset = models.DepartmentLead.objects.all()


class DepartmentLeadForm(forms.ModelForm):
    lead_start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.DepartmentLead
        fields = ('staff', 'lead_start_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        already_a_lead = models.Staff.objects.filter(deleted=False)
        self.fields['staff'].queryset = already_a_lead
        self.fields['staff'].queryset = models.Staff.objects.filter(deleted=False)
