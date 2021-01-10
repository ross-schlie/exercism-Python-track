'''
Introduction
Refactor a Markdown parser.

The markdown exercise is a refactoring exercise. 
There is code that parses a given string with Markdown syntax and returns the associated HTML for that string. 
Even though this code is confusingly written and hard to follow, somehow it works and all the tests are passing! 
Your challenge is to re-write this code to make it easier to read and maintain while still making sure that all the tests keep passing.

It would be helpful if you made notes of what you did in your refactoring in comments so reviewers can see that, 
but it isn't strictly necessary. The most important thing is to make the code better!
'''

import re

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        i = markup_heading(i)
        m = re.match(r'\* (.*)', i)
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
    '''
    Markup text in a headings <h6|h2|h1> when ###### found  
  
    Parameters: 
    arg1 (text): the line of code being considered for markup 
  
    Returns: 
    text: Marked up code with <h6|h2|h1>
    '''
    if re.match('###### (.*)', text) is not None:
        text = '<h6>' + text[7:] + '</h6>'
    elif re.match('## (.*)', text) is not None:
        text = '<h2>' + text[3:] + '</h2>'
    elif re.match('# (.*)', text) is not None:
        text = '<h1>' + text[2:] + '</h1>'
    return text

def markup_paragraph(text):
    '''
    Markup text in a paragraph <p> when not in h/ul/p/li already  
  
    Parameters: 
    arg1 (text): the line of code being considered for markup 
  
    Returns: 
    text: Marked up code with <p>
    '''
    m = re.match('<h|<ul|<p|<li', text)
    if not m:
        text = '<p>' + text + '</p>'

    return text

def markup_strong(text):
    '''
    Markup text in a <strong> when (dobule) heavily underlined 
  
    Parameters: 
    arg1 (text): the line of code being considered for markup 
  
    Returns: 
    text: Marked up code with <strong>
    '''
    m = re.match('(.*)__(.*)__(.*)', text)
    if m:
        text = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
    return text

def markup_em(text):
    '''
     Markup text in a <em> when underlined 
  
    Parameters: 
    arg1 (text): the line of code being considered for markup 
  
    Returns: 
    text: Marked up code with <em>
    '''
    m = re.match('(.*)_(.*)_(.*)', text)
    if m:
        text = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
    return text

# a = parse("This will be a paragraph")
# print(a) # "<p>This will be a paragraph</p>"