import clr

def process_input(func, input):
	if isinstance(input, list): return [func(x) for x in input]
	else: return func(input)
	
def WSSessionWasTerminatedProperly(wssess):
	if wssess.__repr__() == 'WorksharingSession': return wssess.WasTerminatedProperly()
	else: return None

OUT = process_input(WSSessionWasTerminatedProperly,IN[0])