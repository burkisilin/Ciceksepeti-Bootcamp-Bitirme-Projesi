# https://www.cicek.com Search Modülü ve Arama Sonrası İçin Yük Testi

https://www.cicek.com header da bulunan search modülü ve arama sonrası gidilen sonuçların listelendiği listeleme işlemi için kullanılan requestler şu şekildedir.

Aratılan metin : "orkide"

- https://www.cicek.com/Arama?query=orkide 
- https://www.cicek.com/Suggest/Get?key=orkide
- https://www.cicek.com/Catalog/AjaxCategory?query=orkide 

Yukarıda belirtilen requestler ile ilgili yük durumunda değişkenlik gösterilebileceği kanısına vardığım 3 adet test yapılmıştır.

- Response Code = 200 
- Response Message = OK
Sistemin yük altında çalışırken çökme sonucu dönen response kodunun "200" ve response mesajının "OK" olmayabileceği düşünülerek ve

- Response Duration < 700 MS
Yük altında sunucunun cevap süresinin ne kadar değişkenlik gösterdiği gözlemlenmek üzere response duration assertinları yapılmıştır.

10 istemci ile 10 tekrar yapılarak aşağıdaki test sonuçları elde edilmiştir.

![image](https://user-images.githubusercontent.com/13181041/149926920-82de5832-813c-411f-a5ac-1a8f5d925b34.png)



20 istemci ile 5 tekrar yapılarak aşağıdaki test sonuçları elde edilmiştir.

![image](https://user-images.githubusercontent.com/13181041/149927000-cacc2ab9-e4e9-4491-bd9a-0b1d4c861c54.png)

İstemci sayısının 
