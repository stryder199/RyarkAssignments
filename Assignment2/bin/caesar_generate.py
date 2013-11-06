#!/usr/bin/python

import sys
import os

# Modify our path so Python knows where to find verify_util and file_util modules.
sys.path.append(os.path.join(os.path.dirname(__file__), '../web2py/applications/cqg/question'))

import file_util

template_string = '''\
product_family = 'caesar'
question_type = 'caesar'

plaintext = $p
ciphertext = $c
key = $k
hotspots = $h
'''

if len(sys.argv) != 3:
	print 'Usage: caesar_generate.py template question_directory'
	sys.exit(1)

try:
	template = file_util.dynamic_import(sys.argv[1])
except ImportError:
	print 'Failure while importing',sys.argv[1]
	sys.exit(2)

for group in template.question_groups:
	prefix = group[0]
	question_id = 0
	#We should generate the cipher using the alg not load it in... later...
	for (plaintext, ciphertext, key, hotspots) in group[1:]:
		path = os.path.join(sys.argv[2], prefix + str(question_id))

		if not os.path.exists(path):
			os.mkdir(path)

		config_string = template_string
		config_string = config_string.replace('$p', "'" + plaintext + "'")
		config_string = config_string.replace('$c', "'" + ciphertext + "'")
		config_string = config_string.replace('$k', str(key))
		config_string = config_string.replace('$h', str(hotspots))

		file_util.write_string(os.path.join(path,'cqg_config.py'), config_string)

		question_id += 1
