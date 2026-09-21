# Finansiell rapport med Python

## Beskrivning

Projektet läser finansiella data från en CSV-fil och skapar automatiskt en formaterad Excelrapport. Rapporten jämför utfall med budget och prognos för olika affärsenheter.

## Funktioner

Programmet:

* läser data från `data/financial_data.csv`,
* beräknar avvikelse mellan utfall och budget,
* beräknar avvikelse mellan utfall och prognos,
* beräknar avvikelser i procent,
* skapar ett sammanfattningsblad,
* skapar ett detaljblad,
* använder färgmarkering för positiva och negativa avvikelser,
* skapar ett diagram som jämför utfall, budget och prognos.

## Projektstruktur

```text
projektmapp/
│
├── data/
│   └── financial_data.csv
├── main.py
├── README.md
└── finansiell_rapport.xlsx
```

## Förberedelser

Python 3 behöver vara installerat på datorn.

Installera nödvändiga bibliotek genom att köra:

```bash
python -m pip install pandas XlsxWriter
```

## Körning

1. Kontrollera att filen `financial_data.csv` finns i mappen `data`.
2. Öppna terminalen i projektmappen.
3. Kör programmet:

```bash
python main.py
```

När programmet är klart skapas filen:

```text
finansiell_rapport.xlsx
```

## Resultat

Excelrapporten innehåller två blad:

* **Sammanfattning** – summerade värden per affärsenhet och ett diagram.
* **Detaljer** – samtliga rader från datamaterialet med beräknade avvikelser.

Positiva avvikelser markeras med grönt och negativa avvikelser med rött.

## Beroenden

Projektet använder:

* Python 3
* pandas
* XlsxWriter

## Data

Datamaterialet kommer från filen `financial_data.csv`, som tillhandahölls för den examinerande uppgiften. Projektet använder inga externa tjänster och kräver ingen ytterligare konfiguration.
