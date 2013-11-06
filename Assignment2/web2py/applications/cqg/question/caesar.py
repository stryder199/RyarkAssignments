import os
import file_util
import html_util

class caesar:
	def __init__(self,question_library_path,question_path):
		config = file_util.dynamic_import(os.path.join(
		 question_library_path,question_path,'cqg_config.py'))
		self.question_library_path = question_library_path
		self.question_path = question_path

		self.question_text = config.question_text
		self.answers = config.answers
		self.correct_answer = config.correct_answer
	
	def get_question_library_path(self):
		return self.question_library_path
	
	def get_question_path(self):
		return self.question_path

	def get_css(self,answer):
		return style

	def get_html(self, plain, answer):
		html = "<div>"
		html += "<p>" + self.question_text + "</p>"
		topArray = ["Plain text"]
		bottomArray = ["Cipher text"]
		
		#Load the Plain text into a list
		for i in range(len(plain)):
			topArray.append(plain[i])
		
		#Get text boxes for answers
		for i in range(len(answer)):
			bottomArray[i] = html_util.get_text()
		
		tableArray = [topArray, bottomArray]
		
		html += html_util.get_table(tableArray)

		return html + "</div>"

	def get_input_element_ids(self):
		return ['answer']
	
	def check_answer(self,answer):
		try:
			if type(self.correct_answer) is list:
				answer_list = [int(i) for i in answer['answer']] #DR1
				return set(answer_list) == set(self.correct_answer)
			else:
				return int(answer['answer']) == self.correct_answer #DR2
		except:
			return False

style = '''
	#question_cell div {
		text-align:left;
		width:75%;
		margin:auto;
	}
	#question_cell table, #question_cell td {
		border:0px;
	}
	#question_cell {
		border:1px solid black;
	}
	td.top {
		vertical-align:top;
	}
	td.left {
		text-align:left;
	}
'''
