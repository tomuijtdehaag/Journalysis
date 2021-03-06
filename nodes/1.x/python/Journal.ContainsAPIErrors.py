import clr

def process_input(func, input):
	if isinstance(input, list): return [func(x) for x in input]
	else: return func(input)
	
def journalContainsAPIErrors(journal):
	if journal.__repr__() == 'Journal': return journal.ContainsAPIErrors()
	else: return False

OUT = process_input(journalContainsAPIErrors,IN[0])