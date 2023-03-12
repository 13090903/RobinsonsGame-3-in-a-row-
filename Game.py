import random

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
            new[i][j] = field[i - 1][j - 1] if 0 < i < len(field) + 1 and 0 < j < len(field[0]) + 1 else Cell(
                Color.NONE)

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
        if 0 < index[0] + dx[k] < len(extendedField) and 0 < index[1] + dy[k] < 2 * len(extendedField) - 2:
            if extendedField[index[0] + dx[k]][index[1] + dy[k]].color == extendedField[index[0]][index[1]].color and \
                    visited[index[0] + dx[k]][index[1] + dy[k]] is False and extendedField[index[0] + dx[k]][
                index[1] + dy[k]].color != Color.NONE:
                list.add((index[0] + dx[k], index[1] + dy[k]))
                visited[index[0] + dx[k]][index[1] + dy[k]] = True
                similar_near(extendedField, (index[0] + dx[k], index[1] + dy[k]), list, visited)
    return list


def delete_empty_cells(field):
    for k in range(len(field)):
        for i in range(len(field) * 2):
            for j in range(len(field) - 1, 0, -1):
                while field[j][i].color == Color.NONE and j > 0:
                    field[j][i].color = field[j - 1][i].color
                    field[j - 1][i].color = Color.NONE
                    j = j - 1

    for k in range(len(field) * 2):
        for col in range(len(field) * 2 - 2, -1, -1):
            if column_is_empty(field, col):
                for row in range(len(field) - 1):
                    while row < len(field) and field[row][col].color == Color.NONE:
                        field[row][col].color = field[row][col + 1].color
                        field[row][col + 1].color = Color.NONE
                        row = row + 1

    return field


def column_is_empty(field, column):
    for i in range(len(field)):
        if field[i][column].color != Color.NONE:
            return False
    return True


def shuffle(field):
    colors = [Color.RED, Color.BLUE, Color.GREEN]
    balls_poses = count_balls_and_found_pos(field)
    if len(balls_poses) > 10:
        for i in range(len(balls_poses)):
            field[balls_poses[i][0]][balls_poses[i][1]].color = colors[random.randint(0, 2)]
    elif len(balls_poses) > 4:
        for i in range(len(balls_poses)):
            field[balls_poses[i][0]][balls_poses[i][1]].color = colors[random.randint(0, 1)]
    else:
        for i in range(len(balls_poses)):
            field[balls_poses[i][0]][balls_poses[i][1]].color = colors[0]


def count_balls_and_found_pos(field):
    poses = []
    for i in range(len(field)):
        for j in range(len(field) * 2):
            if field[i][j].color != Color.NONE:
                poses.append((i, j))
    return poses
