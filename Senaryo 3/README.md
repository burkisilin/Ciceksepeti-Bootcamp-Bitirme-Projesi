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

- Response Duration < 500 MS
Yük altında sunucunun cevap süresinin ne kadar değişkenlik gösterdiği gözlemlenmek üzere response duration assertinları yapılmıştır.

5 istemci ile 10 tekrar yapılarak aşağıdaki test sonuçları elde edilmiştir.

![image](https://user-images.githubusercontent.com/13181041/149926208-6f362bab-daa5-4844-bf70-bb77652a0c55.png)


20 istemci ile 10 tekrar yapılarak aşağıdaki test sonuçları elde edilmiştir.

![image](https://user-images.githubusercontent.com/13181041/149926364-bf65f787-a378-4437-9ddb-7f25815f2233.png)

İstemci sayısının 
