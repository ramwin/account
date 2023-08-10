#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

# pylint: disable=unused-argument, missing-function-docstring, missing-module-docstring, missing-class-docstring


import logging

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from . import serializers


LOGGER = logging.getLogger(__name__)
User = get_user_model()


class LoginView(GenericAPIView):
    permission_classes = []

    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(
                    username=username,
                    password=password
            )
        if not user.is_active:
            raise ValidationError({"detail": "用户名或者密码错误"})
        LOGGER.info("用户登录: %s", user)
        if not user.check_password(password):
            LOGGER.info("密码错误: %s", user)
            raise ValidationError({"detail": "用户名或者密码错误"})
        return Response({
            "detail": "登录成功",
            "token": Token.objects.get_or_create(user=user)[0].key,
        })
