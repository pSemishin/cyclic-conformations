from gsdc import Box, Mol, Pot
import os

if __name__ == "__main__":
    direct = 'N=200_g=3_n=7'
    os.mkdir(direct)
    my_cwd = os.getcwd()
    path = os.path.join(my_cwd, direct)
    os.chdir(path)
    S = '(B)7[(B)7[(B)7[(B)7](B)7][(B)7](B)7](B)7[(B)7[(B)7](B)7](B)7[(B)7](B)7'   #definition of side chain
    script = '(A)1[' + S + ']((A)1[' + S + '])198(A)1' + S #main chain + side chain
    mol = Mol(script)
    num_last_A = "".join(mol.types).rindex("A")
    mol.bonds.append((0, num_last_A)) #add cyclic bond
    pot = Pot(Box(60.0, 60.0, 60.0))
    pot.add(mol)
    pot.fuller("W")
    pot.brew()
    # print(mol.bonds)
    os.chdir(my_cwd)
    # print(script)