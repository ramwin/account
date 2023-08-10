#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", views.LoginView.as_view(), name="login"),
]
