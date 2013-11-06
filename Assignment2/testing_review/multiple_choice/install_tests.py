import os

# generate questions
question_lib_path = os.path.abspath("../../question_library/test_multiple_choice/")

# generate questions
if not os.path.exists(question_lib_path):
    os.makedirs(question_lib_path)
    
os.system('multiple_choice_generate.py templates/template.py ../../question_library/test_multiple_choice/')

# copy quiz files
os.system('cp quizzes/test_multiple_choice.py ../../quizzes/')
