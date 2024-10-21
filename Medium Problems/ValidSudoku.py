#Makar Borisov 10/10/24
#Granted this was an 'easy' exercise, altho leet said medium, but I got it fairly quickly and it had my best runtime percentile so far! Very happy with how it turned out.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        #here we initialize the array with the numbers in each row, column and 3x3 'tile', the tiles are represented in a two dimentional array for convenience.
        explode = [ ['']*9 for i in range(3)] + [['']*3 for i in range(2)]
        for row in range(0,9):
            for elem in range(0,9):

                #going through each of the elements of the board
                element=board[row][elem]
                if element=='.':
                    continue

                #check if the element already appears in it's row/column/tile.
                #I used a 2-D array since the tile must be dependant both on the horrizontal and vertical position of the element.
                if element in explode[0][row]+explode[1][elem]+explode[2+row//3][elem//3]:
                    return False

                #if the element is not repeated, it gets added to it's correspondant row, column and tile.
                explode[0][row]+=element
                explode[1][elem]+=element
                explode[2+row//3][elem//3]+=element
        return True
