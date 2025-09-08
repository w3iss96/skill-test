def print_board(board):
    # Функция для вывода игрового поля
    for row in board:
        print(f"| {' | '.join(row)} |")
        print("-" * 9)


def check_winner(board, player):
    # Проверка победы
    # Проверка строк
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Проверка столбцов
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def main():
    # Инициализация поля
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for move in range(9):
        print_board(board)
        print(f"Ход игрока {current_player}")

        # Ввод координат
        while True:
            try:
                row = int(input("Введите номер строки (0-2): "))
                col = int(input("Введите номер столбца (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Неверный ввод. Попробуйте снова.")
            except ValueError:
                print("Введите числа!")

        # Проверка победы
        if check_winner(board, current_player):
            print_board(board)
            print(f"Победил игрок {current_player}!")
            return

        # Смена игрока
        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("Ничья!")


if __name__ == "__main__":
    main()