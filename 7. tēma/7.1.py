"""7.1. Meklēšanas pamati."""

import random


def linear_search(saraksts, mekletais):
    """Atgriež pirmās atbilstības indeksu un pārbaudīto elementu skaitu."""
    soli = 0
    for i, elements in enumerate(saraksts):
        soli += 1
        if elements == mekletais:
            return i, soli
    return -1, soli


def binary_search(saraksts, mekletais):
    """Meklē augošā secībā sakārtotā sarakstā un atgriež indeksu un soļus."""
    apaksa = 0
    augsa = len(saraksts) - 1
    soli = 0

    while apaksa <= augsa:
        soli += 1
        vidus = (apaksa + augsa) // 2
        if saraksts[vidus] == mekletais:
            return vidus, soli
        elif saraksts[vidus] < mekletais:
            apaksa = vidus + 1
        else:
            augsa = vidus - 1

    return -1, soli


def main():
    lielakais_id = 10000
    saraksts = [random.randint(1, lielakais_id) for _ in range(20)]
    mekletais = saraksts[10]
    neesosais = lielakais_id + 1

    print("1. Lineārā meklēšana nesakārtotā sarakstā")
    print("Nejaušie ID", saraksts)
    indekss, soli = linear_search(saraksts, mekletais)
    print(f"ID {mekletais} atrasts indeksā {indekss} ({soli} soļi).")
    indekss, soli = linear_search(saraksts, neesosais)
    print(f"Neesošam ID {neesosais} indekss ir {indekss} ({soli} soļi).")

    print("\n2. Meklēšana sakārtotā sarakstā")
    saraksts.sort()
    print("Sakārtotie ID", saraksts)
    linearais_indekss, linearie_soli = linear_search(saraksts, mekletais)
    binarais_indekss, binarie_soli = binary_search(saraksts, mekletais)
    print(f"Lineārā atrada ID {saraksts[linearais_indekss]} indeksā "
          f"{linearais_indekss} ({linearie_soli} soļi).")
    print(f"Binārā atrada ID {saraksts[binarais_indekss]} indeksā "
          f"{binarais_indekss} ({binarie_soli} soļi).")

    print("\n3. Soļu skaita salīdzinājums")
    lielais_saraksts = saraksts + [random.randint(1, lielakais_id) for _ in range(980)]
    lielais_saraksts.sort()

    # ID ir lielāks par visiem saraksta elementiem, tāpēc rezultāti atkārtojas.
    _, linearie_20 = linear_search(saraksts, neesosais)
    _, binarie_20 = binary_search(saraksts, neesosais)
    _, linearie_1000 = linear_search(lielais_saraksts, neesosais)
    _, binarie_1000 = binary_search(lielais_saraksts, neesosais)
    print(f"Abos sarakstos meklējam neesošu ID {neesosais}.")
    print(f"20 elementi — lineārā {linearie_20}, binārā {binarie_20} soļi.")
    print(f"1000 elementi — lineārā {linearie_1000}, binārā {binarie_1000} soļi.")
    print(f"Lineārajai soļu skaits pieauga {linearie_1000 / linearie_20:g} reizes.")
    print(f"Binārajai soļu skaits pieauga {binarie_1000 / binarie_20:g} reizes.")
    print("Binārajai meklēšanai vajag sakārtotu sarakstu, jo tikai tad pēc "
          "salīdzinājuma ar vidējo elementu var droši atmest vienu saraksta pusi.")

    print("\nPapilduzdevums ar index()")
    indekss = saraksts.index(mekletais)
    print(f"ID {mekletais} ar index() un lineāro meklēšanu atrasts "
          f"indeksā {indekss} (linear_search atgrieza {linearais_indekss}).")
    try:
        saraksts.index(neesosais)
    except ValueError as kluda:
        print(f"ValueError — {kluda}")
    indekss, soli = linear_search(saraksts, neesosais)
    print(f"Ja ID nav sarakstā, index() izraisa ValueError, bet linear_search "
          f"atgriež indeksu {indekss} un soļu skaitu {soli}.")


if __name__ == "__main__":
    main()
