# coding: utf-8
"""管理后台操作权限"""
from rest_framework import permissions


class BaseOperatePermission(permissions.BasePermission):
    """基础操作权限"""
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

    def operate_permission(self, request, view):
        if request.user.role in ['ADMIN', 'SALES']:
            return True
        else:
            return False

    def has_permission(self, request, view):
        if self.operate_permission(request, view):
            return True
        return False


class CreateCouponOperatePermission(BaseOperatePermission):
    """创建优惠券操作权限"""

    def operate_permission(self, request, view):
        if request.user.role in ['ADMIN', 'FINANCE']:
            return True
        elif request.user.role in ['SALES'] and request.method in self.SAFE_METHODS:
            return True
        else:
            return False


class UserCouponOperatePermission(BaseOperatePermission):
    """分配优惠券操作权限"""

    def operate_permission(self, request, view):
        if request.user.role in ['ADMIN', 'SALES']:
            return True
        else:
            return False


class StudentReadOnlyPermission(BaseOperatePermission):
    """学生只读操作权限"""

    def operate_permission(self, request, view):
        if request.user.role == 'STUDENT':
            if request.method in self.SAFE_METHODS:
                return True
            else:
                return False
        else:
            return True
