# storm_middleware_temporary
This small microservice serves as a middleware between the Hem3.0 client and Storm

Requrements:
- pipenv

Install dependencies
`pipenv install`

Start server
`python manage.py runserver`

The service has one route at: 
`/api/v1/index`
and takes a parameter: url, e.g:
`api/v1/index/?url=https://{{apihost}}.enferno.se/api/{{apipath}}/ProductService.svc/rest/GetProductByPartNo?format=json&partNo=PRD0001324`

