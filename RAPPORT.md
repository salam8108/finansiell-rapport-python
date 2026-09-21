# Examinerande uppgift 2 – Finansiell rapport

## 1. Inledning

Syftet med projektet är att skapa en automatiserad finansiell rapport med hjälp av Python. Rapporten ska göra det enkelt att jämföra företagets utfall med budget och prognos för olika affärsenheter.

Projektet använder ekonomiska data för fyra affärsenheter: Nord, Syd, Ost och Vast. Datamaterialet omfattar perioden januari–juni 2026.

Resultatet sparas som en formaterad Excelrapport som innehåller både en sammanfattning och detaljerad information.

## 2. Datakälla

Datamaterialet kommer från CSV-filen `financial_data.csv`, som tillhandahölls för den examinerande uppgiften.

Filen innehåller följande kolumner:

* `Datum` – rapporteringsdatum.
* `Affarsenhet` – företagets affärsenhet.
* `Utfall` – det faktiska ekonomiska resultatet.
* `Budget` – det budgeterade beloppet.
* `Prognos` – det prognostiserade beloppet.

Programmet läser filen från mappen `data` med hjälp av funktionen `pandas.read_csv()`.

## 3. Verktyg och bibliotek

Projektet utvecklades i Visual Studio Code och använder Python 3.

Följande Pythonbibliotek används:

* **pandas** för att läsa, bearbeta, gruppera och summera data.
* **XlsxWriter** för att skapa och formatera Excelrapporten.

Projektet använder inga externa tjänster och kräver ingen särskild konfiguration.

## 4. Genomförande

Arbetet genomfördes i flera steg.

### 4.1 Inläsning av data

CSV-filen läses in i en pandas DataFrame. En DataFrame gör det möjligt att bearbeta tabellbaserad information i Python.

### 4.2 Beräkning av avvikelser

Programmet skapar fyra nya kolumner.

Avvikelsen mot budget beräknas enligt:

```text
Avvikelse_budget = Utfall − Budget
```

Avvikelsen mot prognos beräknas enligt:

```text
Avvikelse_prognos = Utfall − Prognos
```

Avvikelserna beräknas också i procent:

```text
Avvikelse_budget_procent = Avvikelse_budget / Budget × 100
```

```text
Avvikelse_prognos_procent = Avvikelse_prognos / Prognos × 100
```

Resultaten avrundas till två decimaler.

### 4.3 Sammanfattning

Informationen grupperas efter affärsenhet. Utfall, budget och prognos summeras för varje affärsenhet.

Därefter beräknas de sammanlagda avvikelserna i belopp och procent. Sammanfattningen gör det möjligt att snabbt jämföra resultatet mellan företagets olika delar.

### 4.4 Export till Excel

Rapporten exporteras till filen `finansiell_rapport.xlsx`.

Excelrapporten innehåller två blad:

* **Sammanfattning** – summerade resultat per affärsenhet.
* **Detaljer** – samtliga ursprungliga rader och de beräknade avvikelserna.

Rapporten innehåller formaterade rubriker, tabeller, anpassade kolumnbredder och låsta rubrikrader.

Positiva avvikelser markeras med grönt och negativa avvikelser med rött. Detta gör rapporten lättare att läsa och hjälper användaren att snabbt upptäcka positiva och negativa resultat.

På sammanfattningsbladet finns även ett diagram som jämför utfall, budget och prognos för varje affärsenhet.

## 5. Resultat och analys

Resultatet visar att **Nord** har det högsta totala utfallet under perioden. Nord har ett utfall på 6 745 000 kronor, vilket är 145 000 kronor över budget och 70 000 kronor över prognos.

**Ost** ligger 20 000 kronor över budget och har ett utfall som motsvarar prognosen.

**Syd** ligger 10 000 kronor under både budget och prognos. Det motsvarar en negativ avvikelse på cirka 0,17 procent.

**Vast** ligger 5 000 kronor över både budget och prognos.

Diagrammet visar att skillnaderna mellan utfall, budget och prognos är relativt små. Nord visar den tydligaste positiva avvikelsen, medan Syd visar en mindre negativ avvikelse.

## 6. Felhantering och möjliga förbättringar

Den nuvarande lösningen fungerar med den angivna CSV-filen. Programmet förutsätter att filen finns i rätt mapp och att kolumnnamnen är korrekta.

Projektet kan i framtiden förbättras genom att:

* kontrollera om CSV-filen finns innan den läses,
* kontrollera om några värden saknas,
* hantera felaktiga kolumnnamn,
* undvika division med noll,
* låta användaren välja indatafil,
* skapa fler diagram och nyckeltal,
* lägga till jämförelser mellan olika månader,
* automatiskt skapa rapporter för nya perioder.

## 7. Självreflektion

Genom projektet har jag fått en bättre förståelse för hur Python kan användas för att automatisera finansiell rapportering. Jag har lärt mig att läsa data från en CSV-fil, skapa nya beräknade kolumner och gruppera information med pandas.

En utmaning var att förstå hur indrag fungerar i Python, särskilt när kod ska placeras inuti en `with`-sats. Jag fick även arbeta med filsökvägar och kontrollera att CSV-filen fanns i rätt mapp.

En annan utmaning var formateringen av Excelrapporten. Jag lärde mig hur XlsxWriter kan användas för att skapa tabeller, formatera tal och procent, ändra kolumnbredder, frysa rubrikrader och använda villkorsstyrd formatering.

Jag tycker att slutresultatet blev tydligt och användbart. Rapporten visar både detaljer och en sammanfattning, vilket gör det möjligt att snabbt identifiera ekonomiska avvikelser. Om jag fortsätter utveckla projektet vill jag lägga till mer felhantering och fler analyser över tid.

## 8. Slutsats

Projektet visar hur Python kan användas för att omvandla finansiella data från en CSV-fil till en tydlig och professionell Excelrapport.

Genom automatiserade beräkningar minskar behovet av manuellt arbete. Lösningen kan återanvändas när nya data läggs till, vilket gör rapporteringen snabbare och minskar risken för manuella beräkningsfel.

## 9. Källor

* Kursmaterial och datamaterial för Examinerande uppgift 2.
* pandas documentation – `read_csv`:
  https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
* pandas documentation – `DataFrame.to_excel`:
  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
* XlsxWriter documentation – Working with pandas:
  https://xlsxwriter.readthedocs.io/working_with_pandas.html
