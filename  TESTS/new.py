class start:

    def __init__(self, name, start, mission, version, objective):
        # SET START TO 1
        self.name = name
        self.start = start
        self.mission = mission
        self.version = version
        self.objective = objective

    def __str__(self):
        return f'The current operating system is [{self.name}] and objective is to [{self.objective}]'

    def __repr__(self):
        return f'OS(\'{self.name}\', {self.version})'
    def function(self):
        return f"good day"



LOLA = start("LOLA",1, "go to mars",2,"Complete my mission without raising any errors")

print(str(LOLA))
print(repr(LOLA))
print(function)