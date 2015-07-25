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
######[Tablas de referencia](#tablas)		
 		
<a name="instalacion"></a>		
## Instalación		
El SDK utiliza como dependencia <b>suds-jurko</b>
ej: pip install suds-jurko <-- instalar la dependencia

[<sub>Volver a inicio</sub>](#inicio)

<a name="Versionesdepythonsoportadas"></a>		
##Versiones de Python soportadas
La versión implementada de la SDK, esta testeada para versiones desde Python 2.7 en adelante. 
[<sub>Volver a inicio</sub>](#inicio)

<a name="general"></a>
##Genaralidades
Esta versión soporta únicamente pago en moneda nacional argentina (CURRENCYCODE = 32),
[<sub>Volver a inicio</sub>](#inicio)

<a name="uso"></a>		
## Uso

####1. Inicializar la clase correspondiente al conector (TodoPago).
- crear un JSON con las wsdl suministradas por Todo Pago

```python
j_wsdls = {
'Operations': 'https://developers.todopago.com.ar/services/Operations?wsdl',
'Authorize': 'https://developers.todopago.com.ar/services/Authorize?wsdl',
'PaymentMethods': 'https://developers.todopago.com.ar/services/PaymentMethods?wsdl'}
```
- crear un JSON con los http header suministrados por todo pago
```python
j_header_http = {
    "Authorization":"PRISMA 912EC803B2CE49E4A541068D495AB570"
}
```
- crear una instancia de la clase TodoPago

```python
tpc = TodoPagoConnector(j_header_http, j_wsdls, 'https://developers.todopago.com.ar/services/')

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
'Merchant': '350',
'EncodingMethod': 'XML',
'Security': '1234567890ABCDEF1234567890ABCDEF',
'URL_OK'="http://www.mysitio.com/true",
'URL_ERROR'="http://www.misitio.com/true"
}
```		

<ins><strong>Datos propios de la operación</strong></ins>		
optionsSAR_operacion debe ser un Hash con la siguiente estructura:		
		
```python
optionsSAR_operacion = {
'MERCHANT': "305",
'OPERATIONID': "ABCDEF-1234-12221-FDE1-00000200",
'CURRENCYCODE': "032",
'AMOUNT': "50"
}
```		
La variable <strong>response</strong> contendrá una estuctura en la cual <strong>url_request</strong> nos dara la url del formulario de pago a la cual habra que redirigir al comprador y <strong>request_key</strong> será un datos que será requerido en el paso de la confirmación de la transacción a través del método <strong>getAuthorizeRequest</strong>

####3.Confirmación de transacción.		
En este caso hay que llamar a getAuthorizeRequest(), enviando como parámetro un Hash como se describe a continuación.		
```python
optionsGAA = {
'Security': '1234567890ABCDEF1234567890ABCDEF',
'Merchant': "305",
'RequestKey': '8496472a-8c87-e35b-dcf2-94d5e31eb12f',
'AnswerKey': '8496472a-8c87-e35b-dcf2-94d5e31eb12f'
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
'CSBTEMAIL' : "decidir@hotmail.com", #Mail del usuario al que se le emite la factura. MANDATORIO.		
'CSBTFIRSTNAME': "Juan", #Nombre del usuario al que se le emite la factura. MANDATORIO.		
'CSBTLASTNAME': "Perez", #Apellido del usuario al que se le emite la factura. MANDATORIO.		
'CSBTPHONENUMBER': "541160913988", #Teléfono del usuario al que se le emite la factura. No utilizar guiones, puntos o espacios. Incluir código de país. MANDATORIO.		
'CSBTPOSTALCODE': "C1010AAP", #Código Postal de la dirección de facturación. MANDATORIO.		
'CSBTSTATE': "B",  #Provincia de la dirección de facturación. MANDATORIO. Ver tabla anexa de provincias.		
'CSBTSTREET1' : "Cerrito 740", #Domicilio de facturación (calle y nro). MANDATORIO.		
'CSBTSTREET2' :"Piso 8", #Complemento del domicilio. (piso, departamento). NO MANDATORIO.		
'CSPTCURRENCY': "ARS",  #Moneda. MANDATORIO.		
'CSPTGRANDTOTALAMOUNT': "125.38", #Con decimales opcional usando el puntos como separador de decimales. No se permiten comas, ni como separador de miles ni como separador de decimales. MANDATORIO. (Ejemplos:$125,38-> 125.38 $12-> 12 o 12.00)
'CSMDD7':"56", # Fecha registro comprador(num Dias). NO MANDATORIO.		
'CSMDD8':"Y", #Usuario Guest? (Y/N). En caso de ser Y, el campo CSMDD9 no deberá enviarse. NO MANDATORIO.	
'CSMDD9':"asjhskajshiuyiquwyiqw", #Customer password Hash: criptograma asociado al password del comprador final. NO MANDATORIO.	
'CSMDD10':"5", #Histórica de compras del comprador (Num transacciones). NO MANDATORIO.		
'CSMDD11':"540111564893736"} #Customer Cell Phone. NO MANDATORIO.		
'CSSTCITY':"rosario",  #Ciudad de enví­o de la orden. MANDATORIO.		
'CSSTCOUNTRY':"AR", #País de envío de la orden. MANDATORIO.		
'CSSTEMAIL': "jose@gmail.com", #Mail del destinatario, MANDATORIO.		
'CSSTFIRSTNAME':"Jose", #Nombre del destinatario. MANDATORIO.		
'CSSTLASTNAME':"Perez", #Apellido del destinatario. MANDATORIO.		
'CSSTPHONENUMBER':"541155893737", #Número de teléfono del destinatario. MANDATORIO.		
'CSSTPOSTALCODE':"1414", #Código postal del domicilio de envío. MANDATORIO.		
'CSSTSTATE':"D", #Provincia de envío. MANDATORIO. Son de 1 caracter		
'CSSTSTREET1':"San Martín 123", #Domicilio de envío. MANDATORIO.		
'CSMDD12':"" #Shipping, DeadLine (Num Dias). NO MADATORIO.		
'CSMDD13':"", #Método de Despacho. NO MANDATORIO.		
'CSMDD14':"", #Customer requires Tax Bill ? (Y/N). NO MANDATORIO.		
'CSMDD15':"", #Customer Loyality Number. NO MANDATORIO. 		
'CSMDD16':"", #Promotional / Coupon Code. NO MANDATORIO. #Retail: datos a enviar por cada producto, los valores deben estar separado con #:		
'CSITPRODUCTCODE':"electronic_good", #Código de producto. CONDICIONAL. Valores posibles(adult_content;coupon;default;electronic_good;electronic_software;gift_certificate;handling_only;service;shipping_and_handling;shipping_only;subscription)		
'CSITPRODUCTDESCRIPTION':"NOTEBOOK L845 SP4304LA DF TOSHIBA", #Descripción del producto. CONDICIONAL.	
'CSITPRODUCTNAME':"NOTEBOOK L845 SP4304LA DF TOSHIBA", #Nombre del producto. CONDICIONAL.		
'CSITPRODUCTSKU':"LEVJNSL36GN", #Código identificador del producto. CONDICIONAL.		
'CSITTOTALAMOUNT':"1254.40", #CSITTOTALAMOUNT=CSITUNITPRICE*CSITQUANTITY "999999[.CC]" Con decimales opcional usando el puntos como separador de decimales. No se permiten comas, ni como separador de miles ni como separador de decimales. CONDICIONAL.		
'CSITQUANTITY':"1", #Cantidad del producto. CONDICIONAL.		
'CSITUNITPRICE': "1254.40" }#Formato Idem CSITTOTALAMOUNT. CONDICIONAL.		
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
print tpc.getStatus(optionsGS)
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
<tr><td>Entre Ríos</td><td>R</td></tr>		
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

[<sub>Volver a inicio</sub>](#inicio)
