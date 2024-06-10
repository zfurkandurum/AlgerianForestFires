import matplotlib.pyplot as plt

# Veriler ve başlıklar
basliklar = ['[1]', '[3]', ' ']
degerler = [0.72, 0.94, 0.92]

# Sütun grafiği oluşturma
plt.bar(basliklar, degerler, color=['blue', 'green', 'red', 'purple'])
plt.ylabel('Değerler')
plt.title('Karar Ağacı Karşılaştırması')
plt.ylim(0, 1)  # Değer aralığını isteğe göre ayarlayabiliriz
plt.show()
