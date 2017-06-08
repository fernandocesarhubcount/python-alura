import os

class File(object):
	def __init__(self,file_path):
		self.file_path = file_path

	def read(self):
		file = open(self.file_path, 'r')
		array_line = []
		for line in file:
			array_line.append(line)
		file.close()
		return array_line

	def write(self,text,option='a'):
		file = open(self.file_path, option)
		file.write(text)
		file.close()

	def delete(self):
		os.remove(self.file_path)