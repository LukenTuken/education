class Cell:
    #  Инициализация клетки
    def __init__(self, index, symbol=' ', fullness=False):
        self.index = index
        self.symbol = symbol
        self.fullness = fullness


class Board:
    # Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        # Создаем поле с клетками
        self.playing_field = [Cell(index) for index in range(1, 10)]
        # Создаем список со значениями
        self.symbol_on_board = [element.symbol for element in self.playing_field]

    # Метод, который меняет значение поля на занятое, изначально False(не занята)
    def change_cell(self, index):
        if self.playing_field[index - 1].fullness:
            return False
        else:
            self.playing_field[index - 1].fullness = True
            return True

    # Метод проверки окончания игры
    def end_of_game(self):
        start = 0
        for i in range(3):
            # Проверяем все горизонтали
            if self.symbol_on_board[start:start + 3] in (['O', 'O', 'O'], ['X', 'X', 'X']):
                return True
            # Проверяем все вертикали
            elif self.symbol_on_board[i:i + 7:3] in (['O', 'O', 'O'], ['X', 'X', 'X']):
                return True
            start += 3

        # Проверяем диагональ справа налево
        if self.symbol_on_board[0:9:4] in (['O', 'O', 'O'], ['X', 'X', 'X']):
            return True
        # Проверяем диагональ слева направо
        elif self.symbol_on_board[2:7:2] in (['O', 'O', 'O'], ['X', 'X', 'X']):
            return True
        else:
            # Если проверки не удались возвращаем False
            return False

    # Метод-подсказка выводящий поле с номерами клеток
    def print_board_info(self):
        start = 0
        for _ in range(3):
            print(f' | {start + 1} | {start + 2} | {start + 3} | ')
            print('_______________')
            start += 3

    # Метод выводящий поле с текущими значениями
    def print_board_result(self):
        start = 0
        for _ in range(3):
            print(f' | {self.symbol_on_board[start]} | {self.symbol_on_board[start + 1]} |'
                  f' {self.symbol_on_board[start + 2]} | ')
            print('_______________')
            start += 3


class Player:
    # Инициализируем класс Игрок
    def __init__(self, index, name, number_of_victories=0):
        self.index = index
        self.name = name
        self.number_of_victories = number_of_victories

    # Метод проверки введенного числа поля
    def make_move(self):
        while True:
            cell_number = int(input('Введите номер клетки куда хотите сходить от 1 до 9: '))
            if isinstance(cell_number, int):
                if cell_number in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                    return cell_number
            else:
                print('Ошибка ввода, введите число от 1 до 9!')


class Game:
    # Инициализация класса Игра
    # Создаем, двух игроков и игровое поле

    players = [Player(index, input(f'Введите имя {index}-го игрока: ')) for index in range(1, 3)]
    field_of_play = Board()

    # Метод одного хода, запрашиваем у игрока ход, проверяем доступность клетки, если доступна записываем Х или О
    def one_move(self, player_number):
        print('Ходит {}-й игрок!'.format(player_number))
        while True:
            move = self.players[player_number - 1].make_move()
            if self.field_of_play.change_cell(move):
                if player_number == 1:
                    self.field_of_play.symbol_on_board[move - 1] = 'X'
                    print(self.field_of_play.symbol_on_board)
                    break
                else:
                    self.field_of_play.symbol_on_board[move - 1] = 'O'
                    print(self.field_of_play.symbol_on_board)
                    break
            else:
                print('Клетка занята, сделайте другой ход!')

        # Выводим поле с текущими значениями и проверяем закончена ли игра
        self.field_of_play.print_board_result()
        if self.field_of_play.end_of_game():
            return True

    # Метод одной игры, создаем чистое поле, запрашиваем ход игрока 1, если победил записываем очко победы,
    # проверяем поле на ничью, запрашиваем ход второго игрока
    def one_game(self):
        self.field_of_play = Board()
        while True:
            first_gamer = self.one_move(1)
            if first_gamer:
                print('Победил игрок 1')
                self.players[0].number_of_victories += 1
                return True

            field_fullness = [self.field_of_play.playing_field[index].fullness for index in range(9)]
            if all(field_fullness):
                print('Ничья')
                return True

            second_gamer = self.one_move(2)
            if second_gamer:
                print('Победил игрок 2')
                self.players[1].number_of_victories += 1
                return True

    # Метод основной игры в бесконечном цикле, запускаем игру,
    # выводим информацию о количестве побед, запрашиваем хотят ли участники играть дальше
    def start_game(self):
        print('Номера клеток поля!')
        self.field_of_play.print_board_info()
        while True:
            if self.one_game():
                print('Текущий счет:\nИгрок 1 побед: {}\nИгрок 2 побед: {}'.format(
                    self.players[0].number_of_victories, self.players[1].number_of_victories)
                )
            question = input('Хотите сыграть еще?Y|N: ').lower()
            if question == 'y':
                continue
            else:
                break


tic_tac_toe = Game()
tic_tac_toe.start_game()
