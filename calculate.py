from docx import Document
import pandas as pd

# Verileri oku
df = pd.read_csv("algerian-bejaia.csv")

# İlk 3 sütunu hariç tut
numeric_cols = df.iloc[:, 3:]

# Sadece sayısal veri içeren sütunları seç
numeric_cols = numeric_cols.select_dtypes(include=['float64', 'int64'])

# İstatistiksel hesaplamaları yap
statistics = {
    "Ortalama": numeric_cols.mean(),
    "Standart Sapma": numeric_cols.std(),
    "Minimum Değer": numeric_cols.min(),
    "Maksimum Değer": numeric_cols.max()
}

# Verileri formatla ve virgülden sonra birden fazla sıfır olmasın
formatted_statistics = {}
for key, value in statistics.items():
    formatted_statistics[key] = value.apply(lambda x: f"{x:.6g}")

# Verileri DataFrame'den Word tablosuna dönüştür
def df_to_table(document, df):
    # Tablo oluştur
    table = document.add_table(rows=1, cols=len(df.columns))
    table.style = 'Table Grid'

    # Başlık satırını ekle
    hdr_cells = table.rows[0].cells
    for i, col in enumerate(df.columns):
        hdr_cells[i].text = col

    # Veri satırlarını ekle
    for _, row in df.iterrows():
        row_cells = table.add_row().cells
        for i, val in enumerate(row):
            row_cells[i].text = str(val)

# Word belgesi oluştur
document = Document()

# Verileri Word tablosuna ekle
df_to_table(document, pd.DataFrame(formatted_statistics))

# Word dosyasını kaydet
document.save('formatted_statistics_table.docx')

print("Word dosyası oluşturuldu: formatted_statistics_table.docx")
