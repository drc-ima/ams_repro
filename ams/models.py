from django.db import models
from djangodeletes.softdeletes import SoftDeletable, SoftDeleteManager, SoftDeleteQuerySet
from django.utils import timezone
from autoslug import AutoSlugField
# Create your models here.

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


class Assets(SoftDeletable, models.Model):
    # asset_type = models.CharField(choices=ASSET_TYPE, max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(default='', blank=True)
    slug = AutoSlugField(populate_from='description', unique=True, default='')
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    staff = models.ManyToManyField('Staff', related_name='assets_staff', through='Assign')
    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-date_added']


class Hardware(Assets):
    # Hardware Fields
    serial_number = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    model_number = models.CharField(max_length=100, null=True, blank=True)
    purchase_date = models.DateField(default='', blank=True)


class Software(Assets):
    # Software Field
    purchase_date = models.DateField(default='', blank=True)
    expiry_date = models.DateField(default='', blank=True)


class Information(Assets):
    # Information Field
    attachment = models.FileField(blank=True)
    published_by = models.ForeignKey('Staff', related_name='publisher_staff', on_delete=models.SET_NULL, blank=True,
                                     null=True)
    publish_date = models.DateField(default='', blank=True)


class Infrastructure(Assets):
    pass


class Staff(SoftDeletable, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    work_email = models.EmailField()
    work_phone = models.CharField(max_length=100, null=True, blank=True)
    home_phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=100)
    residential_address = models.CharField(max_length=255, default='', blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    department = models.ForeignKey('Department', related_name='staff_department', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    slug = AutoSlugField(populate_from='first_name', unique=True, default='')
    asset = models.ManyToManyField(Assets, related_name='staff_assets', through='Assign')

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = 'Staff'
        ordering = ['-date_added']


class Assign(SoftDeletable, models.Model):
    staff = models.ForeignKey(Staff, related_name='staff_assign', on_delete=models.SET_NULL, null=True)
    assets = models.ForeignKey(Assets, related_name='assets_assign', on_delete=models.SET_NULL, null=True)
    date_assigned = models.DateField(default=timezone.now)
    added_date = models.DateTimeField(default=timezone.now, editable=False)

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return str(self.assets) + ' is assigned to ' + str(self.staff)

    class Meta:
        verbose_name_plural = 'Assign'
        ordering = ['-added_date']


class DepartmentLead(SoftDeletable, models.Model):
    staff = models.ForeignKey(Staff, related_name='team_lead', on_delete=models.SET_NULL, null=True)
    lead_start_date = models.DateField(default=timezone.now, blank=True, null=True)
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
    staff = models.ManyToManyField(Staff, related_name='department_staff')

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-added_date']


class Owner(SoftDeletable, models.Model):
    department_lead = models.ForeignKey(DepartmentLead, related_name='department_owner', on_delete=models.SET_NULL,
                                        null=True)
    assets = models.ForeignKey(Assets, related_name='assets_owner', on_delete=models.SET_NULL, null=True)
    date_assigned = models.DateField(default=timezone.now)
    added_date = models.DateTimeField(default=timezone.now, editable=False)

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)

    def __str__(self):
        return str(self.assets) + ' is owned to ' + str(self.department_lead)

    class Meta:
        verbose_name_plural = 'Asset Owners'
        ordering = ['-added_date']
