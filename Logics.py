class SelfLearning:
    def __init__(self):
        pass

    def add_skill(self):
        pass

    def view_skill(self):
        pass


class AddedKills(SelfLearning):
    def __init__(self):
        self.skill = []

    def add_skill(self, code):
        if code == 0:
            return "Enter correct code"
        else:
            self.code += code
            return self.code