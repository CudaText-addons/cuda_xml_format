from cudatext import *
from . import xmlpp

WIDTH = 100 #reformat at max width

def do_format(text, indent, eol):
    text = xmlpp.get_pprint(text, indent=indent, width=WIDTH)
    lines = text.splitlines()
    text = eol.join(lines)+eol
    return text
    
class Command:
    def run(self):
        text = ed.get_text_all()
        indent = ed.get_prop(PROP_TAB_SIZE)
        eol = '\n'
        
        text = do_format(text, indent, eol)
        if text:
            ed.set_text_all(text)
            msg_status('XML formatted')
