 # Güvenlik Açığı İçeren Kod Deposu

Bu depo, yaygın web uygulaması güvenlik açıklarını, etkilerini, istismar edilme yöntemlerini ve uygun düzeltme tekniklerini göstermektedir. Geliştiriciler, güvenlik uzmanları ve güvenli kodlama uygulamaları hakkında bilgi edinmek isteyen herkes için eğitici bir kaynak görevi görür.

## Mevcut Güvenlik Açıkları

### 1. SQL Enjeksiyonu

**OWASP Kategorisi**: A03:2021 - Enjeksiyon

**CVSS Puanı**: 8.6 (Yüksek)


https://github.com/user-attachments/assets/0e693140-8935-4f43-bbb7-044e4a1fa7c7


**CVSS Vektör Dizesi**: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N

**Açıklama**: SQL Enjeksiyonu (SQLi), SQL veritabanlarını kullanan uygulamalardaki güvenlik açıklarından yararlanan bir kod enjeksiyon tekniğidir. Saldırganlar, güvenlik önlemlerini atlamak ve veritabanını manipüle etmek için giriş alanlarına kötü amaçlı SQL ifadeleri ekleyebilirler.

**Konum**: `/vulnerable-code/app.py`

**Düzeltilmiş Sürüm**: `/fixed-code/app.py`
### Vektör Bileşenlerinin Açıklaması:

- **AV:N** (Saldırı Vektörü: Ağ) - Güvenlik açığı ağ üzerinden uzaktan istismar edilebilir.
- **AC:L** (Saldırı Karmaşıklığı: Düşük) - Saldırı, özel koşullar veya durumlar gerektirmez ve tekrarlanabilir.
- **PR:N** (Gereken Ayrıcalıklar: Yok) - Saldırganın güvenlik açığını istismar etmek için hiçbir ayrıcalığa ihtiyacı yoktur.
- **UI:N** (Kullanıcı Etkileşimi: Yok) - Güvenlik açığını istismar etmek için kullanıcı etkileşimi gerekmez.
- **S:C** (Kapsam: Değişmiş) - Savunmasız bileşen, güvenlik kapsamının ötesindeki kaynakları etkiler.
- **C:H** (Gizlilik: Yüksek) - Gizlilikte tam bir kayıp vardır, saldırganın herhangi bir veritabanı içeriğine erişmesine izin verir.
- **I:N** (Bütünlük: Yok) - Bu özel uygulamada bütünlük üzerinde bir etki yoktur.
- *

https://github.com/user-attachments/assets/42becf62-388b-4c7e-8392-abe3f80c63da

*A:N** (Kullanılabilirlik: Yok) - Bu özel uygulamada kullanılabilirlik üzerinde bir etki yoktur.
