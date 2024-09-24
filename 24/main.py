def make_3sg_form(verb):
    if verb.endswith('y'):
        end = verb[-1:]
        third_form = verb[:-1]  
        final_form = third_form + 'ies'
        print (final_form)
    elif verb.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):
        final_form = verb + 'es'
        print (final_form)
    else:
        final_form = verb + 's'
        print(final_form)

    return final_form


make_3sg_form('run')
