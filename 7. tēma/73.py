"""7.3. Big O un sarežģītība."""

import time


def iegut_pirmo(dati):
    return dati[0]


def pirmais_ar_skaitu(dati):
    operacijas = 0
    pirmais = iegut_pirmo(dati)
    operacijas += 1
    return pirmais, operacijas


def viens_cikls(dati):
    summa = 0
    operacijas = 0
    for skaitlis in dati:
        summa += skaitlis
        operacijas += 1
    return summa, operacijas


def divi_cikli(dati):
    operacijas = 0
    for pirmais in dati:
        for otrais in dati:
            operacijas += 1  # Viens solis katram elementu pārim.
    return operacijas


def videjais_laiks(funkcija, dati, atkartojumi):
    """Izmēra vairākus izsaukumus, lai varētu salīdzināt arī īsas darbības."""
    sakums = time.time()
    for _ in range(atkartojumi):
        funkcija(dati)
    beigas = time.time()
    return (beigas - sakums) / atkartojumi


# Binārā meklēšana no 7.1. nodarbības.
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
    print("1. Piekļuve pirmajam elementam, O(1)")
    mazie_dati = list(range(10))
    lielie_dati = list(range(1_000_000))
    mazais_laiks = videjais_laiks(iegut_pirmo, mazie_dati, 100_000)
    lielais_laiks = videjais_laiks(iegut_pirmo, lielie_dati, 100_000)
    print(f"10 elementi — vidēji {mazais_laiks:.10f} s vienā izsaukumā.")
    print(f"1 000 000 elementu — vidēji {lielais_laiks:.10f} s vienā izsaukumā.")
    print("Pirmā elementa nolasīšanas laiks nepieaug līdzi saraksta garumam. "
          "Abos sarakstos jāveic viena piekļuve pēc indeksa.")

    print("\n2. Viens cikls pret diviem ligzdotiem cikliem")
    linearie_laiki = []
    kvadratiskie_laiki = []
    for n in (100, 1000):
        dati = list(range(n))
        linearais_laiks = videjais_laiks(viens_cikls, dati, 500)
        kvadratiskais_laiks = videjais_laiks(divi_cikli, dati, 5)
        linearie_laiki.append(linearais_laiks)
        kvadratiskie_laiki.append(kvadratiskais_laiks)
        print(f"{n:4} elementi — O(n) {linearais_laiks:.8f} s, "
              f"O(n²) {kvadratiskais_laiks:.8f} s.")

    linearais_pieaugums = linearie_laiki[1] / linearie_laiki[0]
    kvadratiskais_pieaugums = kvadratiskie_laiki[1] / kvadratiskie_laiki[0]
    print(f"Izmērītais laika pieaugums — O(n) {linearais_pieaugums:.1f} reizes, "
          f"O(n²) {kvadratiskais_pieaugums:.1f} reizes.")
    print("Palielinot n 10 reizes, divu ciklu darba apjoms aug 100 reizes, "
          "bet viena cikla darba apjoms aug 10 reizes.")

    print("\n3. Big O pārbaude ar operāciju skaitītājiem")
    print("Minējumi — piekļuve pēc indeksa O(1), viens cikls O(n), "
          "divi ligzdoti cikli O(n²).")
    for n in (10, 100):
        dati = list(range(n))
        _, konstants = pirmais_ar_skaitu(dati)
        _, linears = viens_cikls(dati)
        kvadratisks = divi_cikli(dati)
        print(f"{n:3} elementi — O(1) {konstants}, O(n) {linears}, "
              f"O(n²) {kvadratisks} operācijas.")
    print("Skaitītāji apstiprina minējumus. Big O raksturo darba apjoma "
          "pieaugumu, bet sekundes ietekmē datora ātrums un noslodze.")

    print("\nPapilduzdevums — binārā meklēšana, O(log n)")
    ieprieksejie_soli = 0
    for n in (100, 1000, 10_000):
        dati = list(range(n))
        _, soli = binary_search(dati, n - 1)
        print(f"{n:5} elementi — {soli} soļi.")
        if ieprieksejie_soli:
            print(f"Datu apjoms pieauga 10 reizes, soļu skaits par "
                  f"{soli - ieprieksejie_soli}.")
        ieprieksejie_soli = soli


if __name__ == "__main__":
    main()
