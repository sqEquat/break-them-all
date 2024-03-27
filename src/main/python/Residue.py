class Residue:
    def __init__(self, res_num: int, res_name: str, res_part: str):
        self.res_num = res_num
        self.res_name = res_name
        self.res_atom = res_part

    def __str__(self):
        return f'{self.res_num} {self.res_name} {self.res_atom}'

    def __eq__(self, other):
        if isinstance(other, Residue):
            return (self.res_name, self.res_atom) == (other.res_name, other.res_atom)
        else:
            return False

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))