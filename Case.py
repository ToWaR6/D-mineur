class Case:

    def __init__(self, val='0', opened=False):
        self.value = val
        self.opened = opened

    def has_mine(self):
        return self.value == 'X'

    def is_empty(self):
        return self.value == '0'

    def set_mine(self):
        self.value = 'X'

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value

    def is_opened(self):
        return self.opened

    def open(self):
        self.opened = True
