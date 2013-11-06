import os
import file_util
import html_util

class caesar:
	def __init__(self,question_library_path,question_path):
		print "Starting Initing Caesar obj"
		config = file_util.dynamic_import(os.path.join(
		 question_library_path,question_path,'cqg_config.py'))
		self.question_library_path = question_library_path
		self.question_path = question_path

		self.plaintext = config.plaintext
		self.ciphertext = config.ciphertext
		self.key = config.key
		self.hotspots = config.hotspots
		print "Finished Initing Caesar obj"
	
	def get_question_library_path(self):
		return self.question_library_path
	
	def get_question_path(self):
		return self.question_path

	def get_css(self,answer):
		return style

	def get_html(self, answer):
		print "Starting to generate html"
		html = "<div>"
		html += "<p>" + self.question_text + "</p>"
		topArray = ["Plain text"]
		bottomArray = ["Cipher text"]
		
		#Load the Plain text into a list
		for char in self.plaintext:
			topArray.append(char)
			
		#Load the cipher text into the bottom array
		for char in self.ciphertext:
			bottomArray.append(char)
		
		#Replace hotspot positions with text boxes
		for pos in self.hotspots:
			bottomArray[pos] = html_util.get_text()
		
		tableArray = [topArray, bottomArray]
		
		html += html_util.get_table(tableArray)

		print "Finished generating html"
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
