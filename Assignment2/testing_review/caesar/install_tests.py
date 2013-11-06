import os

question_lib_path = os.path.abspath("../../question_library/test_caesar/")

# generate questions
if not os.path.exists(question_lib_path):
    os.makedirs(question_lib_path)
    
os.system('caesar_generate.py templates/template.py ../../question_library/test_caesar/')

# copy quiz files
os.system('cp quizzes/test_caesar.py ../../quizzes/')
