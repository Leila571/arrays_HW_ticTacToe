'''
Leila Lopez Marks
10/6/2020
Arrays Tic Tac Toe HW
'''

vertical = [' | | ']
horizontal = [' - - - ']

def board():
    for i in range(3):
        print(vertical[0])
        if i < 2:
            print(horizontal[0])

board()
