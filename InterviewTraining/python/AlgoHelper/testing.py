import json

def load_tests(module_name):
	file_name = "tests/%s.json" % module_name
	with open(file_name) as fp:
		contents = fp.read()
		retval = json.loads(contents)

	return retval
