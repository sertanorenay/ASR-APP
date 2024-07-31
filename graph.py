import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Örnek veriler oluştur
start_date = datetime(2023, 7, 1)
days = 10

dates = [start_date + timedelta(days=i) for i in range(days)]
correct_words = [75, 81, 71, 86, 90, 93, 90, 95, 96, 96]
total_words = 100
accuracy = [correct / total_words * 100 for correct in correct_words]

# Çizim oluştur
plt.figure(figsize=(12, 6))
plt.plot(dates, accuracy, marker='o', linestyle='-', color='#670F85', label='Doğruluk Yüzdesi')
plt.fill_between(dates, accuracy, color='#670F85', alpha=0.1)

# Çizim detayları
plt.title('Okuma Doğrulukları ve Gün Gün Gelişimi')
plt.xlabel('Tarih')
plt.ylabel('Doğruluk Yüzdesi (%)')
plt.ylim(0, 110)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Çizimi göster
plt.show()
