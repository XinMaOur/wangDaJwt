# -*- coding: utf-8 -*-
import time
import base64
import json
from .init_data import default_exp_invalide_second
from .compat import text_type, binary_type, string_types
from .exceptions import ExpLosedError, ExpTypeError

def base64urlencode(data):
    return base64.urlsafe_b64encode(data).rstrip('=')

def force_unicode(value):
    if isinstance(value, binary_type):
        return value.decode('utf-8')
    elif isinstance(value, text_type):
        return value
    else:
        raise TypeError('Expected a string value')


def force_bytes(value):
    if isinstance(value, text_type):
        return value.encode('utf-8')
    elif isinstance(value, binary_type):
        return value
    else:
        raise TypeError('Expected a string value')


def base64urldecode(input):
    if isinstance(input, text_type):
        input = input.encode('ascii')

    rem = len(input) % 4

    if rem > 0:
        input += b'=' * (4 - rem)

    return base64.urlsafe_b64decode(input)

def is_failure(paload):
    '''
        desc: 验证所给exp是否失效
        input: 
            paload : 
                desc: 信息摘要
                type: string
            
        return: is_failure :
                            desc: 是否失效
                            type: boolean
                            default: false
    '''
    # try:
    #     exp = int(exp)
    # 无效的时间戳异常  todo
    paload = json.loads(base64urldecode(force_unicode(paload)))
    if paload.has_key('exp'):
        exp = paload['exp']
        if isinstance(exp, int):
            is_failure = True if int(time.time()) > exp else False
            return is_failure
        else:
            raise ExpTypeError('Type error for exp.')
    else:
        raise ExpLosedError('Exp is Losed for paload.')