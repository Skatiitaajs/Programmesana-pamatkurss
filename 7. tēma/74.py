"""7.4. Iebūvēto funkciju ātrums."""

import time


def minimums_cikla(dati):
    mazakais = dati[0]
    for skaitlis in dati:
        if skaitlis < mazakais:
            mazakais = skaitlis
    return mazakais


def summa_cikla(dati):
    summa = 0
    for skaitlis in dati:
        summa += skaitlis
    return summa


def summa_iebuveta(dati):
    return sum(dati)


def skaits_cikla(dati):
    skaits = 0
    for _ in dati:
        skaits += 1
    return skaits


def main():
    print("1. Mazākā un lielākā vērtība")
    ienaidnieku_hp = [85, 120, 40, 64, 95, 135, 52, 76, 108, 30]
    vajakais = min(ienaidnieku_hp)
    stiprakais = max(ienaidnieku_hp)
    print(f"Vājākajam ir {vajakais} HP, stiprākajam ir {stiprakais} HP.")
    savs_minimums = minimums_cikla(ienaidnieku_hp)
    print(f"Ciklā iegūtais minimums ir {savs_minimums} HP.")
    print(f"Abu metožu minimums sakrīt — {savs_minimums == vajakais}.")

    print("\n2. Miljona skaitļu summa")
    dati = list(range(1000000))
    summa_sava = summa_cikla(dati)
    summa_no_sum = summa_iebuveta(dati)
    print(f"Cikla summa ir {summa_sava}, sum() summa ir {summa_no_sum}.")
    print(f"Abas summas sakrīt — {summa_sava == summa_no_sum}.")
    print("Ieskaitot def rindu, cikla funkcijai ir 5 rindas, sum() funkcijai ir 2.")
    print("sum() ir vieglāk lasāma, jo funkcijas nosaukums pasaka, ko tā dara.")

    print("\n3. Summēšanas laika salīdzinājums")
    attiecibas = []
    for merijums in range(1, 3):
        sakums = time.time()
        summa_cikla(dati)
        laiks_cikla = time.time() - sakums

        sakums = time.time()
        summa_iebuveta(dati)
        laiks_iebuvetais = time.time() - sakums

        attieciba = laiks_cikla / laiks_iebuvetais
        attiecibas.append(attieciba)
        print(f"{merijums}. mērījums — cikls {laiks_cikla:.4f} s, "
              f"sum() {laiks_iebuvetais:.4f} s, attiecība {attieciba:.2f}×.")

    atskiriba = abs(attiecibas[1] - attiecibas[0]) / attiecibas[0] * 100
    print(f"Otrā mērījuma attiecība atšķiras no pirmās par {atskiriba:.1f}%.")
    print("Abas metodes ir O(n), jo apskata visus skaitļus. CPython sum() "
          "saskaita veselus skaitļus optimizētā C kodā, tāpēc katrs solis ir ātrāks.")

    print("\nPapilduzdevums ar len() un sorted()")
    # Viena len() izsaukuma laiks ir pārāk īss, tāpēc mērām vairākus kopā.
    atkartojumi = 100000
    sakums = time.time()
    for _ in range(atkartojumi):
        skaits_ar_len = len(dati)
    laiks_len = (time.time() - sakums) / atkartojumi

    sakums = time.time()
    savs_skaits = skaits_cikla(dati)
    laiks_savam_skaitam = time.time() - sakums

    kartosanas_dati = dati[:10000][::-1]
    sakums = time.time()
    sakartoti = sorted(kartosanas_dati)
    laiks_sorted = time.time() - sakums

    print(f"len() uz 1 000 000 elementiem — {skaits_ar_len}, "
          f"vidēji {laiks_len:.9f} s izsaukumā.")
    print(f"Skaitīšanas cikls uz 1 000 000 elementiem — {savs_skaits}, "
          f"{laiks_savam_skaitam:.9f} s.")
    print(f"sorted() uz 10 000 elementiem — {laiks_sorted:.9f} s, "
          f"pirmais elements {sakartoti[0]}, pēdējais {sakartoti[-1]}.")
    print("len() ir O(1), jo saraksts glabā savu garumu. "
          "Skaitīšanas cikls ir O(n), jo apmeklē katru elementu.")


if __name__ == "__main__":
    main()
