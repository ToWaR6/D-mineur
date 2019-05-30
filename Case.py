class Case:

    def __init__(self, value='0', opened=False, flag=False):
        self.value = value
        self.opened = opened
        self.flagged = flag
        self.exploded = False

    def has_mine(self):
        return self.value == 'X'

    def is_empty(self):
        return self.value == '0'

    def set_mine(self):
        self.value = 'X'

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def is_opened(self):
        return self.opened

    def open(self):
        self.opened = True

    def is_flag(self):
        return self.flagged

    def toggle_flag(self):
        if self.flagged:
            self.flagged = False
        else:
            self.flagged = True

    def has_explode(self):
        return self.exploded

    def explode(self):
        self.exploded = True
