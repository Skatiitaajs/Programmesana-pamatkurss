"""7.5. Iebūvēto funkciju efektivitāte."""

import time


# Burbuļkārtošanas funkcija no 72.py.
def bubble_sort(rezultati, apturet_agrak=False, radit_gajienus=False):
    """Sakārto sarakstu un atgriež to, salīdzinājumu skaitu un gājienu skaitu."""
    salidzinajumi = 0
    gajieni = 0

    for j in range(len(rezultati)):
        mainits = False
        gajieni += 1
        # Katrs gājiens noliek lielāko no atlikušajiem skaitļiem savā vietā.
        for i in range(len(rezultati) - 1 - j):
            salidzinajumi += 1
            if rezultati[i] > rezultati[i + 1]:
                rezultati[i], rezultati[i + 1] = rezultati[i + 1], rezultati[i]
                mainits = True

        if radit_gajienus:
            print(f"{gajieni}. gājiens — {rezultati}")
        if apturet_agrak and not mainits:
            break

    return rezultati, salidzinajumi, gajieni


def merit_meklesanu(dati, mekletais, atkartojumi):
    """Atgriež meklēšanas rezultātu un visu atkārtojumu kopējo laiku."""
    sakums = time.time()
    for _ in range(atkartojumi):
        atrasts = mekletais in dati
    return atrasts, time.time() - sakums


def main():
    print("1. Burbuļkārtošana un sorted()")
    dati = list(range(3000, 0, -1))
    dati_burbuliem = dati.copy()

    sakums = time.time()
    ar_burbuliem, _, _ = bubble_sort(dati_burbuliem)
    laiks_burbuliem = time.time() - sakums

    sakums = time.time()
    ar_sorted = sorted(dati)
    laiks_sorted = time.time() - sakums

    print(f"bubble_sort() — {laiks_burbuliem:.4f} s.")
    print(f"sorted() — {laiks_sorted:.4f} s ({laiks_sorted * 1000000:.1f} µs).")
    print(f"Sakārtotie saraksti sakrīt — {ar_burbuliem == ar_sorted}.")
    print(f"sorted() bija {laiks_burbuliem / laiks_sorted:.1f} reizes ātrāka.")

    print("\n2. Meklēšana ar in sarakstā un kopā")
    dati_saraksts = list(range(200000))
    dati_kopa = set(dati_saraksts)
    mekletais = 199999
    # Vienāds atkārtojumu skaits ļauj izmērīt arī īso pārbaudi kopā.
    atkartojumi = 1000
    atrasts_saraksta, laiks_saraksta = merit_meklesanu(
        dati_saraksts, mekletais, atkartojumi
    )
    atrasts_kopa, laiks_kopa = merit_meklesanu(dati_kopa, mekletais, atkartojumi)
    print(f"Saraksts — {atrasts_saraksta}, {laiks_saraksta:.6f} s "
          f"par {atkartojumi} pārbaudēm.")
    print(f"Kopa — {atrasts_kopa}, {laiks_kopa:.6f} s "
          f"par {atkartojumi} pārbaudēm.")
    print(f"Kopa bija {laiks_saraksta / laiks_kopa:.0f} reizes ātrāka.")
    print("Saraksts pārbauda elementus pēc kārtas, tāpēc sliktākajā gadījumā "
          "meklēšana ir O(n). Kopa izmanto jaucējvērtību un vidēji meklē O(1) laikā.")

    print("\n3. Datu struktūras izvēle")
    top5 = [980, 940, 940, 870, 820]
    pievienosanas_seciba = ["Zane", "Anna", "Marta"]
    speletaju_vardi = set()
    for vards in pievienosanas_seciba:
        speletaju_vardi.add(vards)
    speletaju_vardi.add("Anna")
    profils = {"vārds": "Anna", "punkti": 940, "līmenis": 7}

    print(f"TOP 5 — saraksts {top5}, jo jāsaglabā vietu secība un vienādi punkti.")
    print(f"Vārdu pārbaude — kopa {speletaju_vardi}, jo tā ļauj ātri pārbaudīt vārdu.")
    print(f"Spēlētāja profils — vārdnīca {profils}, jo katram laukam ir atslēga.")
    kopas_seciba = list(speletaju_vardi)
    print(f"Vārdu pirmās pievienošanas secība — {pievienosanas_seciba}.")
    print(f"Kopas iterācijas secība — {kopas_seciba}.")
    print(f"Šoreiz secības sakrīt — {kopas_seciba == pievienosanas_seciba}.")
    print(f"Vārds Anna pievienots divreiz, kopā palika {len(speletaju_vardi)} vārdi.")
    print("Kopa negarantē pievienošanas secību un glabā katru vērtību vienreiz, "
          "tāpēc ar to pazustu gan TOP 5 secība, gan atkārtots rezultāts.")

    print("\nPapilduzdevums ar vārdnīcu")
    vardnica = {i: i for i in range(200000)}
    atrasts_vardnica, laiks_vardnica = merit_meklesanu(
        vardnica, mekletais, atkartojumi
    )
    print(f"Vārdnīcā atslēga {mekletais} atrasta — {atrasts_vardnica}.")
    laiki = {"saraksts": laiks_saraksta, "kopa": laiks_kopa, "vārdnīca": laiks_vardnica}
    for struktura, laiks in laiki.items():
        print(f"{struktura} — {laiks:.6f} s par {atkartojumi} pārbaudēm.")
    lenaka = max(laiki, key=laiki.get)
    print(f"Visilgāk meklēja {lenaka}.")
    print("Kopa glabā vērtības, savukārt vārdnīca katrai atslēgai glabā arī "
          "tai piesaistītu vērtību. Atslēgas pārbaude vārdnīcā vidēji ir O(1).")


if __name__ == "__main__":
    main()
