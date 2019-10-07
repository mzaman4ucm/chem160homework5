## Define dictionary
atoms = ["C", "H", "O", "N", "P", "S"]
masses = [12.0107,1.00794,15.9994,14.00674,30.973761,32.066]
Dict=dict(zip(atoms,masses))


def molemass2(s):
    atom = 0
    mass = 0
    for i in s:
        a = i
        if a.isdigit() == True:
            num=int(a)
            multi_atom = single_atom*num
            mass = mass + multi_atom - single_atom
        else:
            single_atom = Dict[a]
            mass = mass + single_atom
    return mass
