game_type = 'input_output'

parameter_list = [
	['$y0','string']
]

tuple_list = [
	['KnR_1-1a_',[None]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx	printf("hello, world\\n");
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
hello, $y0
'''

