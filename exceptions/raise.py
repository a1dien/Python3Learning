#raise ValueError('invalid vallue')
#raise ValueError

def get_rainbow_color(color_number, text):
    color_number_list = [1, 2, 3, 4, 5, 6, 7]
    if type(color_number) is not int:
        raise TypeError ('Color number must be integer')
    if color_number not in color_number_list:
        raise ValueError('Parameter color_number must be in range of integer from 1 to 7.')
    if type(text) is not str:
        raise TypeError('Parameter text must be string type')

    if color_number == 1:
        return ('red ' + text)
    elif color_number == 2:
        return ('orange ' + text)
    elif color_number == 3:
        return ('yellow ' + text)
    elif color_number == 4:
        return ('green ' + text)
    elif color_number == 5:
        return ('blue ' + text)
    elif color_number == 6:
        return ('indigo ' + text)
    elif color_number == 7:
        return ('violet ' + text)


color = get_rainbow_color(1, True)
print(color)
