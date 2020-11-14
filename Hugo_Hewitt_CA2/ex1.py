"""This module defines the vat function that calulates VAT on items"""
def vat(pretax_price, kids = False, category = 'miscellaneous'):
    '''A function to return the value of prices after tax worked out according to their catagory'''
    tax = 0.20
    if kids and category == 'clothes' or category == 'food':
        return pretax_price
    addon = pretax_price * tax
    newprice = pretax_price + addon
    return newprice

#print(vat(10, False, 'stuff'))
