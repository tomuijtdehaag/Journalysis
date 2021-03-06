import clr

def process_input(func, input):
	if isinstance(input, list): return [func(x) for x in input]
	else: return func(input)
	
def WSSessionType(wssess):
	if wssess.__repr__() == 'WorksharingSession': return wssess.GetSessionType()
	else: return None

OUT = process_input(WSSessionType,IN[0])