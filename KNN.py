import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from docx import Document
from docx.shared import Inches

# Veri setini yükle
df = pd.read_csv('algerian-bejaia.csv')

# Bağımsız değişkenler (X) ve hedef değişken (y) olarak ayır
X = df.iloc[:, 3:-1]  # İlk üç sütun hariç tüm özellikler
y = df['Fire Classes']  # Hedef değişken

# Eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN modelini oluştur ve eğit
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Test seti üzerinde tahmin yap
y_pred = knn.predict(X_test)

# Sınıflandırma raporunu al
report = classification_report(y_test, y_pred, output_dict=True)

# Doğruluk oranını hesapla
accuracy = accuracy_score(y_test, y_pred)

print(f"Doğruluk Oranı: {accuracy:.2f}")
