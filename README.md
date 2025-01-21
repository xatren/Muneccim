# Veri Analizi ve Ajan Tabanlı Mimari Projesi

Bu proje, veri analizi ve makine öğrenmesi işlemlerini ajan tabanlı bir mimari kullanarak gerçekleştiren bir sistemdir. Proje, veri toplama, işleme ve sonuçların görselleştirilmesi gibi temel işlevleri modüler bir yapıda sunar.

## Özellikler

- Veri toplama ve ön işleme
- PCA (Principal Component Analysis) ile boyut indirgeme
- K-Means kümeleme analizi
- Ajan tabanlı modüler mimari
- Otomatik raporlama ve görselleştirme
- JSON tabanlı ajan iletişimi

## Kurulum

### 1. Projeyi Klonlama

```bash
# Projeyi klonlayın
git clone https://github.com/xatren/Muneccim.git
# Proje dizinine gidin
cd Muneccim
```

### 2. Sanal Ortam Oluşturma ve Bağımlılıkların Kurulumu

Windows için:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac için:
```bash
python3 -m venv venv
source venv/bin/activate
```

Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

## Proje Yapısı

```
proje/
│
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base_agent.py
│   │   ├── data_collector.py
│   │   ├── data_processor.py
│   │   └── result_presenter.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py
│   │
│   ├── config.py
│   ├── exceptions.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_agents.py
│
├── data/
│   └── input.csv
│
├── results/
│   └── clustering.png
│
├── logs/
│   └── .log
│
├── requirements.txt
└── README.md
```

## Kullanım

### 1. Veri Hazırlama

- Veri dosyanızı `data/` klasörüne `input.csv` olarak yerleştirin.
- CSV dosyanız sayısal veriler içermeli ve eksik değer bulunmamalıdır.

### 2. Uygulamayı Çalıştırma

Ana uygulamayı çalıştırın:
```bash
python -m src.main
```

Tüm testleri çalıştırın:
```bash
pytest tests/
```

## Bağımlılıklar

Proje aşağıdaki Python paketlerini kullanmaktadır:

- **numpy (>=1.21.0)**: Sayısal işlemler ve veri manipülasyonu için
- **pandas (>=1.3.0)**: Veri çerçeveleri ve veri analizi için
- **scikit-learn (>=0.24.0)**: Makine öğrenmesi algoritmaları için
- **matplotlib (>=3.4.0)**: Veri görselleştirme için
- **seaborn (>=0.11.0)**: Gelişmiş görselleştirme için
- **pytest (>=7.0.0)**: Test otomasyonu için

## Geliştirme

### Pull Request Gönderme

1. Projeyi fork edin.
2. Yeni bir branch oluşturun:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Değişikliklerinizi commit edin:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Branch'inizi push edin:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Pull Request oluşturun.

### Kod Standartları

- PEP 8 standartlarına uyun.
- Docstring'leri güncel tutun.
- Yeni özellikler için test yazın.
- Commit mesajlarını açıklayıcı yazın.

## Hata Ayıklama

Eğer bir hata ile karşılaşırsanız:

1. `logs/` klasöründeki log dosyalarını kontrol edin.
2. Veri formatınızın doğru olduğundan emin olun.
3. Bağımlılıkların doğru sürümlerle yüklendiğini kontrol edin.

## Lisans

Bu proje [MIT](https://choosealicense.com/licenses/mit/) lisansı altında lisanslanmıştır.

## İletişim

Proje Sahibi - [@xatren](https://github.com/xatren)

Proje Linki: [https://github.com/xatren/Muneccim](https://github.com/xatren/Muneccim)