# -*- coding:utf-8 -*-

from rest_framework.renderers import JSONRenderer


class CustomJsonRender(JSONRenderer):
    """ 自定义返回数据 Json格式
    {
        "code": 0,
        "msg": "success",
        "data": { ... }
    }
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            if isinstance(data, dict):
                msg = data.pop('msg', '请求成功')
                code = data.pop('code', 0)
                field_name = data.pop('field_name', '')
            else:
                msg = '请求成功'
                code = 0
                field_name = ''
            response = renderer_context['response']
            response.status_code = 200
            res = {
                'code': code,
                'msg': msg,
                'data': data,
                'field_name': field_name
            }
            return super().render(res, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
