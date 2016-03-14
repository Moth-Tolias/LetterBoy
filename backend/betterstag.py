def string_stagger_case(oldstring,spaces = True,first = True):
    """Return a staggered version of a string.
    
    This software is based upon original code by www.gmlscripts.com.
    Ported to Python 3.4 by Moth Tolias.
    
    Args:
      oldstring(string): The string to stagger.
      spaces(bool, optional): Whether to include spaces in the staggering.
        Defaults to True.
      first(bool, optional): Whether the first letter is capitalised.
        Defaults to True. 

    Returns:
      string
      
    """
    
    char = "" # An iterator of the characters in the old string.
    charnum = 0 # An iterator of the letters to grab from the new strings.
    newstring = "" # The output string.
    upstring = oldstring.upper() # An uppercase version of oldstring.
    downstring = oldstring.lower() # A lowercase version of oldstring.
    substr = "" # A middleman variable for char.
    currcaps = first # The current capitalisation state. 
    
    for char in oldstring:
        substr = char # Char is immutable. We need a mutable version.
        if char == " " and not spaces:
            newstring += " "
            charnum += 1 # Get ready to grab the next letter.
            continue
        if currcaps:
            newstring += upstring[charnum]
        else:
            newstring += downstring[charnum]
        currcaps = not currcaps # Change the caps state.
        charnum += 1 # Get ready to grab the next letter.
    return newstring   

print(string_stagger_case("""Well, now you can! if you have python's IDLE editor, at least...

disclaimer: swearwords are not automatically inserted into the text
but seriously why on earth would you need this dumb thing i don't even"""))
