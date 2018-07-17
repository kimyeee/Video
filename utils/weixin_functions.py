# coding: utf-8
import datetime
import json
import logging
import random

import requests
from rest_framework import exceptions

from CpBackend.settings import WX_SMART_CONFIG, MEDIA_ROOT
from user_info.models import UserInfo
from ticket.functions import TicketAuthorize
from utils.redis_server import redis_client

logger = logging.getLogger('django')


class WxInterface:
    def __init__(self):
        self.appid = WX_SMART_CONFIG['appid']
        self.secret = WX_SMART_CONFIG['secret']

    # 微信code认证
    # @compute_run_time
    def code_authorize(self, code):
        url = "https://api.weixin.qq.com/sns/jscode2session"
        params = {
            'appid': self.appid,
            'secret': self.secret,
            'js_code': code,
            'grant_type': 'authorization_code'
        }
        response = requests.get(url=url, params=params, verify=False)
        if response.status_code != 200:
            logger.info('X' * 70)
            logger.info(response.text)
            logger.info('X' * 70)
            raise exceptions.ValidationError('连接微信服务器异常')
        res = response.json()
        if res.get('openid') and res.get('session_key'):
            # 首先查询数据库中是否存在该用户信息
            user_info = UserInfo.objects.filter(openid=res['openid']).first()
            if not user_info:
                # 给用户生成活动码
                while True:
                    seed = random.random()
                    code = str(int(seed * 1000000))
                    code = code + '8' * (6 - len(code)) if len(code) < 6 else code
                    code_exist = UserInfo.objects.filter(code=code).count()
                    if code_exist == 0:
                        break
                qr_code = self.get_forever_qrcode(res.get('openid'))
                # 如果用户不存在，则向数据库插入数据
                user_info = UserInfo.objects.create(openid=res['openid'], last_login=datetime.datetime.now(),
                                                    session_key=res['session_key'], code=code, qr_code=qr_code)
            else:
                # 如果用户存在，更新用户信息
                user_info.last_login = datetime.datetime.now()
                user_info.session_key = res.get('session_key')
                user_info.save()
            ticket = TicketAuthorize.create_ticket(res['openid'])
            return {'user_id': user_info.openid, 'ticket': ticket}
        else:
            logger.info('X' * 70)
            logger.info(response.text)
            logger.info('X' * 70)
            raise exceptions.ValidationError('微信认证异常： %s' % json.dumps(res))

    # 调用微信接口向用户发送模板消息
    def send_template_message(self, params):
        access_token = self.get_access_token()
        logger.info("@"*66)
        logger.info(params)
        url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token=" + access_token
        response = requests.post(url=url, data=json.dumps(params), headers={"Content-Type": "application/json"})
        if response.status_code != 200:
            logger.info('WxInterface code_authorize response: %s' % response.text)
            raise exceptions.ValidationError('连接微信服务器异常')
        res = response.json()
        logger.info('*' * 25 + 'send template message' + '*' * 25)
        logger.info(res)
        logger.info('*' * 70)
        return

    # 获取access_token
    def get_access_token(self):
        # 微信token有次数限制，故需要缓存起来
        access_token = redis_client.get_instance('cp.access_token')
        if access_token:
            return access_token
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            'appid': self.appid,
            'secret': self.secret,
            'grant_type': 'client_credential'
        }
        response = requests.get(url=url, params=params, verify=False)
        if response.status_code != 200:
            logger.info('WxInterface get_access_token response: %s' % response.text)
            raise exceptions.ValidationError('连接微信服务器异常')
        res = response.json()
        redis_client.set_instance(key='cp.access_token', value=res['access_token'])
        logger.info(res)
        return res['access_token']

    # 生成个人用户带参数的小程序码
    def get_forever_qrcode(self, code):
        url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit'
        params = {
            'access_token': self.get_access_token(),
        }
        data = {'scene': code, 'width': 430, }
        response = requests.post(url=url, params=params, json=data)
        qr_code_save_path = '%s%s%s%s' % (MEDIA_ROOT, '/images/qrcode/', code, '.jpg')
        qr_code_url = '%s%s%s' % ('images/qrcode/', code, '.jpg')
        open(qr_code_save_path, 'wb').write(response.content)
        return qr_code_url


WxInterfaceUtil = WxInterface()
