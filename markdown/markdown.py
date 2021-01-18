import re

# Compiled regular experssions as shown by yawpitch's solution
BOLD_RE = re.compile(r"(.*)__(.*)__(.*)")
ITALICS_RE = re.compile(r"(.*)_(.*)_(.*)")
LIST_RE = re.compile(r"\* (.*)")

def parse(markdown):
    """Parse some HTML and add HTML tags where appropriate.
    
    Parameters
    ------ 
    arg1 : string
        HTML being considered for markup 
  
    Returns
    ------
    string
        Marked up HTML
    """
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        i = markup_heading(i)
        m = LIST_RE.match(i)
        if m:
            curr = m.group(1)
            curr = markup_strong(curr)
            curr = markup_em(curr)
            if not in_list:
                in_list = True
                i = '<ul><li>' + curr + '</li>'
            else:
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        i = markup_paragraph(i)
        i = markup_strong(i)
        i = markup_em(i)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False

        res += i
    if in_list:
        res += '</ul>'
    return res

def markup_heading(text):
    """Markup text in a headings <h6|h2|h1> when ###### found.
  
    Parameters
    ------ 
    arg1 : string
        Line of code being considered for markup 
  
    Returns
    ------
    string
        Marked up code with <h6|h2|h1>

    """
    if re.match('###### (.*)', text) is not None:
        text = '<h6>' + text[7:] + '</h6>'
    elif re.match('## (.*)', text) is not None:
        text = '<h2>' + text[3:] + '</h2>'
    elif re.match('# (.*)', text) is not None:
        text = '<h1>' + text[2:] + '</h1>'
    return text

def markup_paragraph(text):
    """
    Markup text in a paragraph <p> when not in h/ul/p/li already  
  
    Parameters
    ------ 
    arg1 : string
        Line of code being considered for markup 
  
    Returns
    ------
    string
        Marked up code with <p>

    """
    m = re.match('<h|<ul|<p|<li', text)
    if not m:
        text = '<p>' + text + '</p>'

    return text

def markup_strong(text):
    """
    Markup text in a <strong> when (dobule) heavily underlined 
  
    Parameters
    ------ 
    arg1 : string
        Line of code being considered for markup 
  
    Returns
    ------
    string
        Marked up code with <strong>

    """
    # m = re.match('(.*)__(.*)__(.*)', text)
    # if m:
    #     text = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
    return BOLD_RE.sub(r"\1<strong>\2</strong>\3", text)

def markup_em(text):
    """
     Markup text in a <em> when underlined 
  
   Parameters
    ------ 
    arg1 : string
        Line of code being considered for markup 
  
    Returns
    ------
    string
        Marked up code with <em>
    """
    # m = re.match('(.*)_(.*)_(.*)', text)
    # if m:
    #     text = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
    return ITALICS_RE.sub(r"\1<em>\2</em>\3", text)