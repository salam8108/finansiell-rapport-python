import pandas as pd

# Läs in data
df = pd.read_csv("data/financial_data.csv")
df["Datum"] = pd.to_datetime(df["Datum"])

# Beräkna avvikelser
df["Avvikelse_budget"] = df["Utfall"] - df["Budget"]
df["Avvikelse_prognos"] = df["Utfall"] - df["Prognos"]

df["Avvikelse_budget_procent"] = (
    df["Avvikelse_budget"] / df["Budget"] * 100
).round(2)

df["Avvikelse_prognos_procent"] = (
    df["Avvikelse_prognos"] / df["Prognos"] * 100
).round(2)

# Skapa sammanfattning per affärsenhet
summary = df.groupby("Affarsenhet", as_index=False)[
    ["Utfall", "Budget", "Prognos"]
].sum()

summary["Avvikelse_budget"] = summary["Utfall"] - summary["Budget"]
summary["Avvikelse_prognos"] = summary["Utfall"] - summary["Prognos"]

summary["Avvikelse_budget_procent"] = (
    summary["Avvikelse_budget"] / summary["Budget"] * 100
).round(2)

summary["Avvikelse_prognos_procent"] = (
    summary["Avvikelse_prognos"] / summary["Prognos"] * 100
).round(2)

output_file = "finansiell_rapport.xlsx"

with pd.ExcelWriter(
    output_file,
    engine="xlsxwriter",
    datetime_format="yyyy-mm-dd"
) as writer:

    # Exportera data till Excel
    summary.to_excel(
        writer,
        sheet_name="Sammanfattning",
        startrow=3,
        index=False
    )

    df.to_excel(
        writer,
        sheet_name="Detaljer",
        index=False
    )

    workbook = writer.book
    summary_sheet = writer.sheets["Sammanfattning"]
    detail_sheet = writer.sheets["Detaljer"]

    # Skapa format
    title_format = workbook.add_format({
        "bold": True,
        "font_size": 18,
        "font_color": "white",
        "bg_color": "#1F4E78",
        "align": "center"
    })

    positive_format = workbook.add_format({
        "font_color": "#006100",
        "bg_color": "#C6EFCE"
    })

    negative_format = workbook.add_format({
        "font_color": "#9C0006",
        "bg_color": "#FFC7CE"
    })

    money_format = workbook.add_format({
        "num_format": "#,##0"
    })

    percent_format = workbook.add_format({
        "num_format": '0.00"%"'
    })

    date_format = workbook.add_format({
        "num_format": "yyyy-mm-dd"
    })

    # Formatera sammanfattningen
    summary_sheet.merge_range(
        "A1:H1",
        "Finansiell rapport – Sammanfattning",
        title_format
    )

    summary_sheet.write(
        "A2",
        "Jämförelse mellan utfall, budget och prognos per affärsenhet"
    )

    summary_sheet.add_table(
        3,
        0,
        3 + len(summary),
        len(summary.columns) - 1,
        {
            "columns": [{"header": column} for column in summary.columns],
            "style": "Table Style Medium 2"
        }
    )

    summary_sheet.set_column("A:A", 18)
    summary_sheet.set_column("B:F", 16, money_format)
    summary_sheet.set_column("G:H", 25, percent_format)
    summary_sheet.freeze_panes(4, 0)

    # Färglägg positiva och negativa värden
    summary_sheet.conditional_format(
        4, 4, 3 + len(summary), 7,
        {
            "type": "cell",
            "criteria": ">",
            "value": 0,
            "format": positive_format
        }
    )

    summary_sheet.conditional_format(
        4, 4, 3 + len(summary), 7,
        {
            "type": "cell",
            "criteria": "<",
            "value": 0,
            "format": negative_format
        }
    )

    # Skapa diagram
    chart = workbook.add_chart({"type": "column"})

    chart.add_series({
        "name": "Utfall",
        "categories": ["Sammanfattning", 4, 0, 3 + len(summary), 0],
        "values": ["Sammanfattning", 4, 1, 3 + len(summary), 1],
        "fill": {"color": "#4472C4"}
    })

    chart.add_series({
        "name": "Budget",
        "categories": ["Sammanfattning", 4, 0, 3 + len(summary), 0],
        "values": ["Sammanfattning", 4, 2, 3 + len(summary), 2],
        "fill": {"color": "#A5A5A5"}
    })

    chart.add_series({
        "name": "Prognos",
        "categories": ["Sammanfattning", 4, 0, 3 + len(summary), 0],
        "values": ["Sammanfattning", 4, 3, 3 + len(summary), 3],
        "fill": {"color": "#ED7D31"}
    })

    chart.set_title({
        "name": "Utfall jämfört med budget och prognos"
    })

    chart.set_y_axis({
        "name": "Belopp",
        "num_format": "#,##0"
    })

    chart.set_legend({"position": "bottom"})
    chart.set_style(10)

    summary_sheet.insert_chart(
        "K4",
        chart,
        {
            "x_scale": 1.4,
            "y_scale": 1.3
        }
    )

    # Formatera detaljsidan
    detail_sheet.add_table(
        0,
        0,
        len(df),
        len(df.columns) - 1,
        {
            "columns": [{"header": column} for column in df.columns],
            "style": "Table Style Medium 2"
        }
    )

    detail_sheet.set_column("A:A", 13, date_format)
    detail_sheet.set_column("B:B", 16)
    detail_sheet.set_column("C:G", 18, money_format)
    detail_sheet.set_column("H:I", 27, percent_format)
    detail_sheet.freeze_panes(1, 0)

    detail_sheet.conditional_format(
        1, 5, len(df), 8,
        {
            "type": "cell",
            "criteria": ">",
            "value": 0,
            "format": positive_format
        }
    )

    detail_sheet.conditional_format(
        1, 5, len(df), 8,
        {
            "type": "cell",
            "criteria": "<",
            "value": 0,
            "format": negative_format
        }
    )

print(f"Excelrapport skapad: {output_file}")