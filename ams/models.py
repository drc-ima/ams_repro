# from itertools import chain
from django.contrib.auth.models import User
from django.db import models
# from softdelete.models import SoftDeleteObject, SoftDeleteManager, SoftDeleteQuerySet
# from django.urls import reverse
from django.urls import reverse
from django.utils import timezone
from autoslug import AutoSlugField
# from soft_delete_it.models import SoftDeleteModel, SoftDeleteManager, SoftDeleteQuerySet
from djangodeletes.softdeletes import SoftDeletable, SoftDeleteManager, SoftDeleteQuerySet
# Create your models here.
# from ams_project import settings
from users.models import UserProfile

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

ASSET_TYPE = [
    ('Hardware', 'Hardware'),
    ('Information', 'Information'),
    ('Infrastructure', 'Infrastructure'),
    ('Software', 'Software'),
]


class Hardware(SoftDeletable, models.Model):
    image = models.ImageField(upload_to='hard_photo', blank=True)
    asset_type = models.CharField(default='Hardware', max_length=100, editable=False)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(default='', blank=True)
    # Hardware Fields
    serial_number = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    model_number = models.CharField(max_length=100, null=True, blank=True)
    purchase_date = models.DateField(default='', blank=True)
    slug = AutoSlugField(populate_from='description', unique=True, default='')
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    added_by = models.ForeignKey(User, related_name='hardware_admin', on_delete=models.SET_NULL, null=True)
    staff = models.ManyToManyField('Staff', related_name='assets_hardware_staff', through='HardwareAssign')

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-date_added']
        get_latest_by = ['date_added']


FILE_TYPE = [
    ('doc', 'doc'),
    ('docx', 'docx'),
    ('xls', 'xls'),
    ('pptx', 'pptx'),
    ('others', 'others'),
]


class Information(SoftDeletable, models.Model):
    asset_type = models.CharField(default='Information', max_length=100, editable=False)
    added_by = models.ForeignKey(User, related_name='information_admin', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(default='', blank=True)
    # Information Fields
    file_type = models.CharField(choices=FILE_TYPE, max_length=255, blank=True)
    published_by = models.ForeignKey('Staff', related_name='publisher_staff', on_delete=models.SET_NULL, blank=True,
                                     null=True)
    publish_date = models.DateField(default='', blank=True)
    slug = AutoSlugField(populate_from='description', unique=True, default='')
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    staff = models.ManyToManyField('Staff', related_name='assets_information_staff', through='InformationAssign')

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-date_added']
        get_latest_by = ['date_added']


class Infrastructure(SoftDeletable, models.Model):
    image = models.ImageField(upload_to='infras_photo', blank=True)
    asset_type = models.CharField(default='Infrastructure', max_length=100)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(default='', blank=True)
    slug = AutoSlugField(populate_from='description', unique=True, default='')
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    added_by = models.ForeignKey(User, related_name='infrastructure_admin', on_delete=models.SET_NULL, null=True)
    staff = models.ManyToManyField('Staff', related_name='assets_infrastructure_staff', through='InfrastructureAssign')

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-date_added']
        get_latest_by = ['date_added']


SOFTWARE_TYPE = [
    ('Licensed', 'Licensed'),
    ('Unlicensed', 'Unlicensed'),
    ('Expired', 'Expired'),
]


class Software(SoftDeletable, models.Model):
    image = models.ImageField(upload_to='soft_photo', blank=True)
    asset_type = models.CharField(default='Software', max_length=100, editable=False)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=SOFTWARE_TYPE, max_length=255, blank=True)
    comments = models.TextField(default='', blank=True)
    # Software Fields
    purchase_date = models.DateField(default='', blank=True)
    expiry_date = models.DateField(default='', blank=True)
    slug = AutoSlugField(populate_from='description', unique=True, default='')
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    added_by = models.ForeignKey(User, related_name='software_admin', on_delete=models.SET_NULL, null=True)
    staff = models.ManyToManyField('Staff', related_name='assets_software_staff', through='SoftwareAssign')

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-date_added']
        get_latest_by = ['date_added']


class Staff(SoftDeletable, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    work_email = models.EmailField()
    work_phone = models.CharField(max_length=100, null=True, blank=True)
    home_phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=100)
    residential_address = models.CharField(max_length=255, default='', blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    department = models.ManyToManyField('Department', related_name='staff_department', through='Allocation')
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    slug = AutoSlugField(populate_from='first_name', unique=True, default='')
    hardware_asset = models.ManyToManyField(Hardware, related_name='staff_hardware', through='HardwareAssign')
    information_asset = models.ManyToManyField(Information, related_name='staff_information',
                                               through='InformationAssign')
    infrastructure_asset = models.ManyToManyField(Infrastructure, related_name='staff_infrastructure',
                                                  through='InfrastructureAssign')
    software_asset = models.ManyToManyField(Software, related_name='staff_software', through='SoftwareAssign')

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    def full_name(self):
        return '''{} {}'''.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = 'Staff'
        ordering = ['-date_added']
        get_latest_by = ['date_added']


class Approve(models.Model):
    approve = models.BooleanField(default=False)
    approve_date = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        abstract = True

    def _approve(self):
        self.approve = True
        self.approve_date = timezone.now()
        self.save()


class Return(models.Model):
    return_it = models.BooleanField(default=False)
    return_on = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        abstract = True


class HardwareAssign(Approve, Return, models.Model):
    assign_by = models.ForeignKey(User, related_name='hardware_assign_by', on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey(Staff, related_name='staff_hardware_assign', on_delete=models.SET_NULL, null=True)
    assets = models.ForeignKey(Hardware, related_name='hardware_assign', on_delete=models.SET_NULL, null=True)
    date_assigned = models.DateField(default=timezone.now)
    added_date = models.DateTimeField(default=timezone.now, editable=False)
    slug = AutoSlugField(populate_from='assets', unique=True, default='')

    def __str__(self):
        return str(self.assets) + ' is assigned to ' + str(self.staff)

    class Meta:
        verbose_name = 'Hardware Assignment'
        verbose_name_plural = 'Hardware Assignments'
        ordering = ['-added_date']


class InformationAssign(Approve, Return, models.Model):
    assign_by = models.ForeignKey(User, related_name='information_assign_by', on_delete=models.SET_NULL,
                                  null=True)
    staff = models.ForeignKey(Staff, related_name='staff_information_assign', on_delete=models.SET_NULL, null=True)
    assets = models.ForeignKey(Information, related_name='information_assign', on_delete=models.SET_NULL, null=True)
    date_assigned = models.DateField(default=timezone.now)
    added_date = models.DateTimeField(default=timezone.now, editable=False)
    slug = AutoSlugField(populate_from='assets', unique=True, default='')

    def __str__(self):
        return str(self.assets) + ' is assigned to ' + str(self.staff)

    class Meta:
        verbose_name = 'Information Assignment'
        verbose_name_plural = 'Information Assignments'
        ordering = ['-added_date']


class InfrastructureAssign(Approve, Return, models.Model):
    assign_by = models.ForeignKey(User, related_name='infrastructure_assign_by', on_delete=models.SET_NULL,
                                  null=True)
    staff = models.ForeignKey(Staff, related_name='staff_infrastructure_assign', on_delete=models.SET_NULL, null=True)
    assets = models.ForeignKey(Infrastructure, related_name='infrastructure_assign', on_delete=models.SET_NULL,
                               null=True)
    date_assigned = models.DateField(default=timezone.now)
    added_date = models.DateTimeField(default=timezone.now, editable=False)
    slug = AutoSlugField(populate_from='assets', unique=True, default='')

    def __str__(self):
        return str(self.assets) + ' is assigned to ' + str(self.staff)

    class Meta:
        verbose_name = 'Infrastructure Assignment'
        verbose_name_plural = 'Infrastructure Assignments'
        ordering = ['-added_date']


class SoftwareAssign(Approve, Return, models.Model):
    assign_by = models.ForeignKey(User, related_name='software_assign_by', on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey(Staff, related_name='staff_software_assign', on_delete=models.SET_NULL, null=True)
    assets = models.ForeignKey(Software, related_name='software_assign', on_delete=models.SET_NULL, null=True)
    date_assigned = models.DateField(default=timezone.now)
    added_date = models.DateTimeField(default=timezone.now, editable=False)
    slug = AutoSlugField(populate_from='assets', unique=True, default='')

    def __str__(self):
        return str(self.assets) + ' is assigned to ' + str(self.staff)

    class Meta:
        verbose_name = 'Software Assignment'
        verbose_name_plural = 'Software Assignments'
        ordering = ['-added_date']


class DepartmentLead(SoftDeletable, models.Model):
    staff = models.ForeignKey(Staff, related_name='team_lead', on_delete=models.SET_NULL, null=True)
    lead_start_date = models.DateField(default=timezone.now, blank=True, null=True)
    is_lead = models.BooleanField(default=True, editable=False)
    added_date = models.DateTimeField(default=timezone.now, editable=False)
    slug = AutoSlugField(populate_from='staff', unique=True, default='')

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return str(self.staff)

    class Meta:
        verbose_name_plural = 'Department Leads'
        ordering = ['added_date']


class Department(SoftDeletable, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    team_leads = models.ForeignKey(DepartmentLead, related_name='team_lead', on_delete=models.SET_NULL, blank=True,
                                   null=True)
    added_date = models.DateTimeField(default=timezone.now, editable=False)
    slug = AutoSlugField(populate_from='name', unique=True, default='')
    staff = models.ManyToManyField(Staff, related_name='department_staff', through='Allocation')

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-added_date']
        get_latest_by = ['added_date']


class Allocation(models.Model):
    staff = models.ForeignKey(Staff, related_name='allocate_staff', on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, related_name='allocate_department', on_delete=models.SET_NULL, null=True)
    date_allocated = models.DateTimeField(default=timezone.now, editable=False)
    allocated_by = models.ForeignKey(User, related_name='allocated', on_delete=models.SET_NULL, null=True)


class SoftwareOwner(SoftDeletable, models.Model):
    assets = models.ForeignKey(Software, related_name='software_owner', on_delete=models.SET_NULL, null=True)
    department_lead = models.ForeignKey(DepartmentLead, related_name='department_software_owner',
                                        on_delete=models.SET_NULL, null=True)
    added_date = models.DateTimeField(default=timezone.now, editable=False)

    # objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return str(self.assets) + ' is assigned to ' + str(self.department_lead)

    class Meta:
        verbose_name = 'Software Owner'
        verbose_name_plural = 'Software Owners'
        ordering = ['-added_date']


class InfrastructureOwner(SoftDeletable, models.Model):
    assets = models.ForeignKey(Infrastructure, related_name='infrastructure_owner', on_delete=models.SET_NULL,
                               null=True)
    department_lead = models.ForeignKey(DepartmentLead, related_name='department_infrastructure_owner',
                                        on_delete=models.SET_NULL, null=True)
    added_date = models.DateTimeField(default=timezone.now, editable=False)

    # objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return str(self.assets) + ' is assigned to ' + str(self.department_lead)

    class Meta:
        verbose_name = 'Infrastructure Owner'
        verbose_name_plural = 'Infrastructure Owners'
        ordering = ['-added_date']


class InformationOwner(SoftDeletable, models.Model):
    assets = models.ForeignKey(Information, related_name='information_owner', on_delete=models.SET_NULL, null=True)
    department_lead = models.ForeignKey(DepartmentLead, related_name='department_information_owner',
                                        on_delete=models.SET_NULL, null=True)
    added_date = models.DateTimeField(default=timezone.now, editable=False)

    # objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return str(self.assets) + ' is assigned to ' + str(self.department_lead)

    class Meta:
        verbose_name = 'Information Owner'
        verbose_name_plural = 'Information Owners'
        ordering = ['-added_date']


class HardwareOwner(SoftDeletable, models.Model):
    assets = models.ForeignKey(Hardware, related_name='hardware_owner', on_delete=models.SET_NULL, null=True)
    department_lead = models.ForeignKey(DepartmentLead, related_name='department_hardware_owner',
                                        on_delete=models.SET_NULL,
                                        null=True)
    added_date = models.DateTimeField(default=timezone.now, editable=False)

    # objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return str(self.assets) + ' is assigned to ' + str(self.department_lead)

    class Meta:
        verbose_name = 'Hardware Owner'
        verbose_name_plural = 'Hardware Owners'
        ordering = ['-added_date']
