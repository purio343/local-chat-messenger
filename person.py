class Person:
    def __init__(self, name, address, job):
       self.name = name
       self.address = address
       self.job = job

    def introduce(self):
       string = f'私の名前は{self.name}です。\n{self.address}に住んでいて、{self.job}として働いています。'
       return string