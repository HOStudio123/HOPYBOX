from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text as print

def ask_proceed(question:str):  
    # question prompt
    text = [
    ('class:arrow', '➤'),
    ('', ' '),
    ('class:text',f'{question}, Do you want to proceed ? (Y/n) ')
    ]
    style = {
    'arrow': '#00FF00',
    'text': '#00FFFF',
    }
    answer = color_input(text,style,single=False)
    if answer in ["Y", "y", ""]:
        return True
    elif answer in ["N", "n"]:
        return False
    else:
        color_print(f"✗ Your response('{answer}') was not one of the expected responses: y, n",'#CD0000')
        ask_proceed(question)

def error_cross(error,mode,text:str,value):
    # error output
    color_print(f"✗ {error} in {mode}: \n '{value}' -> {text}",'#FF0000')
    
def error_cross_simple(text:str):
    # more pure error output
    color_print(f'✗ Oops! {text}','#FF0000')

def tip_tick(text:str):
    # tick prompt
    text = [
    ('class:tick', '✓'),
    ('', ' '),
    ('class:text',text)
    ]
    style = {
    'tick': '#00FF00',
    'text': '#00FFFF'
    }
    color_print(text,style,single=False)

def getpass(text:str,color:str,html=False):
    # password protection for input
    style = Style.from_dict({'prompt':color})
    if html:
        return prompt(HTML(text),is_password=True,style=style)
    else:
        return prompt(text,is_password=True,style=style)
    
def color_input(text,color,single=True,html=False):
    # beautifying input
    if single:
        style = Style.from_dict({'prompt':color})
    else:
        text = FormattedText(text)
        style = Style.from_dict(color)
    if html:
        return prompt(HTML(text),style=style)
    else:
        return prompt(text,style=style)
        
def color_print(text,color,single=True):
    # beautifying output
    if single:
        text = FormattedText([('class:text',text)])
        style = Style.from_dict({'text':color})
    else:
        text = FormattedText(text)
        style = Style.from_dict(color)
    print(text,style=style)