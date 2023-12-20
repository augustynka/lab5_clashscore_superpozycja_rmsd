from Bio.PDB import PDBParser, NeighborSearch

vdw_radii = {
    "H": 1.2,
    "C": 1.7,
    "N": 1.55,
    "O": 1.52,

}

def calculate_clash_score(structure):
    number_of_bad_overlaps = 0
    atoms = list(structure.get_atoms())
    number_of_atoms = len(atoms)
    neighbor_search = NeighborSearch(atoms)
    checked_pairs = set()

    for atom in atoms:
        residue = atom.get_parent()
        for other_atom in neighbor_search.search(atom.coord, 4, level='A'):
            other_residue = other_atom.get_parent()

            # identyfikator pary atomów
            atom_pair = frozenset([atom, other_atom])

            # sprawdzanie, czy para atomów została już wcześniej rozpatrzona
            if atom_pair in checked_pairs:
                continue
            checked_pairs.add(atom_pair)

            # sprawdzanie, czy atomy pochodzą z tej samej reszty lub są oddzielone o mniej niż dwa nukleotydy
            if residue == other_residue or abs(residue.id[1] - other_residue.id[1]) < 2:
                continue


            distance = atom - other_atom


            vdw_radius1 = vdw_radii.get(atom.element, 1.5)
            vdw_radius2 = vdw_radii.get(other_atom.element, 1.5)


            if (vdw_radius1 + vdw_radius2 - distance) >= 0.4:
                number_of_bad_overlaps += 1


    clash_score = (1000 * number_of_bad_overlaps) / number_of_atoms
    return clash_score

pdb_parser = PDBParser()
structure = pdb_parser.get_structure("model", "R1107_reference.pdb")


clash_score = calculate_clash_score(structure)
print("Clash Score: {:.2f}".format(clash_score))
