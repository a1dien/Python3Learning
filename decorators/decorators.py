def simple_function():
    #print('Some code before the old code')
    print('Simple function code')
    #print('Some code after the old code')

simple_function()

def decorator_function(original_function):
    def wrap_function():
        print('Some code before the old code')
        original_function()
        print('Some code after the old code')
    return wrap_function()


#decorated_function = decorator_function(simple_function)

@decorator_function
def simple_function():
    print('Simple function code')

simple_function()