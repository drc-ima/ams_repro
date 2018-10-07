from django.urls import path
from ams.views import assets, hardware, software, information, infrastructure, staff, department, setting

app_name = 'ams'


urlpatterns = [
    # path('assets/assign/', assets.Assign.as_view(), name='assign-assets'),
    path('assets/list', assets.List.as_view(), name='assets-list'),
    # path('assets/assign/', assets.Assign.as_view(), name='asset-assign'),
    # path('assets/archive/<str:slug>/', assets.Archive.as_view(), name='assets-archive'),

    # hardware
    # path('assets/hardware/list/', hardware.List.as_view(), name='assets-hardware-list'),
    path('assets/hardware/add/', hardware.Add.as_view(), name='assets-hardware-add'),
    path('assets/hardware/update/<str:slug>/', hardware.Update.as_view(), name='assets-hardware-update'),
    path('assets/hardware/detail/<str:slug>/', hardware.Detail.as_view(), name='assets-hardware-detail'),
    path('assets/hardware/archive/<str:slug>/', hardware.Archive.as_view(), name='assets-hardware-archive'),
    path('assets/hardware/restore/<str:slug>/', hardware.Restore.as_view(), name='assets-hardware-restore'),
    # path('assets/hardware/archive/', hardware.ArchiveList.as_view(), name='assets-hardware-archive'),
    path('assets/hardware/assign/', hardware.Assign.as_view(), name='assign-hardware'),

    # software urls
    path('assets/software/add/', software.Add.as_view(), name='assets-software-add'),
    # path('assets/software/list/', software.List.as_view(), name='assets-software-list'),
    path('assets/software/update/<str:slug>/', software.Update.as_view(), name='assets-software-update'),
    path('assets/software/detail/<str:slug>/', software.Detail.as_view(), name='assets-software-detail'),
    path('assets/hardware/restore/<str:slug>/', software.Restore.as_view(), name='assets-software-restore'),
    path('assets/software/archive/<str:slug>/', software.Archive.as_view(), name='assets-software-archive'),
    # path('assets/software/archive/', software.ArchiveList.as_view(), name='assets-software-archive'),
    path('assets/software/assign/', software.Assign.as_view(), name='assign-software'),

    # information urls
    path('assets/information/add/', information.Add.as_view(), name='assets-information-add'),
    # path('assets/information/list/', information.List.as_view(), name='assets-information-list'),
    path('assets/information/update/<str:slug>/', information.Update.as_view(), name='assets-information-update'),
    path('assets/information/detail/<str:slug>/', information.Detail.as_view(), name='assets-information-detail'),
    path('assets/information/archive/<str:slug>/', information.Archive.as_view(), name='assets-information-archive'),
    path('assets/information/assign/', information.Assign.as_view(), name='assign-information'),
    path('assets/information/restore/<str:slug>/', information.Restore.as_view(), name='assets-information-restore'),
    # path('assets/information/archive/', information.ArchiveList.as_view(), name='assets-information-archive'),

    # infrastructure urls
    path('assets/infrastructure/add/', infrastructure.Add.as_view(), name='assets-infrastructure-add'),
    # path('assets/infrastructure/list/', infrastructure.List.as_view(), name='assets-infrastructure-list'),
    path('assets/infrastructure/update/<str:slug>/', infrastructure.Update.as_view(),
         name='assets-infrastructure-update'),
    path('assets/infrastructure/detail/<str:slug>/', infrastructure.Detail.as_view(),
         name='assets-infrastructure-detail'),
    path('assets/infrastructure/assign/', infrastructure.Assign.as_view(), name='assign-infrastructure'),
    path('assets/infrastructure/restore/<str:slug>/', infrastructure.Restore.as_view(),
         name='assets-infrastructure-restore'),
    path('assets/infrastructure/archive/<str:slug>/', infrastructure.Archive.as_view(),
         name='assets-infrastructure-archive'),
    # path('assets/infrastructure/archive/', infrastructure.ArchiveList.as_view(),
    # name='assets-infrastructure-archive'),

    # staff urls
    path('staff/add/', staff.Add.as_view(), name='staff-add'),
    path('staff/list/', staff.List.as_view(), name='staff-list'),
    path('staff/update/<str:slug>/', staff.Update.as_view(), name='staff-update'),
    path('staff/detail/<str:slug>/', staff.Detail.as_view(), name='staff-detail'),
    path('staff/archive/detail/<str:slug>/', staff.ArchiveDetail.as_view(), name='staff-archive-detail' ),
    path('staff/archive/<str:slug>/', staff.Archive.as_view(), name='staff-archive'),
    path('assets/staff/restore/<str:slug>/', staff.Restore.as_view(), name='staff-restore'),
    # path('staff/archive/', staff.ArchiveList.as_view(), name='staff-archive-list'),

    # department urls
    path('department/add/', department.Add.as_view(), name='department-add'),
    path('department/list/', department.List.as_view(), name='department-list'),
    path('department/update/<str:slug>/', department.Update.as_view(), name='department-update'),
    path('department/detail/<str:slug>/', department.Detail.as_view(), name='department-detail'),
    path('department/delete/<str:slug>/', department.Delete.as_view(), name='department-delete'),
    path('department/archive/list', department.ArchiveList.as_view(), name='department-archive-list'),
    path('department/lead/add/', department.AddLead.as_view(), name='department-lead-add'),
    path('department/archive/detail/<str:slug>/', department.ArchiveDetail.as_view(), name='department-archive-detail'),
    path('assets/staff/restore/<str:slug>/', department.Restore.as_view(), name='department-restore'),

    # settings urls
    path('settings/', setting.Details.as_view(), name='settings'),

]
