# -*- coding: utf-8 -*-\
import json, time, chardet
from jwt.api_jwt import wdJwt
from jwt.utils import base64urlencode, force_unicode


if __name__ == "__main__":
	wd = wdJwt()
	start_time = int(time.time())
	print 'header: ',  wd.generate_header()
	payload_str = force_unicode(json.dumps({
				'nickname' : u'王强',
				'gender': 1
				}))

	print 'payload: ',  wd.generate_payload(payload_str)
	print 'signature: ', wd.generate_signature()
	first_token = wd.generate_token()
	print 'token: ', first_token
	print 'token code: ', chardet.detect(first_token)
	print 'verify token', wd.verify_token(first_token)
	# FormatError
	try:
		wd.verify_token(first_token+".d")
	except Exception, e:
		print "verify token ", e 
	
	# LosedError
	try:
		wd.verify_token(first_token+"s")
	except Exception, e:
		print "verify token", e


	# TimeoutTokenError
	time.sleep(7)
	try:
		wd.verify_token(first_token)
	except Exception, e:
		print "verify token", e

