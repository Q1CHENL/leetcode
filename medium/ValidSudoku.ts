function isValidSudoku(board: string[][]): boolean {
    // check rows
    for (let i = 0; i < 9; i++) {
        let filtered: string[] = board[i].filter(str => str != ".");
        if (filtered.length !== new Set(filtered).size) {
            return false
        }
    }
    // check columns
    for (let i = 0; i < 9; i++) {
        let column: string[] = []
        for (let j = 0; j < 9; j++) {
            if (board[j][i] !== ".") {
                column.push(board[j][i])
            }
        }
        if (column.length !== new Set(column).size) {
            return false
        }
    }
    // check boxes
    for (let i = 0; i < 9; i += 3) {
        for (let j = 0; j < 9; j += 3) {
            let box: string[] = []
            for (let n = i; n < i + 3; n += 1) {
                for (let m = j; m < j + 3; m += 1) {
                    if (board[n][m] !== ".") {
                        box.push(board[n][m])
                    }
                }
            }
            if (box.length !== new Set(box).size) {
                return false
            }
        }
    }
    return true
};

// An interesting answer from LeetCode w/ my modification of the Sets' initialization
// function isValidSudoku(board: string[][]): boolean {
//     const cols: Set<string>[] = Array.from({ length: 9 }, () => new Set<string>());
//     const rows: Set<string>[] = Array.from({ length: 9 }, () => new Set<string>());
//     const boxes: Set<string>[] = Array.from({ length: 9 }, () => new Set<string>());
    
//     const getBoxNum = (x, y) => 3 * Math.floor(x / 3) + Math.floor(y / 3);

//     for (let x = 0; x < 9; x++) {
//         for (let y = 0; y < 9; y++) {
//             if (board[x][y] == '.') continue;
//             if (rows[y].has(board[x][y])) return false;
//             rows[y].add(board[x][y]);
//             if (cols[x].has(board[x][y])) return false;
//             cols[x].add(board[x][y]);
//             const box = boxes[getBoxNum(x, y)];
//             if (box.has(board[x][y])) return false;
//             box.add(board[x][y]);
//         }
//     }
//     return true;
// };

let board =
    [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

console.log(isValidSudoku(board))
