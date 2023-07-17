from django import template

register=template.Library()

def swap(data):
    return data.swapcase()

register.filter('swapping',swap)


@register.filter('remove')
def remove(data,arg):
    return data.replace(arg,'')

@register.filter()
def counting(s,sub):
    c=0
    for i in range(len(s)):
        if s[i:i+len(s):]==sub:
            c+=1
    return c
