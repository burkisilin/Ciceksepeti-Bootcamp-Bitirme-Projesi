# PROJENİN AYAĞA KALDIRILMASI

Projenin ayağa kaldırılması için öncelikle Python ve gerekli paketlerin kurulması gerekmektedir. Aşağıda bulunan kodu çalıştırarak gerekli paketlerin kurulumunu otomatik olarak gerçekleştirebilirsiniz. 

```
pip install -r /path/to/requirements.txt
```



Projenin bulunduğu dizinde CMD üzerinden aşağıda bulunan kodu çalıştırarak testleri koşmaya başlayabilirsiniz.
```
py.test --html=report.html --capture=tee-sys
```
![image](https://user-images.githubusercontent.com/13181041/149815898-94aa2f3c-e139-43ce-8d12-96edb7269d6e.png)


# TEST EDİLEN SENARYOLAR #

- https://www.mizu.com/flowers ‘da aşağı scroll yaptıkça ilk 10 sayfa için her sayfada 60 ürün geldiğinin kontrolü.

- https://www.mizu.com/flowers sayfasında filtre alanından sort: price high to low seçilip listeleme sayfasındaki ürünlerin doğru fiyat sırasıyla listelendiğinin kontrolü.

- https://www.mizu.com menü altında bulunan tüm alt kategorilerin linklerinin kırık olup olmadığının kontrolü.

```
```

# RAPORLAMA

![image](https://user-images.githubusercontent.com/13181041/149817712-a4eea80b-cd97-46fa-a7a6-11f3ee10dab7.png)

