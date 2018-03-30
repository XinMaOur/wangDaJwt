# -*- coding: utf-8 -*-
import base64
import json
import datetime
import time
import chardet
from .exceptions import TimeoutTokenError, FormatError, LosedError, InvalidTokenError

from .init_data import header, secret, default_exp_invalide_second
from .algorithms import HMACAlgorithm
from .utils import base64urlencode, base64urldecode, force_unicode, is_failure
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

hmac = HMACAlgorithm()

class wdJwt(object):
	
	def __init__(self):
		self.header = base64urlencode(json.dumps(header))
		self.payload = {}
		self.signature = {}
		self.secret = secret
		self.token = ""

	def generate_token(self):
		self.token = self.header + '.' + self.payload + '.' + self.signature
		return self.token


	def generate_header(self):
		header_json = json.dumps(self.header, separators=(',', ':'))
		self.header = base64urlencode(header_json)
		return self.header


	def generate_payload(self, msg, exp=int(time.time())+default_exp_invalide_second):
		'''
			desc: 生成payload
			input: 
				msg type: json
				{
				'nickname' : u'王强',
				'gender' 1
				}
			return:
				payload type:string base64 
		'''
		
		msg = force_unicode(msg)
		self.payload = json.loads(msg)
		self.payload['exp'] = exp # 预留5分钟登录有效期
		# 序列化
		payload_json = json.dumps(self.payload, separators=(',', ':'))
		self.payload = base64urlencode(payload_json)
		return self.payload

	def generate_signature(self):
		'''
			desc: 生成签名
			input: self.header, self.payload, secret
			return: signature
		'''
		msg = self.header + '.' + self.payload
		self.signature = base64urlencode(hmac.sign(msg, self.secret))
		
		return self.signature
	

	def verify_token(self, token):
		'''
			desc: 验证token是否有效
			input: token
						{ 
						type: str
						}
			return :
					success:
						Boolean: True
					error:
						1.token : timeout 过期失效 
						2.token : losed 已丢失失效包括已篡改
						3.token : error format 格式错误失效
		'''
		if len(token.split('.')) == 3:
			hea, pal, sig = token.split('.')
			msg = force_unicode(hea + '.' + pal)
			not_losed =  hmac.verify(msg, self.secret, base64urldecode(sig))
			if not not_losed:
				raise LosedError('Token is losed.')
			elif is_failure(pal):
				raise TimeoutTokenError('Token is timeout.')
			return not_losed
		else: 
		 	raise FormatError('Bad format for token.') 

