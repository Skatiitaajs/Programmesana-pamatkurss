# 7.6. Koda lauzējs

Dators min spēlētāja iedomātu veselu skaitli. Atbildi ar `lielaks`, ja tavs
skaitlis ir lielāks par datora minējumu, ar `mazaks`, ja tas ir mazāks, vai ar
`pareizi`, ja dators ir uzminējis.

## Palaišana

Terminālī atver mapi `7. tēma` un izvēlies diapazonu.

```sh
python 76.py       # no 1 līdz 100
python 76.py 1000  # no 1 līdz 1000
```

Ja datorā Python 3 palaišanai izmanto `python3`, komandās aizstāj `python` ar
`python3`.

## Algoritma efektivitāte

Dators min diapazona vidējo skaitli. Ja minējums ir par mazu, jaunā apakšējā
robeža ir minējums plus viens. Ja minējums ir par lielu, jaunā augšējā robeža ir
minējums mīnus viens. Pēc katra nepareiza minējuma paliek ne vairāk kā puse no
iepriekšējām iespējām. Ja apakšējā robeža pārsniedz augšējo, atbildes ir
pretrunīgas un spēle beidzas.

Ar `n` iespējamiem skaitļiem sliktākajā gadījumā binārajai meklēšanai vajag
`⌊log₂(n)⌋ + 1` minējumus. Pēc `⌊log₂(n)⌋` dalīšanas soļiem paliek ne vairāk kā
viens skaitlis, kuru pārbauda ar pēdējo minējumu. Tāpēc sarežģītība ir
`O(log n)`. Lineārā meklēšana pārbauda skaitļus pēc kārtas, tāpēc sliktākajā
gadījumā tai vajag `n` minējumus jeb `O(n)`.

| Diapazons | Pirmais minējums | Binārās meklēšanas maksimums | Lineārās meklēšanas maksimums |
| --- | ---: | ---: | ---: |
| 1–100 | 50 | 7 | 100 |
| 1–1000 | 500 | 10 | 1000 |

## Testu pieraksts

| Diapazons | Iedomātais skaitlis vai atbildes | Datora minējumi | Rezultāts |
| --- | --- | --- | --- |
| 1–100 | 73 | 50, 75, 62, 68, 71, 73 | Uzminēja 6 minējumos. |
| 1–100 | 1 | 50, 25, 12, 6, 3, 1 | Uzminēja 6 minējumos. |
| 1–100 | 100 | 50, 75, 88, 94, 97, 99, 100 | Uzminēja 7 minējumos. |
| 1–1000 | 1000 | 500, 750, 875, 938, 969, 985, 993, 997, 999, 1000 | Uzminēja 10 minējumos. |
| 1–100 | `mazaks` pēc katra minējuma | 50, 25, 12, 6, 3, 1 | Pēc atbildes, ka skaitlis ir mazāks par 1, pamanīja pretrunu un beidza spēli. |

Trijās spēlēs ar diapazonu 1–100 lielākais minējumu skaits bija **7**.
Pārbaudīju arī nederīgu ievadi. Pēc atbildes `nezināms` programma vēlreiz
prasa atbildi uz to pašu minējumu un minējumu skaits nepieaug.

[eBskola 7.6. uzdevums](https://ebskola.lv/programmesana1/prog1_7/prog1_76)
