 # Güvenlik Açığı İçeren Kod Deposu

Bu depo, yaygın web uygulaması güvenlik açıklarını, etkilerini, istismar edilme yöntemlerini ve uygun düzeltme tekniklerini göstermektedir. Geliştiriciler, güvenlik uzmanları ve güvenli kodlama uygulamaları hakkında bilgi edinmek isteyen herkes için eğitici bir kaynak görevi görür.

## Mevcut Güvenlik Açıkları

### 1. SQL Enjeksiyonu

**OWASP Kategorisi**: A03:2021 - Enjeksiyon

**CVSS Puanı**: 8.6 (Yüksek)

**CVSS Vektör Dizesi**: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N

**Açıklama**: SQL Enjeksiyonu (SQLi), SQL veritabanlarını kullanan uygulamalardaki güvenlik açıklarından yararlanan bir kod enjeksiyon tekniğidir. Saldırganlar, güvenlik önlemlerini atlamak ve veritabanını manipüle etmek için giriş alanlarına kötü amaçlı SQL ifadeleri ekleyebilirler.

**Konum**: `/vulnerable-code/app.py`

**Düzeltilmiş Sürüm**: `/fixed-code/app.py`
