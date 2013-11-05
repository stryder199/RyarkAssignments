import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','int'],['$x2','int'],['$x3','int'],['$y0','int'],
]

tuple_list = [
	['while_break_',
		[0,1,2,None],
		[0,2,2,None],
		[0,4,2,None],
		[0,6,2,None],
		[0,7,2,None],
		[None,None,2,1],
		[None,None,2,2],
		[None,None,2,4],
		[None,None,2,6],
		[None,None,2,7],
		[0,1,3,None],
		[0,2,3,None],
		[0,4,3,None],
		[0,6,3,None],
		[0,7,3,None],
		[None,None,3,1],
		[None,None,3,2],
		[None,None,3,4],
		[None,None,4,6],
		[None,None,5,7],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
'''

main_code_template = '''\
dx		int s = $x1;
dx		int i = 1;
dx		while (i < $x2) {
dx			if (i % $x3 == 0)
dx				break;
dx			s = s + i;
dx			i++;
dx		}
dx		printf("%d\\n",s);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)