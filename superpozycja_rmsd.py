from Bio.PDB import PDBParser, Superimposer
import numpy as np

def calculate_rmsd(atoms1, atoms2):
    sum_of_squares = 0
    for atom1, atom2 in zip(atoms1, atoms2):
        distance = atom1.coord - atom2.coord
        sum_of_squares += np.dot(distance, distance)

    rmsd = np.sqrt(sum_of_squares / len(atoms1))
    return rmsd

def get_matching_atoms(structure1, structure2):
    atoms1 = [atom for atom in structure1.get_atoms() if atom.name in ['P', 'C4\'', 'C1\'']]
    atoms2 = [atom for atom in structure2.get_atoms() if atom.name in ['P', 'C4\'', 'C1\'']]

    # Dopasowanie atomów
    matched_atoms1 = []
    matched_atoms2 = []
    for atom1 in atoms1:
        for atom2 in atoms2:
            if atom1.get_parent().get_id() == atom2.get_parent().get_id() and atom1.name == atom2.name:
                matched_atoms1.append(atom1)
                matched_atoms2.append(atom2)
                break

    return matched_atoms1, matched_atoms2

parser = PDBParser(QUIET=True)
reference_structure = parser.get_structure("reference", "R1107_reference.pdb")
models_structure = parser.get_structure("models", "R1107TS081.pdb")

for model in models_structure:
    ref_atoms, model_atoms = get_matching_atoms(reference_structure[0], model)
    if ref_atoms and model_atoms:
        # superpozycja
        super_imposer = Superimposer()
        super_imposer.set_atoms(ref_atoms, model_atoms)
        super_imposer.apply(model.get_atoms())

        # RMSD
        rmsd = calculate_rmsd(ref_atoms, model_atoms)
        print(f"RMSD dla modelu {model.id}: {rmsd}")
    else:
        print(f"Niewystarczająca liczba dopasowanych atomów dla modelu {model.id}")

