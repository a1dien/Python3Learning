color_list = []

with open ('C:/Users/Val/Downloads/rainbow_colors1.txt', 'r') as rainbow_colors:
    for color in rainbow_colors:
        color_list.append(color.strip('\n'))

print(color_list)