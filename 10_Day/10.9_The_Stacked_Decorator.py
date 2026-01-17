def bold(func):
    def bold_wrap():
        return '<b>'+func()+'</b>'
    return bold_wrap
def italic(func):
    def italic_wrap():
        return '<i>'+func()+'</i>'
    return italic_wrap

@bold
@italic
def my_name():
    return 'sourav'

print(my_name())