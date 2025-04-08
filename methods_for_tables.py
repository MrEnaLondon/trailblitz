from tables.table_for_black import black_table
from tables.table_for_white import white_table

def coords_shuffle(coords):
    if coords[0][0] < coords[1][0]:
        print('shuffling a&b\'s...')
        coords[0][1], coords[1][1] = coords[1][1], coords[0][1]
        coords[0][0], coords[1][0] = coords[1][0], coords[0][0]
    if (coords[0][0] == coords[1][0]) and (coords[0][1] < coords[1][1]):
        print('shuffling c&d\'s...')
        coords[0][1], coords[1][1] = coords[1][1], coords[0][1]
    return coords[0][0], coords[1][0], coords[0][1], coords[1][1]

#chekes are two given spaces connected and available
def check_move(table, coords):
    coords = coords_shuffle(coords)
    print(coords)
    try:
        return table[coords[0]][coords[1]][coords[2]][coords[3]]
    except IndexError:
        print('exception!!!')
        return 0
#e.g. for chek_move:
#print(check_move(black_table ,[[3, 0], [3, 1]]))
#print(check_move(white_table ,[[3, 0], [3, 1]]))

