class Knight():
    def __init__(self, name):
        self._name = name
        with open('knights.txt') as knights:
            for rLine in knights:
                line = rLine.strip()
                name, title, color, quest, comment = line.split(":")
                if name == self._name:
                    self._title = title
                    self._favorite_color = color
                    self._quest = quest
                    self._comment = comment
                    break


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    
    @property
    def favorite_color(self):
        return self._favorite_color
    
    @property
    def quest(self):
        return self._quest
    
    @property
    def comment(self):
        return self._comment
    
    # def print(self)
    #     print(self.title, self.name, self.quest, self.fav_color, self._comment)