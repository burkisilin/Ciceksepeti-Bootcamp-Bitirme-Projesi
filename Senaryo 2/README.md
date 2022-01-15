# Burak Bayramoğlu Homework

Projede kullanılan endpointlere bu linkten ulaşabilirsiniz : https://bootcampapi.techcs.io/api/fe/v1/#/

# PROJE GEREKSİNİMLERİ

Projenin ayağa kalması için Postman ve aşağıdaki görselde paylaşılan Environmente ihtiyaç duyulmaktadır. İndirdiğiniz Collection'u Postman'ın içerisine import ettikten sonra belirtilen Environment'ı içe aktararak aktif olarak seçmeniz gerekmektedir.

![image](https://user-images.githubusercontent.com/13181041/149616456-e64d9f8d-4834-40dd-be23-5900c37a10d6.png)




# Sign Up Success
![image](https://user-images.githubusercontent.com/13181041/149616657-be020cfa-32cf-4159-9e7f-e2f796aa898b.png)

Pre-request Script üzerinde rastgele üretilen mail ve password değerleri Environment üzerine set edilir.

- Request Body is Valid
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
Request Body'de bulunan;

email'in String cinsinden olup olmadığının kontrolü,
password'un String cinsinden olup olmadığının kontrolü sağlanmıştır.


- Response Body Types are Valid
```javascript
pm.test("Response Body Types are Valid", () =>{
    pm.expect(typeof(jsonData.access_token) == "string").to.be.true
});
```
Response Body'de bulunan;

access_token değerinin String cinsinden olup olmadığının kontrolü sağlanmıştır.




- Signed In Successfully
```javascript
    pm.expect(pm.response.text()).to.include("access_token")
    pm.expect(jsonData.access_token.length).to.be.equal(175)
});
```

Response'de  "access_token" değerinin bulunup bulunmadığı ve access_token'in 175 karakterden oluşup oluşmadığı kontrol edilmiştir.

- Status Code is 200
```javascript
pm.test('Status Code is 200', () =>{
    pm.expect(pm.response.code).equal(200,'Status received is ' + pm.response.code + '. User successfully signed-up -> Response code must be 200 due to Swagger API Documentation. '); // user successfully signed-up -> Response code must be 200 due to Swagger API Documentation. 
});
```

Response kodunun 200 olup olmadığı kontrol edilmiştir. Swagger üzerinde belirtildiği üzere 200 kodu beklenirken 201 kodunun dönmesi üzerine test fail olmaktadır.

# Sign In Fail - Wrong Credentials
![image](https://user-images.githubusercontent.com/13181041/149618932-8f0ea5ad-108d-4a6b-b3a5-3b0dc7cc1622.png)

Giriş bilgileri body üzerinden yanlış set edilmiştir. 
```json
{
  "email": "wrongMail",
  "password": "wrongPassword"
}
```

- Request Body Types are Valid
```javascript
pm.test("Request Body Types are Valid", () =>{
    pm.expect(typeof(email) == "string").to.be.true;
    pm.expect(typeof(password) == "string").to.be.true;
});
```
Request Body'de bulunan;

email'in String cinsinden olup olmadığının kontrolü, 
password'un String cinsinden olup olmadığının kontrolü sağlanmıştır.

- Response Body Types are Valid
```javascript
pm.test("Response Body Types are Valid", () =>{
    pm.expect(typeof(jsonData.statusCode) == "number").to.be.true
    pm.expect(typeof(jsonData.message) == "string").to.be.true
});
```

- Unsuccessful Sign In
```javascript
pm.test('Unsuccessful Sign In', () =>{
    pm.expect(pm.response.text()).to.include("Unauthorized")
    pm.expect(pm.response.text()).to.not.include("access_token")
});
```
Response Body'de;
Unauthorized kısmının bulunduğu,
acces_token'in bulunmadığı kontrol edilmiştir.

- Status Code is 401
```javascript
pm.test('Status Code is 401', () =>{
    pm.expect(pm.response.code).equal(401,'Status received is ' + pm.response.code); // Response code must be 401 due to Swagger API Documentation. 
});
```
Response kodunun 401 olup olmadığı kontrol edilmiştir. 

```javascript
function randomStringGenerator(length){
    var charset = 'abcdefghkmnpqrstuvwxyz23456789';
    return new Array(length)
      .fill(null)
      .map(()=> charset.charAt(Math.floor(Math.random() * charset.length)))
      .join('');

}

function setRequestBody(emailField,passwordField)
{
    switch (emailField)
    {
        case "validEmail":
            email = randomStringGenerator(3) + "@" +randomStringGenerator(5)+ ".com"
            break
        case "invalidEmail":
            email = randomStringGenerator(6) + ".com"
            break
        case "emptyEmail":
            email = ""
            break
    }

        switch (passwordField)
    {
        case "validPassword":
            
            password = randomStringGenerator(8)
            break
        case "invalidPassword":
            moreChars = Math.random() < 0.5 // Determine with %50 probability, if password is going to be invalid because of having more than 20 or below 8 characters. If password is going to be 20+ characters.
            if (moreChars == true){ // Determines the invalid password lenght to be below 8 or more then 20 chars.
                passwordLength = Math.floor(Math.random() * 11) + 21; // Set length from 21 to 31
            }
            else{
                passwordLength = Math.floor(Math.random() * 7) + 1; // Set length from 1 to 7
            }
            password = randomStringGenerator(passwordLength)
            break
        case "emptyPassword":
            password = ""
            break
    }

    pm.environment.set("email", email)
    pm.environment.set("password", password)
}

function returnRandomItemFromArray(array)
{
    return array[Math.floor(Math.random() * array.length)];
}

function setFieldsInvalidRandomly(){ // Sets one of either fields invalid randomly. So when collection iterated more then one time each condution can be tested.
    invalidEmailSituations = ["invalidEmail", "emptyEmail"]
    invalidPasswordSituations = ["invalidPassword", "emptyPassword"]
    invalidFields = [returnRandomItemFromArray(invalidEmailSituations), returnRandomItemFromArray(invalidPasswordSituations)]
    pm.environment.set("invalidFields", invalidFields)
    setRequestBody(invalidFields[0], invalidFields[1])
}
```

Yukarıda bulunan kodlar ile Request ile gönderilecek body'de bulunan email ve password otomatize olarak rastgele olarak geçersiz veya boş olarak tanımlanmaktadır.
![image](https://user-images.githubusercontent.com/13181041/149619295-ac1080ba-03ee-4030-8714-fea35abbe0d6.png)
Yapılan 3. test olan Request Body Invalid testinde rastgele oluşturulup request gönderilen parametrelerin invalid/empty olup olmadığı görülebilmektedir. Senaryonun rastgele oluşturulması, Collection koşumu sırasında iterasyon sayısı ayarlanarak mümkün olan tüm geçersiz parametre testlerinin yapılmasını sağlamaktadır.

# Sign Up Fail - Invalid Fields
![image](https://user-images.githubusercontent.com/13181041/149619152-ab6745c2-fb9b-423e-9b05-fff096029eea.png)

Geçersiz alanların ayarlanması için Postmanda bulunan Pre-request Script kısmından yararlanılmıştır. 




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
    pm.expect(typeof(jsonData.statusCode) == "number").to.be.true;
    pm.expect(typeof(jsonData.message) == "object").to.be.true;
    pm.expect(typeof(jsonData.error) == "string").to.be.true;
});
```

- Request Body Invalid Field Errors Case
```javascript
pm.test("Request Body Invalid Field Errors Case: "+ invalidFieldsCase, () =>{
    if (validateEmail(email) == false){
        pm.expect(pm.response.text()).to.include("email must be an email")
    }

    if (email.length == 0){
        pm.expect(pm.response.text()).to.include("mail should not be empty")
    }

    if (validatePassword == false){
        pm.expect(pm.response.text()).to.include("password must be shorter than or equal to 20 characters")
    }

    if (password.length == 0){
        pm.expect(pm.response.text()).to.include("password should not be empty")
    }

});
```

- Status Code is 400
```javascript
pm.test('Status Code is 400', () =>{
    pm.expect(pm.response.code).equal(400,'Status received is ' + pm.response.code); // Respopnse code must be 400 due to Swagger API Documentation.
});
```

```javascript
```

```javascript
```
