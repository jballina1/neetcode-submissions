class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_group(group):
            d = {}
            for n in group:
                d[n] = d.get(n,0) + 1
            for k,v in d.items():
                if k != '.' and v > 1:
                    return False
            return True
        
        #check rows
        for row in board:
            if not check_group(row):
                return False
        
        #check columns
        columns = []
        for i in range(len(board)):
            col = []
            for j in range(len(board[i])):
                col.append(board[j][i])
            columns.append(col)
        for col in columns:
            if not check_group(col):
                return False

        #check box
        boxes = []
        tl = [[0,0],[3,0],[6,0],[0,3],[0,6],[3,3],[3,6],[6,3],[6,6]]
        for point in tl:
            box = []
            for i in range(point[0], point[0] + 3):
                for j in range(point[1], point[1] + 3):
                    box.append(board[i][j])
            boxes.append(box)
        for box in boxes:
            if not check_group(box):
                return False
            
        return True


            