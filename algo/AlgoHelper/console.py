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
	if color in TermColors:
		output = TermColors[color]
	else:
		output="FAIL"
	output+=line
	#print("Color",color)
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
	def log(self,mystr,color=None):
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
		#print(self.debugstrs)
		for out in self.debugstrs:
			print_color(out[0],color=out[1])

		debugstrs=[]

#legacy for one line debug
debug_console = DebugConsole()

def debug(line,color=None):
	debug_console.log(line,color=color)
def log(line,color=None):
	debug_console.log(line,color=color)
def debug_out():
	debug_console.show()
def flush():
	debug_console.flush()
def print_variables(vars,row_size=3):
	var_strs=[]

	output=""
	idx=0
	for key,val in vars.items():
		idx+=1
		cur_str=" %s: %s "%(get_color_str(key,"BOLD"),get_color_str(val,"HEADER"))
		var_strs.append(cur_str)
		if idx%row_size==0:
			output += "     ".join(var_strs)+"\n"
			var_strs=[]

	output += "     ".join(var_strs)

	print(output)

