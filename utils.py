# -*- coding: utf-8 -*-
import time
import base64
from compat import text_type, binary_type, string_types

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


def base64url_decode(input):
    if isinstance(input, text_type):
        input = input.encode('ascii')

    rem = len(input) % 4

    if rem > 0:
        input += b'=' * (4 - rem)

    return base64.urlsafe_b64decode(input)

def is_failure(exp, failure_time=300):
    '''
        desc: 验证所给exp是否失效
        input: 
            exp : 
                desc: 时间戳
                type: string
            failure_time ：
                           desc: 从生成的时刻到失效时间间隔的总秒数
                           type: s (秒)
                           default: 300
        return: is_failure :
                            type: boolean
                            default: false
    '''
    # try:
    #     exp = int(exp)
    # 无效的时间戳异常  todo
        

    is_failure = True if int(time.time())-exp > failure_time else False
    return is_failure