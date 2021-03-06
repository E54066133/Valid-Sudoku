class Sudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):                                                          # 產生九宮格
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    for i_index in range(9):                                        # 檢查直欄
                        if i_index != i and board[i_index][j] == board[i][j]:
                            return False
                    
                    for j_index in range(9):                                        # 檢查橫列
                        if j_index != j and board[i][j_index] == board[i][j]:
                            return False
                    
                    # check square                                                  # 檢查九宮格
                    for i_index in range(3):
                        for j_index in range(3):
                            if (i_index + int(i / 3) * 3) != i and (j_index + int(j / 3) * 3) != j and board[i][j] == board[i_index + int(i / 3) * 3][j_index + int(j / 3) * 3]:
                                return False
        return True
