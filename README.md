<a name="inicio"></a>
# sdk-python
Modulo para conexión con gateway de pago Todo Pago		
		
######[Instalación](#instalacion)		
######[Versiones de Python soportadas](#Versionesdepythonsoportadas)
######[Generalidades](#general)	
######[Uso](#uso)		
######[Datos adicionales para prevencion de fraude] (#datosadicionales) 		
######[Ejemplo](#ejemplo)		
######[Modo test](#test)
######[Status de la operación](#status)
######[Consulta de operaciones por rango de tiempo](#GBRDT)
######[Devoluciones](#devoluciones)
######[Tablas de referencia](#tablas)
<!--######[Formulario hibrido](#FormularioHibrido)-->
 		
<a name="instalacion"></a>		
## Instalación		
El SDK utiliza como dependencias *suds-jurko*, *requests* y *xmltodict*. Para instalarlas correr las siguientes lineas en la consola:
ej: pip install suds-jurko <-- instalar la dependencia
```bash
> pip install suds-jurko
> pip install requests
```

[<sub>Volver a inicio</sub>](#inicio)

<a name="Versionesdepythonsoportadas"></a>		
##Versiones de Python soportadas
La versión implementada de la SDK, esta testeada para versiones desde Python 2.7 en adelante. 
[<sub>Volver a inicio</sub>](#inicio)

<a name="general"></a>
##Genaralidades
Esta versión soporta únicamente pago en moneda nacional argentina (CURRENCYCODE = 32).
Todos los métodos devuelven la respuesta en forma de diccionario.
[<sub>Volver a inicio</sub>](#inicio)

<a name="uso"></a>		
## Uso

####1. Inicializar la clase correspondiente al conector (TodoPago).

- crear un JSON con los http header suministrados por todo pago
```python
j_header_http = {
    "Authorization":"PRISMA f3d8b72c94ab4a06be2ef7c95490f7d3"
}
```
- crear una instancia de la clase TodoPago para hacer pruebas en el ambiente developers se pasa como modo "test" y para producción "prod".

```python
tpc = TodoPagoConnector(j_header_http, 'test')

```		
		
####2.Solicitud de autorización		
En este caso hay que llamar a sendAuthorizeRequest(). 		
```python	
response = tpc.sendAuthorizeRequest(optionsSAR_comercio, optionsSAR_operacion)
```		
<ins><strong>Datos propios del comercio</strong></ins>		
optionsSAR_comercio debe ser un Hash con la siguiente estructura:		
		
```python
optionsSAR_comercio = {
"Session": "ABCDEF-1234-12221-FDE1-00000200",
"Security": "f3d8b72c94ab4a06be2ef7c95490f7d3",
"EncodingMethod": "XML",
"URL_OK": "http,//someurl.com/ok/",
"URL_ERROR": "http,//someurl.com/fail/",
"EMAILCLIENTE": "email_cliente@dominio.com"
}
```		

<ins><strong>Datos propios de la operación</strong></ins>		
optionsSAR_operacion debe ser un Hash con la siguiente estructura:		
		
```python
optionsSAR_operacion = {
"MERCHANT": "2153",
"OPERATIONID": "8000",
"CURRENCYCODE": "032",
"AMOUNT": "1.00"
}
```

<!--
#Optionals
"AVAILABLEPAYMENTMETHODSIDS": "1#194#43#45",
"PUSHNOTIFYMETHOD" : "",
"PUSHNOTIFYENDPOINT": "",  
"PUSHNOTIFYSTATES": ""
}
```-->
La variable <strong>response</strong> contendrá una estuctura en la cual <strong>url_request</strong> nos dara la url del formulario de pago a la cual habra que redirigir al comprador y <strong>request_key</strong> será un datos que será requerido en el paso de la confirmación de la transacción a través del método <strong>getAuthorizeRequest</strong>

####3.Confirmación de transacción.		
En este caso hay que llamar a getAuthorizeRequest(), enviando como parámetro un Hash como se describe a continuación.		
```python
optionsGAA = {
'Security': 'f3d8b72c94ab4a06be2ef7c95490f7d3',
'Merchant': "2153",
'RequestKey': '710268a7-7688-c8bf-68c9-430107e6b9da',
'AnswerKey': '693ca9cc-c940-06a4-8d96-1ab0d66f3ee6'
}

tpc.getAuthorizeAnswer(optionsGAA)
```		
[<sub>Volver a inicio</sub>](#inicio)		

<a name="datosadicionales"></a>		
## Datos adicionales para control de fraude				
				
```python	
optionsSAR_operacion={ 		
...........................................................................		
'CSBTCITY': "Villa General Belgrano", #Ciudad de facturación, #MANDATORIO.		
'CSBTCOUNTR': "AR", #País de facturación. MANDATORIO. Código ISO. (http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)		
'CSBTCUSTOMERID': "453458", #Identificador del usuario al que se le emite la factura. MANDATORIO. No puede contener un correo electrónico.		
'CSBTIPADDRESS': "192.0.0.4", #IP de la PC del comprador. MANDATORIO.		
'CSBTEMAIL' : "some@someurl.com", #Mail del usuario al que se le emite la factura. MANDATORIO.		
'CSBTFIRSTNAME': "Juan", #Nombre del usuario al que se le emite la factura. MANDATORIO.		
'CSBTLASTNAME': "Perez", #Apellido del usuario al que se le emite la factura. MANDATORIO.		
'CSBTPHONENUMBER': "541160913988", #Teléfono del usuario al que se le emite la factura. No utilizar guiones, puntos o espacios. Incluir código de país. MANDATORIO.		
'CSBTPOSTALCODE': "1010", #Código Postal de la dirección de facturación. MANDATORIO.		
'CSBTSTATE': "B",  #Provincia de la dirección de facturación. MANDATORIO. Ver tabla anexa de provincias.		
'CSBTSTREET1' : "Some Street 2153", #Domicilio de facturación (calle y nro). MANDATORIO.		
'CSBTSTREET2' :"Piso 8", #Complemento del domicilio. (piso, departamento). NO MANDATORIO.		
'CSPTCURRENCY': "ARS",  #Moneda. MANDATORIO.		
'CSPTGRANDTOTALAMOUNT': "10.01", #Con decimales opcional usando el puntos como separador de decimales. No se permiten comas, ni como separador de miles ni como separador de decimales. MANDATORIO. (Ejemplos:$125,38-> 125.38 $12-> 12 o 12.00)
'CSMDD7':"", # Fecha registro comprador(num Dias). NO MANDATORIO.		
'CSMDD8':"", #Usuario Guest? (Y/N). En caso de ser Y, el campo CSMDD9 no deberá enviarse. NO MANDATORIO.	
'CSMDD9':"", #Customer password Hash: criptograma asociado al password del comprador final. NO MANDATORIO.	
'CSMDD10':"", #Histórica de compras del comprador (Num transacciones). NO MANDATORIO.		
'CSMDD11':"", #Customer Cell Phone. NO MANDATORIO.		

#Retail
'CSSTCITY':"Villa General Belgrano",  #Ciudad de enví­o de la orden. MANDATORIO.		
'CSSTCOUNTRY':"AR", #País de envío de la orden. MANDATORIO.		
'CSSTEMAIL': "some@someurl.com", #Mail del destinatario, MANDATORIO.		
'CSSTFIRSTNAME':"Jose", #Nombre del destinatario. MANDATORIO.		
'CSSTLASTNAME':"Perez", #Apellido del destinatario. MANDATORIO.		
'CSSTPHONENUMBER':"541155893737", #Número de teléfono del destinatario. MANDATORIO.		
'CSSTPOSTALCODE':"1010", #Código postal del domicilio de envío. MANDATORIO.		
'CSSTSTATE':"B", #Provincia de envío. MANDATORIO. Son de 1 caracter		
'CSSTSTREET1':"Some Street 2153", #Domicilio de envío. MANDATORIO.		

'CSITPRODUCTCODE':"electronic_good", #Código de producto. CONDICIONAL. Valores posibles(adult_content;coupon;default;electronic_good;electronic_software;gift_certificate;handling_only;service;shipping_and_handling;shipping_only;subscription)		
'CSITPRODUCTDESCRIPTION':"Test Prd Description", #Descripción del producto. CONDICIONAL.	
'CSITPRODUCTNAME':"TestPrd", #Nombre del producto. CONDICIONAL.		
'CSITPRODUCTSKU':"SKU1234", #Código identificador del producto. CONDICIONAL.		
'CSITTOTALAMOUNT':"10.01", #CSITTOTALAMOUNT=CSITUNITPRICE*CSITQUANTITY "999999[.CC]" Con decimales opcional usando el puntos como separador de decimales. No se permiten comas, ni como separador de miles ni como separador de decimales. CONDICIONAL.		
'CSITQUANTITY':"1", #Cantidad del producto. CONDICIONAL.		
'CSITUNITPRICE': "10.01", #Formato Idem CSITTOTALAMOUNT. CONDICIONAL.		

'CSMDD12':"" #Shipping, DeadLine (Num Dias). NO MADATORIO.		
'CSMDD13':"", #Método de Despacho. NO MANDATORIO.		
'CSMDD14':"", #Customer requires Tax Bill ? (Y/N). NO MANDATORIO.		
'CSMDD15':"", #Customer Loyality Number. NO MANDATORIO. 		
'CSMDD16':"", #Promotional / Coupon Code. NO MANDATORIO. #Retail: datos a enviar por cada producto, los valores deben estar separado con #:		

...........................................................		
```		
<a name="ejemplo"></a>		
## Ejemplo		          
Existe un ejemplo en la carpeta https://github.com/TodoPago/sdk-python/blob/master/lib/prueba.py que muestra los resultados de los métodos principales del SDK.		

<a name="test"></a>
##Modo test
Para utlilizar el modo test se debe pasar un end point de prueba (provisto por TODO PAGO).
````python
tpc = TodoPagoConnector(j_header_http_test, j_wsdls_test, end_point_test)
```
[<sub>Volver a inicio</sub>](#inicio)

<a name="status"></a>
##Status de la operación
La SDK cuenta con un método para consultar el status de la transacción desde la misma SDK. El método se utiliza de la siguiente manera:
```python
optionsGS = {
'MERCHANT': merchant, #merchant es una variable que contiene al id site 
'OPERATIONID': operationid # operationid es un variable (id de la operacion a consultar)
}
print tpc.getByoperationId(optionsGS)
```

[<sub>Volver a inicio</sub>](#inicio)


<a name="GBRDT"></a>
##Consulta de operaciones por rango de tiempo.
En este caso hay que llamar a getByRangeDateTime() y devolvera todas las operaciones realizadas en el rango de fechas dado
```python
optionsGBRDT = {
'MERCHANT': '2153',
'STARTDATE': '2015-01-01T17:34:42.903',
'ENDDATE': '2015-12-10T17:34:42.903'
}
response = tpc.getByRangeDateTime(optionsGBRDT)
```
[<sub>Volver a inicio</sub>](#inicio)

<a name="devolucones"></a>

<a name="devoluciones"></a>
## Anulaciones y Devoluciones

La SDK dispone de métodos para realizar la anulación o la devolución online, total o parcial, de una transacción realizada a traves de TodoPago.

#### Anulaciones

Se debe llamar al método ```voidRequest``` de la siguiente manera:
```python

options = {
"Security" : "837BE68A892F06C17B944F344AEE8F5F", #API Key del comercio asignada por TodoPago 
"Merchant" : "35", #Merchant o Nro de comercio asignado por TodoPago
"RequestKey" : "6d2589f2-37e6-1334-7565-3dc19404480c" #RequestKey devuelto como respuesta del servicio SendAutorizeRequest
}
resp = tpc.voidRequest(options)	
```

También se puede llamar al método ```voidRequest``` de la esta otra manera:
```python

options = {
"Security" : "837BE68A892F06C17B944F344AEE8F5F", #API Key del comercio asignada por TodoPago 
"Merchant" : "35", #Merchant o Nro de comercio asignado por TodoPago
"AuthorizationKey" : "6d2589f2-37e6-1334-7565-3dc19404480c" #AuthorizationKey devuelto como respuesta del servicio GetAuthorizeAnswer
}
resp = tpc.voidRequest(options)	
```

#### Devoluciones

Se debe llamar al método ```returnRequest``` de la siguiente manera:
```python

options = {
"Security" : "837BE68A892F06C17B944F344AEE8F5F", #API Key del comercio asignada por TodoPago 
"Merchant" : "35", #Merchant o Nro de comercio asignado por TodoPago
"RequestKey" : "6d2589f2-37e6-1334-7565-3dc19404480c" #RequestKey devuelto como respuesta del servicio SendAutorizeRequest
"AMOUNT" : "23.50" #Opcional. Monto a devolver, si no se envía, se trata de una devolución total
}
resp = tpc.returnRequest(options)
```

También se puede llamar al método ```returnRequest``` de la esta otra manera:
```python

options = {
"Security" : "837BE68A892F06C17B944F344AEE8F5F", #API Key del comercio asignada por TodoPago 
"Merchant" : "35", #Merchant o Nro de comercio asignado por TodoPago
"AuthorizationKey" : "6d2589f2-37e6-1334-7565-3dc19404480c" #AuthorizationKey devuelto como respuesta del servicio GetAuthorizeAnswer
"AMOUNT" : "23.50" #Opcional. Monto a devolver, si no se envía, se trata de una devolución total
}
resp = tpc.returnRequest(options)	
```

#### Respuesta de los servicios

Si la operación fue realizada correctamente se informará con un código 2011 y un mensaje indicando el éxito de la operación.

```python
(reply){
StatusCode = 2011
StatusMessage = "Operacion OK"
AuthorizationKey = "30e72e14-043c-a740-7bfa-95f976d8f0a7"
AUTHORIZATIONCODE = "2011"
}
```

[<sub>Volver a inicio</sub>](#inicio)	


<a name="tablas"></a>
## Tablas de Referencia		
######[Códigos de Estado](#cde)		
######[Provincias](#p)		
<a name="cde"></a>		
<p>Codigos de Estado</p>		
<table>		
<tr><th>IdEstado</th><th>Descripción</th></tr>		
<tr><td>1</td><td>Ingresada</td></tr>		
<tr><td>2</td><td>A procesar</td></tr>		
<tr><td>3</td><td>Procesada</td></tr>		
<tr><td>4</td><td>Autorizada</td></tr>		
<tr><td>5</td><td>Rechazada</td></tr>		
<tr><td>6</td><td>Acreditada</td></tr>		
<tr><td>7</td><td>Anulada</td></tr>		
<tr><td>8</td><td>Anulación Confirmada</td></tr>		
<tr><td>9</td><td>Devuelta</td></tr>		
<tr><td>10</td><td>Devolución Confirmada</td></tr>		
<tr><td>11</td><td>Pre autorizada</td></tr>		
<tr><td>12</td><td>Vencida</td></tr>		
<tr><td>13</td><td>Acreditación no cerrada</td></tr>		
<tr><td>14</td><td>Autorizada *</td></tr>		
<tr><td>15</td><td>A reversar</td></tr>		
<tr><td>16</td><td>A registar en Visa</td></tr>		
<tr><td>17</td><td>Validación iniciada en Visa</td></tr>		
<tr><td>18</td><td>Enviada a validar en Visa</td></tr>		
<tr><td>19</td><td>Validada OK en Visa</td></tr>		
<tr><td>20</td><td>Recibido desde Visa</td></tr>		
<tr><td>21</td><td>Validada no OK en Visa</td></tr>		
<tr><td>22</td><td>Factura generada</td></tr>		
<tr><td>23</td><td>Factura no generada</td></tr>		
<tr><td>24</td><td>Rechazada no autenticada</td></tr>		
<tr><td>25</td><td>Rechazada datos inválidos</td></tr>		
<tr><td>28</td><td>A registrar en IdValidador</td></tr>		
<tr><td>29</td><td>Enviada a IdValidador</td></tr>		
<tr><td>32</td><td>Rechazada no validada</td></tr>		
<tr><td>38</td><td>Timeout de compra</td></tr>		
<tr><td>50</td><td>Ingresada Distribuida</td></tr>		
<tr><td>51</td><td>Rechazada por grupo</td></tr>		
<tr><td>52</td><td>Anulada por grupo</td></tr>		
</table>		
		
<a name="p"></a>		
<p>Provincias</p>
<p>Solo utilizado para incluir los datos de control de fraude</p>
<table>		
<tr><th>Provincia</th><th>Código</th></tr>		
<tr><td>CABA</td><td>C</td></tr>		
<tr><td>Buenos Aires</td><td>B</td></tr>		
<tr><td>Catamarca</td><td>K</td></tr>		
<tr><td>Chaco</td><td>H</td></tr>		
<tr><td>Chubut</td><td>U</td></tr>		
<tr><td>Córdoba</td><td>X</td></tr>		
<tr><td>Corrientes</td><td>W</td></tr>		
<tr><td>Entre Ríos</td><td>E</td></tr>		
<tr><td>Formosa</td><td>P</td></tr>		
<tr><td>Jujuy</td><td>Y</td></tr>		
<tr><td>La Pampa</td><td>L</td></tr>		
<tr><td>La Rioja</td><td>F</td></tr>		
<tr><td>Mendoza</td><td>M</td></tr>		
<tr><td>Misiones</td><td>N</td></tr>		
<tr><td>Neuquén</td><td>Q</td></tr>		
<tr><td>Río Negro</td><td>R</td></tr>		
<tr><td>Salta</td><td>A</td></tr>		
<tr><td>San Juan</td><td>J</td></tr>		
<tr><td>San Luis</td><td>D</td></tr>		
<tr><td>Santa Cruz</td><td>Z</td></tr>		
<tr><td>Santa Fe</td><td>S</td></tr>		
<tr><td>Santiago del Estero</td><td>G</td></tr>		
<tr><td>Tierra del Fuego</td><td>V</td></tr>		
<tr><td>Tucumán</td><td>T</td></tr>		
</table>		
[<sub>Volver a inicio</sub>](#inicio)

<!--
<a name="FormularioHibrido"></a>
##Formulario hibrido

### Conceptos basicos

El formulario hibrido, es una alternativa al medio de pago actual por formulario externo.

El plugin tiene que permitir seleccionar entre el formulario externo actual o el integrado al e-commerce. La seleccion de uno u otro se debe realizar desde una subseccion en la pagina todopago de admin.

### Ubicacion en el proceso de pago

Integrado al e-commerce la pagina del formulario tiene que mostrarse en el proceso de pago luego del paso de confirmacion.

### Parametros requeridos

El formulario requiere 5 parametros obligatorios. El PublicRequestKey (entregado por el SAR), MerchantId, nombre completo de usuario, mail y monto de la compra. Estos datos son requeridos al inicializar el formulario en la pagina:

window.TPFORMAPI.hybridForm.setItem({
  publicKey: taf08222e-7b32-63d4-d0a6-5cabedrb5782,
  merchantId: 35,
  defaultNombreApellido: "Juan Perez",
  defaultMail: "juanperez@mail.com",
  numericAmount: 999
});

### Endpoints

El formulario requiere endpoints para la realizacion del pagos, estos se setean en la libreria TPHybridForm-v0.1.js.

El ajax de seleccion de medio de pago y del banco , requiere:

cfg.API_URL = 'http://developers.todopago.com.ar/t/1.1/api/';

Endpoint de pago por billetera:

cfg.FORM_EMBEDED_URL = 'https://developers.todopago.com.ar/formulario2/commands';

Endpoint de pago:

cfg.FORM_PAYMENT_ENDPOINT = 'http://localhost:8280/t/1.1/FormPaymentRest';

### Callbacks de pago

El formulario posee callbacks, que revuelven el estado y la informacion del luego del pago realizado:

billeteraPaymentResponse: Devuelve el response del pago si el pago por billetera se realizo satisfactoriamente.

customPaymentSuccessResponse: Devuelve response si el pago se realizo correctamente.

customPaymentErrorResponse: Si hubo algun error durante el proceso de pago, este devuelve el response con el codigo y mensaje correspondiente.

### Directivas Ajax

El formulario requiere las siguientes directivas de CORS para el cross-origin HTTP request.

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept');
		

[<sub>Volver a inicio</sub>](#inicio)
-->
