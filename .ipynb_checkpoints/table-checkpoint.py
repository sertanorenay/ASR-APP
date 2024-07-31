import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

# Veriler
start_date = datetime(2023, 7, 1)
days = 10
dates = [start_date + timedelta(days=i) for i in range(days)]
correct_words = [75, 81, 71, 86, 90, 93, 90, 95, 96, 96]
total_words = 100
accuracy = [correct / total_words * 100 for correct in correct_words]

# Tablo verileri
columns = ['Tarih', 'Doğru Okunan Kelimeler', 'Toplam Kelime Sayısı', 'Doğruluk Yüzdesi']
table_data = []
for date, correct, acc in zip(dates, correct_words, accuracy):
    table_data.append([date.strftime('%Y-%m-%d'), correct, total_words, f'{acc:.2f}%'])

# Çizim oluştur
fig, ax = plt.subplots(figsize=(12, 6))

# Çizim ve alan doldurma
ax.plot(dates, accuracy, marker='o', linestyle='-', color='#670F85', label='Doğruluk Yüzdesi')
ax.fill_between(dates, accuracy, color='#670F85', alpha=0.1)

# Çizim detayları
ax.set_title('Okuma Doğrulukları ve Gün Gün Gelişimi')
ax.set_xlabel('Tarih')
ax.set_ylabel('Doğruluk Yüzdesi (%)')
ax.set_ylim(0, 110)
ax.set_xticks(dates)
ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in dates], rotation=45)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Tabloyu ekle
table = plt.table(cellText=table_data, colLabels=columns, cellLoc='center', loc='bottom', bbox=[0, -0.5, 1, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Düzenle ve göster
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.show()
