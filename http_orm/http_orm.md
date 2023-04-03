# Protocols
> **HTTP** - Hyper Text Transfer Protocol. Протокол, который построен на протоколах **TCP/IP**.

>**HTTPS** - более новая версия HTTP, где появилось шифрование и SSL сертификаты

## HTTP methods
* **GET** - Метод для получения данных
* **POST** - отправка данных на создание
* **PUT** - полное обновление или создание 
* **PATCH** - частичное обновление
* **DELETE** - удаление 
* TRACE - трассировка (проверка связи)
* HEAD - Получение списка headers для запроса
* OPTIONS - получение списка методов на данную url

# Status Code
* 1XX - информационные
* 2XX - успешные
* 3XX - перенаправление
* 4XX - ошибки со стороны клиента (front-end)
* 5XX - ошибки со стороны сервера (back-end)

# URL
> uniform resource locator (https://www.google.com/search?q=hello)
> **DOMAIN** - уникальное название к которому прикреплен определенный сервер (www.google.com)
> **URI** - кусочек URL (/search)
> **Query parameters** - пары (ключ-значение) после ? (q=hello)
* HOST - адрес на который мы отправляем запрос (ip address / domain)
* PORT - номер сервиса в сервере (http-server:80, posgresql:5432, backend:8000, frontend:3000)