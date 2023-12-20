#CLASHCORE

Ten skrypt oblicza Clash Score struktury białka poprzez analizę nakładania się atomów bazując między innymi na promieniach Van der Waalsa. 
Skrypt wykorzystuje moduł Bio.PDB z biblioteki Biopython do parsowania struktur białkowych oraz przeprowadzania wyszukiwania sąsiednich par atomów.

#Wymagania
    Python w wersji 3.x
    Pakiet Biopython (pip install biopython)
    
#Kod
    Ekstrahuje wszystkie atomy ze struktury.
    Wykorzystuje NeighborSearch do identyfikacji sąsiadujących atomów w określonym promieniu.
    Sprawdza pary atomów pod kątem zderzeń na podstawie ich promieni Van der Waalsa i odległości.
    Ignoruje pary atomów z tej samej reszty lub te, które są oddzielone o mniej niż dwa nukleotydy, aby uniknąć fałszywych pozytywów.
    Oblicza liczbę "złych" nakładających się atomów, gdzie atomy są zbyt blisko siebie.
    Wyjście: ClashScore obliczany jako (1000 * liczba złych nakładających się atomów) / całkowita liczba atomów.


Skrypt oblicza Clash Score dla struktury białka, sprawdzane jest, czy suma promieni Van der Waalsa obu atomów, 
pomniejszona o ich odległość, jest większa lub równa 0.4 Å (angstrema). Jest to próg, który określa, czy atomy są zbyt blisko siebie, co może sugerować zderzenie (clash).
Jeśli warunek jest spełniony (tj. atomy są zbyt blisko siebie), zwiększany jest licznik number_of_bad_overlaps, który śledzi liczbę takich zderzeń, aby finalnie obliczyć ClashScore jako
(1000 * liczba złych nakładających się atomów) / całkowita liczba atomów.
Niższy wynik wskazuje na mniej sterycznych zderzeń, sugerując bardziej fizycznie prawdopodobną strukturę.
