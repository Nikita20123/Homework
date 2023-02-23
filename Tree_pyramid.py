class Make_tree:
    '''Создает Ёлку'''
    def __init__(self, ) :
        '''Здесь сохраняется ввод юзера'''
        self.height = " "
        self.pin = " "

    def tree(self):
        '''Создается елка по параметрам юзера'''
        for pyramid in range(self.height + 1):
            print(' ' * (self.height - pyramid), self.pin * (2 * pyramid + 1))

answer = Make_tree()

answer.height = int(input('Какая высота нужна?: '))
answer.pin = input('Какой значок пирамиды: ')

answer.tree()