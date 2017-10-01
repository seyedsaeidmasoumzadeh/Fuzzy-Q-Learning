

class Build(object):
    list_of_input_variable = []

    def __init__(self,*args):
        self.list_of_input_variable = args

    def get_input(self):
        return self.list_of_input_variable

    def get_number_of_rulls(self):
        number_of_rulls = 1
        for input_variable in self.list_of_input_variable:
            number_of_rulls = (number_of_rulls * self.get_number_of_fuzzy_sets(input_variable))
        return number_of_rulls

    def get_number_of_fuzzy_sets(self, input_variable):
        return len(input_variable.get_fuzzy_sets())
