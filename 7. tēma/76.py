"""Skaitļa minēšanas spēle ar bināro meklēšanu."""


def aprekinat_minejumu(apaksa, augsa):
    """Atgriež iespējamā diapazona vidējo veselo skaitli."""
    return (apaksa + augsa) // 2


def nolasit_atbildi(minejums):
    """Prasa atbildi atkārtoti, līdz spēlētājs ievada derīgu komandu."""
    while True:
        atbilde = input(
            f"Vai tavs skaitlis ir {minejums}? "
            "(lielaks/mazaks/pareizi): "
        ).strip().lower()

        if atbilde in ("lielaks", "mazaks", "pareizi"):
            return atbilde

        print("Nederīga atbilde! Ievadi lielaks, mazaks vai pareizi.")


def spelet(apaksa=1, augsa=100):
    """Vada spēli, skaita minējumus un pamana pretrunīgas atbildes."""
    print("Koda lauzējs: AI efektivitāte")
    print(f"Iedomājies veselu skaitli no {apaksa} līdz {augsa}.")
    print("Pašu skaitli neievadi. Atbildi uz datora minējumiem:")
    print("lielaks — tavs skaitlis ir lielāks par datora minējumu;")
    print("mazaks — tavs skaitlis ir mazāks par datora minējumu;")
    print("pareizi — dators ir uzminējis tavu skaitli.")

    minejumi = 0

    while True:
        # Ja diapazons ir tukšs, visas atbildes nevar būt patiesas.
        if apaksa > augsa:
            print("Atbildes ir pretrunīgas! Iespējamu skaitļu vairs nav.")
            print(f"Spēle pārtraukta. Minējumu skaits: {minejumi}.")
            break

        minejums = aprekinat_minejumu(apaksa, augsa)
        minejumi += 1
        print(f"\n{minejumi}. minējums. Diapazons: {apaksa}–{augsa}.")
        atbilde = nolasit_atbildi(minejums)

        if atbilde == "pareizi":
            print(f"Uzminēju! Tavs skaitlis ir {minejums}.")
            print(f"Minējumu skaits: {minejumi}.")
            break
        elif atbilde == "lielaks":
            apaksa = minejums + 1
        else:
            augsa = minejums - 1


if __name__ == "__main__":
    spelet()
