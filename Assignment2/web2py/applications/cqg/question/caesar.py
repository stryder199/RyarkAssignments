import os
import file_util
import html_util
import caesar_util

class caesar:
	def __init__(self,question_library_path,question_path):
		config = file_util.dynamic_import(os.path.join(
		 question_library_path,question_path,'cqg_config.py'))
		self.question_library_path = question_library_path
		self.question_path = question_path

		self.plaintext = config.plaintext
		self.key = config.key
		self.ciphertext = caesar_util.caesar_encrypt(self.plaintext, self.key)
		self.hotspots = config.hotspots
	
	def get_question_library_path(self):
		return self.question_library_path
	
	def get_question_path(self):
		return self.question_path

	def get_css(self,answer):
		return style

	def get_html(self, answer):		
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
		i = 0
		for pos in self.hotspots:
			if answer['answer'] == None: #DR1
				bottomArray[pos+1] = html_util.get_text('answer', '', 1) #DR2
			else:
				bottomArray[pos+1] = html_util.get_text('answer', answer['answer'][i], 1) #DR3 #DR4
				i=i+1
		
		tableArray = [topArray, bottomArray]
		
		html += html_util.get_table(tableArray, "class=\"center_table\"")

		return html + "</div>"

	def get_input_element_ids(self):
		return ['answer']
	
	def check_answer(self,answer):
		i = 0;
		try:
			for char in answer['answer']: #DR5
				#If the char isn't a string or char
				if not isinstance(char, str) and not isinstance(char, unicode) and not isinstance(char, basestring):
					return False
				if char == '' or char.lower() != self.ciphertext[self.hotspots[i]]: #DR6(inner) #DR7
					return False
				i = i + 1
		except:
			return False
		return True

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
