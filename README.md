**CLASHCORE**

Ten skrypt oblicza Clash Score struktury białka poprzez analizę nakładania się atomów bazując między innymi na promieniach Van der Waalsa. 
Skrypt wykorzystuje moduł Bio.PDB z biblioteki Biopython do parsowania struktur białkowych oraz przeprowadzania wyszukiwania sąsiednich par atomów.

**Wymagania** 
- Python w wersji 3.x
- Pakiet Biopython (pip install biopython)
    
**Kod**
- Ekstrahuje listę atomów ze struktury.
- Wykorzystuje NeighborSearch do identyfikacji sąsiadujących atomów w określonym promieniu.
- Sprawdza pary atomów pod kątem zderzeń na podstawie ich promieni Van der Waalsa i odległości.
- Ignoruje pary atomów z tej samej reszty lub te, które są oddzielone o mniej niż dwa nukleotydy, aby uniknąć fałszywych pozytywów.
- Oblicza liczbę "złych" nakładających się atomów, gdzie atomy są zbyt blisko siebie.
- Wyjście: ClashScore obliczany jako (1000 * liczba złych nakładających się atomów) / całkowita liczba atomów.


Skrypt oblicza Clash Score dla struktury białka, sprawdzane jest, czy suma promieni Van der Waalsa obu atomów, 
pomniejszona o ich odległość, jest większa lub równa 0.4 Å (angstrema). Jest to próg, który określa, czy atomy są zbyt blisko siebie, co może sugerować zderzenie (clash).
Jeśli warunek jest spełniony (tj. atomy są zbyt blisko siebie), zwiększany jest licznik number_of_bad_overlaps, który śledzi liczbę takich zderzeń, aby finalnie obliczyć ClashScore jako
(1000 * liczba złych nakładających się atomów) / całkowita liczba atomów.

**Niższy wynik wskazuje na mniej sterycznych zderzeń, sugerując bardziej fizycznie prawdopodobną strukturę.**


**Superpozycja, RMSD**


Skrypt wykorzystuje moduł Bio.PDB z biblioteki Biopython oraz bibliotekę NumPy do obliczania Root Mean Square Deviation (RMSD) pomiędzy dwoma strukturami białkowymi. 
Głównym celem jest ocena podobieństwa strukturalnego przez superpozycję i porównanie kluczowych atomów w obu strukturach.

**Wymagania**
- Python w wersji 3.x
- Biblioteka Biopython (instalacja: pip install biopython)
- Biblioteka NumPy (instalacja: pip install numpy)


  **Funkcja calculate_rmsd(atoms1, atoms2)**
  Przechodzi przez odpowiadające sobie atomy (atom1 i atom2) z dwóch różnych struktur, oblicza kwadrat ich odległości, sumuje te wartości, a następnie oblicza pierwiastek kwadratowy ze średniej tych sum.

  **Funkcja get_matching_atoms(structure1, structure2)**
Wybiera atomy z obu struktur (structure1 i structure2)
Dopasowuje atomy między dwiema strukturami na podstawie identyfikatorów ich rodziców (zwykle reszt) i nazw atomów.
Zwraca listy dopasowanych atomów z obu struktur.

**Iteracja po modelach i obliczanie RMSD:**
Dla każdego modelu w strukturze modeli (models_structure) wykonuje następujące kroki:
- Znajduje dopasowane atomy między strukturą referencyjną a aktualnym modelem.
- Jeśli istnieją dopasowane atomy:
- Używa Superimposer do ustawienia modelu w taki sposób, aby jak najlepiej pasował do struktury referencyjnej. Jest to proces nazywany superpozycją, który minimalizuje odległość między odpowiadającymi sobie atomami.
- Oblicza RMSD pomiędzy dopasowanymi atomami struktury referencyjnej i modelu.
- Wypisuje RMSD dla danego modelu.
  W przypadku niewystarczającej liczby dopasowanych atomów, wyświetla stosowny komunikat.
  
RMSD służy jako miara podobieństwa strukturalnego między różnymi konformacjami białka. 
Superpozycja struktur jest kluczowym etapem w obliczaniu RMSD, pozwalającym na precyzyjne porównanie odpowiadających sobie atomów w obu strukturach.
