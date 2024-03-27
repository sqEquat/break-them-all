from Residue import Residue


class Peak:
    def __init__(self, from_str: str, res_dict: dict):
        if res_dict is not None:
            key_res_num1 = int(from_str.split()[1])
            key_res_name1 = res_dict[key_res_num1]
            key_res_atom1 = from_str.split()[0]

            key_res_num2 = int(from_str.split()[3])
            key_res_name2 = res_dict[key_res_num2]
            key_res_atom2 = from_str.split()[2]

            self.first = Residue(key_res_num1, key_res_name1, key_res_atom1)
            self.second = Residue(key_res_num2, key_res_name2, key_res_atom2)
        else:
            self.first = Residue(int(from_str.split()[0]), from_str.split()[1], from_str.split()[2])
            self.second = Residue(int(from_str.split()[3]), from_str.split()[4], from_str.split()[5])

    def __str__(self):
        return f'{self.first} {self.second}'

    def __eq__(self, other):
        if isinstance(other, Peak):
            return (self.first, self.second) == (other.first, other.second)
        else:
            return False

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))