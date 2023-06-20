# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-16 23:36                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : views.py                                                          =
#    @Program: website5                                                        =
# ==============================================================================
import os

from django.http import HttpResponseRedirect
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from appstore.conf import settings
from appstore.models import App, AppVersion
from appstore.serializers import AppCreateSerializer, AppSerializer, AppVersionCreateSerializer, AppVersionSerializer


class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    queryset = App.objects.all()
    permission_classes = settings.permissions.app
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'create':
            return AppCreateSerializer
        elif self.action == 'version_create':
            return AppVersionCreateSerializer
        elif self.action == 'latest':
            return AppVersionSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = settings.permissions.app_create
        elif self.action == "version_create":
            self.permission_classes = settings.permissions.app_version_create
        return super().get_permissions()

    def get_instance(self):
        return self.request.user

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        app = serializer.save()
        return Response(
            status=status.HTTP_200_OK, data={
                'app_id': app.id
            }
        )

    @action(methods=['post'], detail=False)
    def version_create(self, request, *args, **kwargs):
        user = self.get_instance()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        app = App.objects.get(id=data['app_id'])
        installer = data['installer']
        ext = os.path.splitext(installer.name)[1]
        installer.name = f"{app.name}-{data['version_name']}{ext}"
        version = AppVersion.objects.create(
            app=app,
            version_name=data['version_name'],
            version_code=data['version_code'],
            updates=data['updates'],
            is_force=data['is_force'] == 'true',
            author=user,
            installer=installer,
        )
        url = request.build_absolute_uri(version.installer.url)
        return Response(
            status=status.HTTP_200_OK, data={'installer': url, 'apk': url}
        )

    @action(methods=['get'], detail=True)
    def latest(self, request, *args, **kwargs):
        app = self.get_object()
        latest = self.get_serializer(instance=app.versions.all().first())
        data = latest.data
        VersionCode = request.query_params.get('VersionCode')
        if VersionCode:
            data["updates"] = ""
            for version in app.versions.filter(version_code__gt=VersionCode):
                if version.is_force:
                    data["is_force"] = True
                data["updates"] += f"# {version.version_name}\n{version.updates}\n"

        return Response(status=status.HTTP_200_OK, data=data)

    @action(methods=['get'], detail=True)
    def get_latest_installer(self, request, *args, **kwargs):
        app = self.get_object()
        latest = app.versions.all().first()
        # resp = FileResponse(latest.installer, as_attachment=True)
        # resp.headers["Access-Control-Expose-Headers"] = 'Content-Disposition'
        url = request.build_absolute_uri(latest.installer.url)
        return HttpResponseRedirect(url)

    @action(methods=['get'], detail=True)
    def get_latest_apk(self, *args, **kwargs):
        """由于历史原因，保留该函数"""
        return self.get_latest_installer(*args, **kwargs)
