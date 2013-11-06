import os
import file_util
import html_util

class caesar:
	def __init__(self,question_library_path,question_path):
		config = file_util.dynamic_import(os.path.join(
		 question_library_path,question_path,'cqg_config.py'))
		self.question_library_path = question_library_path
		self.question_path = question_path

		self.plaintext = config.plaintext
		self.ciphertext = config.ciphertext
		self.key = config.key
		self.hotspots = config.hotspots
	
	def get_question_library_path(self):
		return self.question_library_path
	
	def get_question_path(self):
		return self.question_path

	def get_css(self,answer):
		return style

	def get_html(self, answer):
		print answer
		print self.plaintext
		print self.ciphertext
		print self.hotspots
		print self.key		
		
		html = "<div class=\"container\">"
		html += "<p>Use a <b>caesar</b> cipher with key " + str(self.key)  + " to encrypt the plain text.</p>"
		topArray = ["Plain text"]
		bottomArray = ["Cipher text"]
		
		#Load the Plain text into a list
		for char in self.plaintext:
			topArray.append(str(char))
			
		#Load the cipher text into the bottom array
		for char in self.ciphertext:
			bottomArray.append(str(char))
		
		#Replace hotspot positions with text boxes
		for pos in self.hotspots:
			bottomArray[pos+1] = html_util.get_text("text_box" + str(pos), '', 1)
		
		tableArray = [topArray, bottomArray]
		
		html += html_util.get_table(tableArray, "class=\"center_table\"")

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
	div.question_cell {
		text-align:left;
		width:75%;
		margin:auto;
	}
	table.question_cell, td.question_cell {
		border:0px;
	}
	table.center_table
	{
		margin-left:auto; 
    	margin-right:auto;
    	border-collapse: collapse;
   		border-style: hidden;
	}
	td.question_cell {
		border:1px solid black;
	}
	div.container {
		text-align:center;
	}
	table td, table th {
    	border: 1px solid black;
	}
	td {
		padding-left:10px;
		padding-right:10px;
		text-align:center;
	}
	td.top {
		vertical-align:top;
	}
	td.left {
		text-align:left;
	}
'''
