import numpy as np
from matplotlib import pyplot as plt

# Toplam kişi sayısı
n = 106

# Ortalama ve standart sapma
mean = 28
std_dev = 15

# Normal dağılım oluştur
np.random.seed(0)
scores = np.random.normal(mean, std_dev, n)

# 0 alan kişi sayısını 3 olarak ayarlayalım
zero_count = np.sum(scores < 0)
if zero_count < 3:
    additional_zeros = 3 - zero_count
    scores[scores < 0] = np.random.choice(scores[scores > 0], zero_count)
    zero_indices = np.random.choice(np.where(scores > 0)[0], additional_zeros, replace=False)
    scores[zero_indices] = 0

# 70'in üzerinde olan kişi sayısını 5'e ayarlayalım
above_70_count = np.sum(scores > 70)
if above_70_count < 5:
    additional_above_70 = 5 - above_70_count
    below_70_indices = np.where(scores <= 70)[0]
    chosen_indices = np.random.choice(below_70_indices, additional_above_70, replace=False)
    scores[chosen_indices] = 70 + np.random.rand(additional_above_70)

# Puanları küçükten büyüğe sıralayalım
sorted_scores = np.sort(scores)

# Harf notları aralıklarını belirleyelim
def get_grade_boundaries(sorted_scores):
    n = len(sorted_scores)
    boundaries = {
        "AA": sorted_scores[int(0.90 * n)],
        "BA": sorted_scores[int(0.80 * n)],
        "BB": sorted_scores[int(0.70 * n)],
        "CB": sorted_scores[int(0.60 * n)],
        "CC": sorted_scores[int(0.50 * n)],
        "DC": sorted_scores[int(0.40 * n)],
        "DD": sorted_scores[int(0.30 * n)],
        "FF": sorted_scores[int(0.0 * n)]
    }
    return boundaries

grade_boundaries = get_grade_boundaries(sorted_scores)

print("Harf Notları Aralıkları:")
for grade, boundary in grade_boundaries.items():
    print(f"{grade}: {boundary:.2f} ve üstü")

# Histogram oluştur
plt.hist(scores, bins=20, edgecolor='black')
plt.title('Sınav Puan Dağılımı ve Harf Notları')
plt.xlabel('Puan')
plt.ylabel('Frekans')
plt.grid(True)

# Harf notları sınırlarını çiz
for grade, boundary in grade_boundaries.items():
    plt.axvline(x=boundary, color='red', linestyle='--')
    plt.text(boundary, max(plt.ylim())*0.9, f'{grade}', rotation=90, verticalalignment='center')

plt.show()

# Dağılım istatistikleri
print(f"Ortalama: {np.mean(scores):.2f}")
print(f"Standart Sapma: {np.std(scores):.2f}")
print(f"Minimum Puan: {np.min(scores):.2f}")
print(f"Maksimum Puan: {np.max(scores):.2f}")
print(f"70'in Üzerinde Olan Kişi Sayısı: {np.sum(scores > 70)}")
print(f"0 Alan Kişi Sayısı: {np.sum(scores == 0)}")
