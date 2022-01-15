# Burak Bayramoğlu Homework

Projede kullanılan endpointlere bu linkten ulaşabilirsiniz : https://bootcampapi.techcs.io/api/fe/v1/#/

# PROJE GEREKSİNİMLERİ

Projenin ayağa kalması için Postman ve aşağıdaki görselde paylaşılan Environmente ihtiyaç duyulmaktadır. İndirdiğiniz Collection'u Postman'ın içerisine import ettikten sonra belirtilen Environment'ı içe aktararak aktif olarak seçmeniz gerekmektedir.

![image](https://user-images.githubusercontent.com/13181041/149616456-e64d9f8d-4834-40dd-be23-5900c37a10d6.png)




# Sign Up Success
![image](https://user-images.githubusercontent.com/13181041/149616657-be020cfa-32cf-4159-9e7f-e2f796aa898b.png)


Testler
- Response Body is Valid
![image](https://user-images.githubusercontent.com/13181041/149616692-91d2570f-0d52-4243-9e3c-2f1d8a6c6bb4.png)

Request Body'de bulunan;

email'in String cinsinden olup olmadığının kontrolü,
password'un String cinsinden olup olmadığının kontrolü,
validateEmail fonksiyonu ile email'in geçerli bir email olup olmadığının kontrolü sağlanmıştır.



- Signed Up Succesfully
![image](https://user-images.githubusercontent.com/13181041/149616769-b2396364-991c-4e2d-b77c-ebb78d9fd808.png)


Response Body'de bulunan;

access_token değerinin String cinsinden olup olmadığının kontrolü,
access_token değerinin 175 karakter içerip içermediğinin kontrolü sağlanmıştır.



- Status Code is 200
![image](https://user-images.githubusercontent.com/13181041/149616811-d009fceb-40ba-4a2b-a2ce-97edc7750eaa.png)
Response kodunun 200 olup olmadığı kontrol edilmiştir. Swagger üzerinde belirtildiği üzere 200 kodu beklenirken 201 kodunun dönmesi üzerine test fail olmaktadır.


