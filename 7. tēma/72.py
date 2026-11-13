"""7.2. Kārtošanas loģika."""


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


def main():
    print("1. Divu vērtību apmaiņa")
    rezultati = [90, 45]
    print("Pirms maiņas", rezultati)
    rezultati[0], rezultati[1] = rezultati[1], rezultati[0]
    print("Pēc maiņas", rezultati)

    a, b = 90, 45
    print(f"Pirms maiņas a = {a}, b = {b}.")
    a, b = b, a
    print(f"Pēc maiņas a = {a}, b = {b}.")
    print("Python vispirms nolasa abas vērtības un tikai tad tās piešķir "
          "pretējā secībā, tāpēc pietiek ar diviem mainīgajiem.")

    print("\n2. Pirmais burbuļkārtošanas gājiens")
    dati = [42, 15, 8, 99, 23, 4]
    rezultati = dati.copy()
    print("Sākuma saraksts", rezultati)
    for i in range(len(rezultati) - 1):
        if rezultati[i] > rezultati[i + 1]:
            rezultati[i], rezultati[i + 1] = rezultati[i + 1], rezultati[i]
    print("Pēc pirmā gājiena", rezultati)
    print(f"Pēdējā vietā nonāca lielākais skaitlis {rezultati[-1]}.")

    print("\n3. Pilna burbuļkārtošana")
    sakartoti_6, salidzinajumi_6, _ = bubble_sort(dati.copy(), radit_gajienus=True)
    print(f"6 elementi — {salidzinajumi_6} salīdzinājumi.")
    print("Sakārtots pareizi", sakartoti_6 == sorted(dati))

    dati_10 = dati + [17, 50, 2, 30]
    sakartoti_10, salidzinajumi_10, _ = bubble_sort(
        dati_10.copy(), radit_gajienus=True
    )
    print(f"10 elementi — {salidzinajumi_10} salīdzinājumi.")
    print("Sakārtots pareizi", sakartoti_10 == sorted(dati_10))
    print(f"Elementu skaits pieauga no 6 līdz 10, bet salīdzinājumu skaits "
          f"pieauga {salidzinajumi_10 / salidzinajumi_6:g} reizes.")
    print("Bez agrās apstāšanās salīdzinājumu skaits ir n(n - 1) / 2 "
          "un aug kvadrātiski (O(n²)).")

    print("\nPapilduzdevums — agrā apstāšanās")
    _, pilnie_salidzinajumi, pilnie_gajieni = bubble_sort(sakartoti_10.copy())
    _, atrie_salidzinajumi, atrie_gajieni = bubble_sort(
        sakartoti_10.copy(), apturet_agrak=True
    )
    print(f"Parastais variants — {pilnie_gajieni} gājieni un "
          f"{pilnie_salidzinajumi} salīdzinājumi.")
    print(f"Ar agro apstāšanos — {atrie_gajieni} gājiens un "
          f"{atrie_salidzinajumi} salīdzinājumi.")


if __name__ == "__main__":
    main()
