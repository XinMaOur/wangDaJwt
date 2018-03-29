# -*- coding: utf-8 -*-
header = {
	"typ": "JWT",
	"alg": "HS256"
    }

secret = "hixinma"    # 可以是任意字符串也可以是加密中的公钥

# default_exp_invalide_second = 5*60 # 默认exp失效时间为5分钟
default_exp_invalide_second = 5 # test 默认exp失效时间为3s