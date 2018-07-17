# -*- coding: utf-8 -*-
import json
from re import compile

import time

import datetime
from django.conf import settings
from django.http.response import HttpResponse

from authentication.models import User
from utils.mongodb import stu_db
from micro_service.service import AuthorizeServer
import logging

logging = logging.getLogger("django")

EXEMPT_URLS = []
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class AuthorizeRequiredMiddleWare(MiddlewareMixin):
    """用户认证中间件"""

    def process_request(self, request):
        logging.info('info Auth Url : %s' % request.path)
        path = request.path_info.lstrip('/')
        for m in EXEMPT_URLS:
            if m.match(path):
                return
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            ticket = request.GET.get('ticket')
        if not ticket:
            return HttpResponse(content=json.dumps(dict(code=401, msg='未登录')),
                                content_type='application/json')
        auth_res = AuthorizeServer.ticket_authorize(ticket)
        valid_ticket = auth_res['valid_ticket']
        err_msg = auth_res['err_msg']
        if not valid_ticket:
            return HttpResponse(content=json.dumps(dict(code=401, msg=err_msg)),
                                content_type='application/json')
        user = User.objects.get(id=auth_res['user_id'])
        logging.info('Get User : %s' % user.__dict__)
        request.user = user


class BackendAPIRequestMiddleWare(MiddlewareMixin):
    """管理后台接口访问限制中间件"""

    def process_request(self, request):
        path = request.path_info.lstrip('')
        if path.split('/')[1] == 'admin' and request.user.role == 'STUDENT':
            return HttpResponse(content=json.dumps(dict(code=403, msg='您没有执行该操作的权限')),
                                content_type='application/json')
        if path.split('/')[1] == 'order' and request.user.role != 'STUDENT':
            return HttpResponse(content=json.dumps(dict(code=403, msg='您没有执行该操作的权限')),
                                content_type='application/json')


class AccessRecordMiddleWare(MiddlewareMixin):
    """接口访问记录"""

    def process_response(self, request, response):
        meta = request.META
        http_method = request.method
        get_data = request.GET
        try:
            body_data = json.load(request.body)
        except:
            body_data = None
        ticket = request.COOKIES.get('ticket')
        request_user_agent = meta.get('HTTP_USER_AGENT')
        url = request.path_info.lstrip('')
        insert_data = {
            'url': url,
            'method': http_method,
            'user_agent': request_user_agent,
            'request_data': body_data if body_data else get_data,
            'request_module': url.split('/')[1],
            'ticket': ticket,
            'time': int(time.time()),
            'remote_addr': meta.get('REMOTE_ADDR'),
            'user_id': request.user.id
        }
        try:
            insert_data.update({
                'status_code': response.status_code,
                'process_time': int(time.time()) - insert_data.get('time'),
                'response_content': json.loads(response.content.decode('utf-8'))
            })
            collection_name = "access_records_%s" % datetime.datetime.now().strftime('%Y-%m-%d')
            stu_db.insert(collection_name=collection_name, insert_data=insert_data)
        except Exception as e:
            pass
        return response
