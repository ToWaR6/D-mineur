def print_field(field):
    print('Mine Field')
    for x in range(field.size_x):
        ligne = ''
        for y in range(field.size_y):
            ligne += field.field[x][y].value
            if y < field.size_y-1:
                ligne += ' | '

        print(ligne)
