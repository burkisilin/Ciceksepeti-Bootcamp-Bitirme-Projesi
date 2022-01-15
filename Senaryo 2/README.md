# Burak Bayramoğlu Homework

Projede kullanılan endpointlere bu linkten ulaşabilirsiniz : https://bootcampapi.techcs.io/api/fe/v1/#/

# PROJE GEREKSİNİMLERİ

Projenin ayağa kalması için Postman ve aşağıdaki görselde paylaşılan Environmente ihtiyaç duyulmaktadır. İndirdiğiniz Collection'u Postman'ın içerisine import ettikten sonra belirtilen Environment'ı içe aktararak aktif olarak seçmeniz gerekmektedir.

![image](https://user-images.githubusercontent.com/13181041/149616456-e64d9f8d-4834-40dd-be23-5900c37a10d6.png)




# Sign Up Success
![image](https://user-images.githubusercontent.com/13181041/149616657-be020cfa-32cf-4159-9e7f-e2f796aa898b.png)

Pre-request Script üzerinde rastgele üretilen mail ve password değerleri Environment üzerine set edilir.

- Response Body is Valid
```javascript
pm.test("Request Body is Valid", () =>{
    
    pm.expect(typeof(email) == "string").to.be.true;
    pm.expect(typeof(password) == "string").to.be.true;
    pm.expect(validateEmail(email)).equal(true,"Email is not valid. "); // Check if email is valid.
});
```

Request Body'de bulunan;

email'in String cinsinden olup olmadığının kontrolü,
password'un String cinsinden olup olmadığının kontrolü,
validateEmail fonksiyonu ile email'in geçerli bir email olup olmadığının kontrolü sağlanmıştır.



- Signed Up Succesfully
```javascript
pm.test('Signed Up Successfully.', () =>{
pm.expect(typeof(jsonData.access_token) == "string").to.be.true
pm.expect(jsonData.access_token.length).to.be.equal(175)
});
```

Response Body'de bulunan;

access_token değerinin String cinsinden olup olmadığının kontrolü,
access_token değerinin 175 karakter içerip içermediğinin kontrolü sağlanmıştır.



- Status Code is 200
```javascript
pm.test('Status Code is 200', () =>{
    pm.expect(pm.response.code).equal(200,'Status received is ' + pm.response.code + '. User successfully signed-up -> Response code must be 200 due to Swagger API Documentation. '); // user successfully signed-up -> Response code must be 200 due to Swagger API Documentation. 
});
```
Response kodunun 200 olup olmadığı kontrol edilmiştir. Swagger üzerinde belirtildiği üzere 200 kodu beklenirken 201 kodunun dönmesi üzerine test fail olmaktadır.

# Sign In Success
![image](https://user-images.githubusercontent.com/13181041/149617747-8c976763-b27e-47d3-941b-ccf86adba97d.png)

Pre-request Script üzerinden sistemde kayıtlı bir mail ve password değeri Environment üzerine set edilir.


- Request Body Types are Valid
```javascript
pm.test("Request Body Types are Valid", () =>{
    pm.expect(typeof(email) == "string").to.be.true;
    pm.expect(typeof(password) == "string").to.be.true;
});
```
- Response Body Types are Valid
```javascript
pm.test("Response Body Types are Valid", () =>{
    pm.expect(typeof(jsonData.access_token) == "string").to.be.true
});
```
- Signed In Successfully
```javascript
    pm.expect(pm.response.text()).to.include("access_token")
    pm.expect(jsonData.access_token.length).to.be.equal(175)
});
```
- Status Code is 200
```javascript
pm.test('Status Code is 200', () =>{
    pm.expect(pm.response.code).equal(200,'Status received is ' + pm.response.code + '. User successfully signed-up -> Response code must be 200 due to Swagger API Documentation. '); // user successfully signed-up -> Response code must be 200 due to Swagger API Documentation. 
});
```
