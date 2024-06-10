import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Veri dosyasını oku
df = pd.read_csv('algerian-bejaia.csv')

# Bağımsız değişkenler (X) ve bağımlı değişken (y) olarak ayır
X = df.iloc[:, 3:13]  # Sıcaklık, Nem, Rüzgar Hızı, Yağış, vb. özellikler
y = df['Fire Classes']  # Hedef değişken: Yangın Sınıfları

# Eğitim ve test veri setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Naive Bayes modelini eğit
model = GaussianNB()
model.fit(X_train, y_train)

# Test verileri ile tahmin yap
y_pred = model.predict(X_test)

# Doğruluk oranını hesapla
accuracy = accuracy_score(y_test, y_pred)
print("Doğruluk Oranı:", accuracy)
