
def getBoardPosition(position):
    column = position % 5
    row = position//5
    print(position)
    print(column)
    print(row)
    return row, column


getBoardPosition(4)
