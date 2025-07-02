import tkinter as tk

# --- N-Queens Solver (Backtracking) ---
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens_util(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0

def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

# --- Tkinter Visualization ---
CELL_SIZE = 50

def draw_board(canvas, board):
    canvas.delete("all")
    n = len(board)
    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill=color)
            if board[i][j] == 1:
                canvas.create_text(j*CELL_SIZE + CELL_SIZE//2, i*CELL_SIZE + CELL_SIZE//2, text="♛", font=("Arial", 24), fill="red")

def next_solution():
    global solution_index
    solution_index = (solution_index + 1) % len(solutions)
    draw_board(canvas, solutions[solution_index])

def prev_solution():
    global solution_index
    solution_index = (solution_index - 1) % len(solutions)
    draw_board(canvas, solutions[solution_index])

def main(n):
    global canvas, solutions, solution_index
    root = tk.Tk()
    root.title(f"{n}-Queens Visualizer")
    canvas = tk.Canvas(root, width=n*CELL_SIZE, height=n*CELL_SIZE)
    canvas.pack()

    nav_frame = tk.Frame(root)
    nav_frame.pack()

    tk.Button(nav_frame, text="⟨ Prev", command=prev_solution).pack(side=tk.LEFT, padx=10)
    tk.Button(nav_frame, text="Next ⟩", command=next_solution).pack(side=tk.LEFT, padx=10)

    solutions = solve_nqueens(n)
    if not solutions:
        print("No solution found!")
        return
    solution_index = 0
    draw_board(canvas, solutions[0])
    root.mainloop()

if __name__ == "__main__":
    try:
        n = int(input("Enter the value of N (e.g., 4 or 8): "))
        main(n)
    except Exception as e:
        print("Error:", e)
