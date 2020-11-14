"""This module generates suggested email addresses from name inputs"""
def email_addresses(first, last, domain = '@exeter.ac.uk'):
    '''This is the function that takes 2 list inputs and the
    domain and then returns their respective email addresses'''
    loop = len(first)
    for i in range(loop):
        first[i] = first[i].lower()
        last[i] = last[i].lower()
        first[i] = first[i][0:1]
    result =[]
    for i in range(loop):
        email = first[i] + '.' + last[i] + domain
        result.append(email)
    return result

print(email_addresses(["David", "Matthew"], ["Wakeling", "Collison"]))
