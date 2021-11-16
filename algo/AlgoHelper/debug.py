#dodebug=[3]
TermColors = {
    "HEADER" : '\033[95m',
    "OKBLUE" : '\033[94m',
    "OKCYAN" : '\033[96m',
    "OKGREEN" : '\033[92m',
    "WARNING" : '\033[93m',
    "FAIL" : '\033[91m',
    "ENDC" : '\033[0m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m'

	
}

default_color="OKCYAN"
import sys
def array_to_str(array):
	#print(array)
	retlist=[]

	for val in array:
		if isinstance(val,list):
			retlist.append(array_to_str(val) )
		elif isinstance(val,str):
			retlist.append( val )			
		else:
			retlist.append(str(val) )

	retval = "[ " + ", ".join(retlist) + ' ]'
	return retval

def get_color_str(line,color=None):
	output=""
	if not color:
		color = default_color
	if(isinstance(line,list)):
		line = array_to_str(line)
	if not isinstance(line,str):
		line=repr(line)
	output = TermColors[color]
	output+=line
	output += TermColors["ENDC"]
	return output
def print_color(line,color=None):
	if color==None:
		color=default_color
	print(get_color_str(line,color))

def script_header(line):
	offset=len(line)//2
	print_color("_"*(60),color="WARNING")
	print_color(" "*(30-offset)+line,color="WARNING")
	print_color("_"*60,color="WARNING")
def test_header(line):
	offset=len(line)//2
	line = "\n%s %s %s" % ("*"*(29-offset), line, "*"*(29-offset))
	print_color(line,color="WARNING")
def section_header(line):
	offset=len(line)//2
	line = "\n%s %s %s" % ("-"*(29-offset), line, "-"*(29-offset))
	print_color(line,color="WARNING")
class DebugConsole():
	def __init__(self,color="OKCYAN"):
		self.debugstrs=[]
		self.default_color=color
	"""
		append a line to the debug output
	"""
	def log(mystr,color=None):
		if not color:
			color=self.default_color
		self.debugstrs.append([mystr,color])
	"""
		clear debug output
	"""
	def flush(self):
		self.debugstrs=[]
	"""
		print logged debug lines
	"""
	def show(self):
		for out in debugstrs:
			print_color(out[0],color=out[1])

		debugstrs=[]

#legacy for one line debug
debug_console = DebugConsole()

def debug(line):
	debug_console.log(line)
def log(line):
	debug_console.log(line)
def debug_out():
	debug_console.show()
def flush():
	debug_console.flush()
