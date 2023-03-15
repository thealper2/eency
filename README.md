
# Eency

Fernet kütüphanesini kullanarak bir anahtar oluşturur. Bu anahtarı key.txt dosyasına kaydeder ve bu anahtarı kullanarak dosya/dosyaları şifreler. Tekrar key.txt dosyasındaki anahtarı kullanarak şifrelenmiş dosyaları çözer. Dosya şifrelendikten sonra key.txt dosyası asla silinmemelidir. Aksi halde dosya kalıcı olarak kaybedilebilir. Oluşabilecek tüm veri kayıplarından kullanıcı sorumludur.

---

## Önemli
key.txt dosyasını sakın silmeyin.

---

## Kullanımı

* Gerekli kütüphaneleri kurmak için;
```python
pip3 install -r requirements.txt
```

-h parametresi ile yardım menüsünü açabilirsiniz.

### Dosya şifrelemek için

* Tek bir dosyayı şifrelemek için;
```python
python3 eency.py --encryption --file DOSYANIN_TAM_YOLU
```

* Bir dizinin içindeki birden fazla dosyayi şifrelemek için;
```python
python3 eency.py --encryption --dir DIZNIN_TAM_YOLU
```

### Dosya şifresini çözmek için
* Şifrelenmiş ".eency" uzantılı tek bir dosyanın şifresini çözmek için;
```python
python3 eency.py --decryption --file DOSYANIN_TAM_YOLU
```

* Şifrelenmiş ".eency" uzantılı birden fazla dosyanın şifresini çözmek için;
```python
python3 eency.py --decryption --dir DIZININ_TAM_YOLU
```