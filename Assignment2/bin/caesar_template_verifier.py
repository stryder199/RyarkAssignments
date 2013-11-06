#!/usr/bin/python

import os
import sys

# Modify our path so Python knows where to find verify_util and file_util modules.
sys.path.append(os.path.join(os.path.dirname(__file__), '../web2py/applications/cqg/question'))

import verify_util
import file_util

# list of verification identifier/condition pairs
condition_list = [
    ['question_groups_defined',
        "'question_groups' is defined"],
    ['question_groups_type',
        "'question_groups' is a list"],
    ['group_format',
        'Each group is a list of length at least 2'],
    ['group_unique',
        'Each group has a unique name'],
    ['question_format',
        'Each question is a list of length 4'],
                  
    ['plaintext',
        "'plaintext' is a string comprised of chars in [A..Z]"],
    ['ciphertext',
        "'ciphertext' is a string comprised of chars in [A..Z]"],
    ['key',
        "'key' is an int < 26"],
    ['hotspots',
        "'hotspots' is a list of indeces into plaintext (0-relative)"],
]
 
def verify_conditions(template, condition_list):
    conditions_dictionary = dict(condition_list)

    if not ('question_groups' in dir(template)):
        return conditions_dictionary['question_groups_defined']
    if not (type(template.question_groups) == list):
        return conditions_dictionary['question_groups_type']

    prefix_list = []
    for group in template.question_groups:
        if not (type(group) == list and len(group) >= 2):
            return conditions_dictionary['group_format'] + \
             '\n\tgroup: ' + str(group)

        if not (type(group[0]) == str and group[0] not in prefix_list):
            return conditions_dictionary['group_unique'] + \
             '\n\tgroup: ' + str(group)
        else:
            prefix_list.append(group[0])

        for question in group[1:]:
            if not (type(question) == list and len(question) == 4):
                return \
                 conditions_dictionary['question_format'] + \
                 '\n\tquestion: ' + str(question)

            if not (type(question[0]) == str and question[0].isalpha()):
                return conditions_dictionary['plaintext']+\
                 '\n\tquestion: ' + str(question)
                 
            if not (type(question[1]) == str and question[1].isalpha()):
                return conditions_dictionary['ciphertext']+\
                 '\n\tquestion: ' + str(question)

            if not (type(question[2]) == int and question[2] < 26 and question[2] >= 0):
                return conditions_dictionary['key'] + \
                 '\n\tquestion: ' + str(question)

            if type(question[3]) is list:
                for index in question[3]:
                    if index not in range(len(question[0])):
                        return conditions_dictionary['hotspots'] + '\n\tquestion: ' + str(question)
            else:
                return conditions_dictionary['hotspots'] + '\n\tquestion: ' + str(question)
    print "Passed"

# handle invocation from command line
if __name__ == '__main__':
    n = verify_util.template_verifier_main(sys.argv, 'Question Type Caesar: Template Verification Conditions', condition_list, verify_conditions)

    if n == verify_util.COMMAND_LINE_SYNTAX_FAILURE:
        print 'Usage: caesar_template_verifier.py [template_file]'

    sys.exit(n)
