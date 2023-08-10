#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

# pylint: disable=unused-argument, missing-function-docstring, missing-module-docstring, missing-class-docstring, too-few-public-methods, abstract-method


from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=True)
    password = serializers.CharField(allow_blank=True)

    class Meta:
        fields = ["username", "password"]
