# coding:utf-8
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions, status
from rest_framework.compat import set_rollback
from rest_framework.response import Response


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait
        detail = exc.detail
        field_name = ''
        while isinstance(detail, dict):
            field_name = next(iter(detail.keys()))
            detail = detail[field_name]
        if isinstance(detail, list):
            detail = detail[0]
        err_data = {
            'code': exc.code if hasattr(exc, 'code') else exc.status_code,
            'msg': exc.msg if hasattr(exc, 'msg') else detail,
            'field_name': field_name
        }

        set_rollback()
        return Response(err_data, status=200, headers=headers)

    elif isinstance(exc, Http404):
        set_rollback()
        err_data = {
            'code': 404,
            'msg': '请求失败'
        }
        return Response(err_data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        err_data = {
            'code': 403,
            'msg': '请求失败'
        }
        set_rollback()
        return Response(err_data, status=status.HTTP_403_FORBIDDEN)

