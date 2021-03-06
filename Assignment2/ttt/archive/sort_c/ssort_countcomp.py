question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string']
]

tuple_list = [
	['ssort_countcomp_',
		[None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void selection_sort(int a[], int n)
dx	{
dx		int i,j,temp,comparison_count;
dx		comparison_count = 0;
dx
dx		for (i = 0; i < n-1; i++) {
dx			for (j = i + 1; j < n; j++) {
dx				comparison_count++;
dx				if (a[i] > a[j]) {
dx					temp = a[i];
dx					a[i] = a[j];
dx					a[j] = temp;
dx				}
dx			}
dx		}
dx		printf("%i\\n",comparison_count);
dx	}
'''

main_code_template = '''\
dx		int a[3] = {1,2,4};
dx
dx		selection_sort(a,3);        
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
