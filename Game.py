from Cell import Cell
from Color import Color


def find_chain(field, index):
    new = []

    for i in range(len(field) + 2):
        arr2 = []
        for j in range(len(field[0]) + 2):
            arr2.append(Cell(Color.NONE))
        new.append(arr2)

    for i in range(len(field) + 2):
        for j in range(len(field[0]) + 2):
            new[i][j] = field[i - 1][j - 1] if 0 < i < len(field) + 1 and 0 < j < len(field[0]) + 1 else Cell(Color.NONE)

    list = set()

    visited = []
    for i in range(len(new)):
        arr2 = []
        for j in range(len(new[0])):
            arr2.append(False)
        visited.append(arr2)

    chain = similar_near(new, (index[0] + 1, index[1] + 1), list, visited)

    return chain


def similar_near(extendedField, index, list, visited):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    list.add(index)
    visited[index[0] + 1][index[1] + 1] = True
    for k in range(4):
        if 0 < index[0] + dx[k] < len(extendedField) and 0 < index[1] + dy[k] < 2*len(extendedField) - 2:
            if extendedField[index[0] + dx[k]][index[1] + dy[k]].color == extendedField[index[0]][index[1]].color and \
                    visited[index[0] + dx[k]][index[1] + dy[k]] is False and extendedField[index[0] + dx[k]][index[1] + dy[k]].color != Color.NONE:
                list.add((index[0] + dx[k], index[1] + dy[k]))
                visited[index[0] + dx[k]][index[1] + dy[k]] = True
                similar_near(extendedField, (index[0] + dx[k], index[1] + dy[k]), list, visited)
    return list
