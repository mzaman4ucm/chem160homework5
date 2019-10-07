## Define dictionary
atoms = ["C", "H", "O", "N", "P", "S"]
masses = [12.0107,1.00794,15.9994,14.00674,30.973761,32.066]
Dict=dict(zip(atoms,masses))


def molemass(s):
    mass = 0
    for i in s:
        mass = mass + Dict[i]
    return mass
