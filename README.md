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
######[Credenciales](#obtenercredenciales)
######[Formulario hidrido](#formhidrido)
######[Tablas de referencia](#tablas)
######[Tabla de errores](#codigoerrores)
 		
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

<a name="devoluciones"></a>
## Devoluciones y Devolucion parcial

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

<a name="obtenercredenciales"></a>
## Credenciales
El SDK permite obtener las credenciales "Authentification", "MerchandId" y "Security" de la cuenta de Todo Pago, ingresando el usuario y contraseña.<br>
Esta funcionalidad es util para obtener los parametros de configuracion dentro de la implementacion.

- Crear una instancia de la clase User:
```python

j_header_http = {
	'Authorization':''
}

tpc = TodoPagoConnector(j_header_http, "test")

#usario de TodoPago
$datosUsuario = array(
	'USUARIO' : "usuario@todopago.com.ar", 
	'CLAVE' : "contraseña"
);

#este metodo devuelve un json con las credenciales
tpc.getCredentials(userCredenciales);

```
**Observación**: El Security se obtiene a partir de apiKey, eliminando TODOPAGO de este ultimo.

<a name="formhidrido"></a>
####Formulario hibrido

**Conceptos basicos**<br>
El formulario hibrido, es una alternativa al medio de pago actual por redirección al formulario externo de TodoPago.<br> 
Con el mismo, se busca que el comercio pueda adecuar el look and feel del formulario a su propio diseño.

**Libreria**<br>
El formulario requiere incluir en la pagina una libreria Javascript de TodoPago.<br>
El endpoint depende del entorno:
+ Desarrollo: https://developers.todopago.com.ar/resources/TPHybridForm-v0.1.js
+ Produccion: https://forms.todopago.com.ar/resources/TPHybridForm-v0.1.js

**Restricciones y libertades en la implementación**

+ Ninguno de los campos del formulario podrá contar con el atributo name.
+ Se deberá proveer de manera obligatoria un botón para gestionar el pago con Billetera Todo Pago.
+ Todos los elementos de tipo <option> son completados por la API de Todo Pago.
+ Los campos tienen un id por defecto. Si se prefiere utilizar otros ids se deberán especificar los
mismos cuando se inicialice el script de Todo Pago.
+ Pueden aplicarse todos los detalles visuales que se crean necesarios, la API de Todo Pago no
altera los atributos class y style.
+ Puede utilizarse la API para setear los atributos placeholder del formulario, para ello deberá
especificar dichos placeholders en la inicialización del formulario "window.TPFORMAPI.hybridForm.setItem". En caso de que no se especifiquen los placeholders se usarán los valores por defecto de la API.

**HTML del formulario**

El formulario implementado debe contar al menos con los siguientes campos.

```html
<body>
	<select id="formaDePagoCbx"></select>
	<select id="bancoCbx"></select>
	<select id="promosCbx"></select>
	<label id="labelPromotionTextId"></label>
	<input id="numeroTarjetaTxt"/>
	<input id="mesTxt"/>
	<input id="anioTxt"/>
	<input id="codigoSeguridadTxt"/>
	<label id="labelCodSegTextId"></label>
	<input id="apynTxt"/>
	<select id="tipoDocCbx"></select>
	<input id="nroDocTxt"/>
	<input id="emailTxt"/><br/>
	<button id="MY_btnConfirmarPago"/>
</body>
```

**Inizialización y parametros requeridos**<br>
Para inicializar el formulario se usa window.TPFORMAPI.hybridForm.initForm. El cual permite setear los elementos y ids requeridos.

Para inicializar un ítem de pago, es necesario llamar a window.TPFORMAPI.hybridForm.setItem. Este requiere obligatoriamente el parametro publicKey que corresponde al PublicRequestKey (entregado por el SAR).
Se sugiere agregar los parametros usuario, e-mail, tipo de documento y numero.

**Javascript**
```js
window.TPFORMAPI.hybridForm.initForm({
    callbackValidationErrorFunction: 'validationCollector',
	callbackCustomSuccessFunction: 'customPaymentSuccessResponse',
	callbackCustomErrorFunction: 'customPaymentErrorResponse',
	botonPagarId: 'MY_btnConfirmarPago',
	modalCssClass: 'modal-class',
	modalContentCssClass: 'modal-content',
	beforeRequest: 'initLoading',
	afterRequest: 'stopLoading'
});

window.TPFORMAPI.hybridForm.setItem({
    publicKey: 'taf08222e-7b32-63d4-d0a6-5cabedrb5782', //obligatorio
    defaultNombreApellido: 'Usuario',
    defaultNumeroDoc: 20234211,
    defaultMail: 'todopago@mail.com',
    defaultTipoDoc: 'DNI'
});

//callbacks de respuesta del pago
function validationCollector(parametros) {
}
function customPaymentSuccessResponse(response) {
}
function customPaymentErrorResponse(response) {
}
function initLoading() {
}
function stopLoading() {
}
```

**Callbacks**<br>
El formulario define callbacks javascript, que son llamados según el estado y la informacion del pago realizado:
+ customPaymentSuccessResponse: Devuelve response si el pago se realizo correctamente.
+ customPaymentErrorResponse: Si hubo algun error durante el proceso de pago, este devuelve el response con el codigo y mensaje correspondiente.

**Ejemplo de Implementación**:
<a href="/Ejemplo/form_hibrido-ejemplo/index.html" target="_blank">Formulario hibrido</a>
<br>
		
<a name="p"></a>		
##Provincias

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

<a name="codigoerrores"></a>    
## Tabla de errores 

<table>		
<tr><th>Id mensaje</th><th>Mensaje</th></tr>				
<tr><td>-1</td><td>Aprobada.</td></tr>
<tr><td>1081</td><td>Tu saldo es insuficiente para realizar la transacción.</td></tr>
<tr><td>1100</td><td>El monto ingresado es menor al mínimo permitido</td></tr>
<tr><td>1101</td><td>El monto ingresado supera el máximo permitido.</td></tr>
<tr><td>1102</td><td>La tarjeta ingresada no corresponde al Banco indicado. Revisalo.</td></tr>
<tr><td>1104</td><td>El precio ingresado supera al máximo permitido.</td></tr>
<tr><td>1105</td><td>El precio ingresado es menor al mínimo permitido.</td></tr>
<tr><td>2010</td><td>En este momento la operación no pudo ser realizada. Por favor intentá más tarde. Volver a Resumen.</td></tr>
<tr><td>2031</td><td>En este momento la validación no pudo ser realizada, por favor intentá más tarde.</td></tr>
<tr><td>2050</td><td>Lo sentimos, el botón de pago ya no está disponible. Comunicate con tu vendedor.</td></tr>
<tr><td>2051</td><td>La operación no pudo ser procesada. Por favor, comunicate con tu vendedor.</td></tr>
<tr><td>2052</td><td>La operación no pudo ser procesada. Por favor, comunicate con tu vendedor.</td></tr>
<tr><td>2053</td><td>La operación no pudo ser procesada. Por favor, intentá más tarde. Si el problema persiste comunicate con tu vendedor</td></tr>
<tr><td>2054</td><td>Lo sentimos, el producto que querés comprar se encuentra agotado por el momento. Por favor contactate con tu vendedor.</td></tr>
<tr><td>2056</td><td>La operación no pudo ser procesada. Por favor intentá más tarde.</td></tr>
<tr><td>2057</td><td>La operación no pudo ser procesada. Por favor intentá más tarde.</td></tr>
<tr><td>2059</td><td>La operación no pudo ser procesada. Por favor intentá más tarde.</td></tr>
<tr><td>90000</td><td>La cuenta destino de los fondos es inválida. Verificá la información ingresada en Mi Perfil.</td></tr>
<tr><td>90001</td><td>La cuenta ingresada no pertenece al CUIT/ CUIL registrado.</td></tr>
<tr><td>90002</td><td>No pudimos validar tu CUIT/CUIL.  Comunicate con nosotros <a href="#contacto" target="_blank">acá</a> para más información.</td></tr>
<tr><td>99900</td><td>El pago fue realizado exitosamente</td></tr>
<tr><td>99901</td><td>No hemos encontrado tarjetas vinculadas a tu Billetera. Podés  adherir medios de pago desde www.todopago.com.ar</td></tr>
<tr><td>99902</td><td>No se encontro el medio de pago seleccionado</td></tr>
<tr><td>99903</td><td>Lo sentimos, hubo un error al procesar la operación. Por favor reintentá más tarde.</td></tr>
<tr><td>99970</td><td>Lo sentimos, no pudimos procesar la operación. Por favor reintentá más tarde.</td></tr>
<tr><td>99971</td><td>Lo sentimos, no pudimos procesar la operación. Por favor reintentá más tarde.</td></tr>
<tr><td>99977</td><td>Lo sentimos, no pudimos procesar la operación. Por favor reintentá más tarde.</td></tr>
<tr><td>99978</td><td>Lo sentimos, no pudimos procesar la operación. Por favor reintentá más tarde.</td></tr>
<tr><td>99979</td><td>Lo sentimos, el pago no pudo ser procesado.</td></tr>
<tr><td>99980</td><td>Ya realizaste un pago en este sitio por el mismo importe. Si querés realizarlo nuevamente esperá 5 minutos.</td></tr>
<tr><td>99982</td><td>En este momento la operación no puede ser realizada. Por favor intentá más tarde.</td></tr>
<tr><td>99983</td><td>Lo sentimos, el medio de pago no permite la cantidad de cuotas ingresadas. Por favor intentá más tarde.</td></tr>
<tr><td>99984</td><td>Lo sentimos, el medio de pago seleccionado no opera en cuotas.</td></tr>
<tr><td>99985</td><td>Lo sentimos, el pago no pudo ser procesado.</td></tr>
<tr><td>99986</td><td>Lo sentimos, en este momento la operación no puede ser realizada. Por favor intentá más tarde.</td></tr>
<tr><td>99987</td><td>Lo sentimos, en este momento la operación no puede ser realizada. Por favor intentá más tarde.</td></tr>
<tr><td>99988</td><td>Lo sentimos, momentaneamente el medio de pago no se encuentra disponible. Por favor intentá más tarde.</td></tr>
<tr><td>99989</td><td>La tarjeta ingresada no está habilitada. Comunicate con la entidad emisora de la tarjeta para verificar el incoveniente.</td></tr>
<tr><td>99990</td><td>La tarjeta ingresada está vencida. Por favor seleccioná otra tarjeta o actualizá los datos.</td></tr>
<tr><td>99991</td><td>Los datos informados son incorrectos. Por favor ingresalos nuevamente.</td></tr>
<tr><td>99992</td><td>La fecha de vencimiento es incorrecta. Por favor seleccioná otro medio de pago o actualizá los datos.</td></tr>
<tr><td>99993</td><td>La tarjeta ingresada no está vigente. Por favor seleccioná otra tarjeta o actualizá los datos.</td></tr>
<tr><td>99994</td><td>El saldo de tu tarjeta no te permite realizar esta operacion.</td></tr>
<tr><td>99995</td><td>La tarjeta ingresada es invalida. Seleccioná otra tarjeta para realizar el pago.</td></tr>
<tr><td>99996</td><td>La operación fué rechazada por el medio de pago porque el monto ingresado es inválido.</td></tr>
<tr><td>99997</td><td>Lo sentimos, en este momento la operación no puede ser realizada. Por favor intentá más tarde.</td></tr>
<tr><td>99998</td><td>Lo sentimos, la operación fue rechazada. Comunicate con la entidad emisora de la tarjeta para verificar el incoveniente o seleccioná otro medio de pago.</td></tr>
<tr><td>99999</td><td>Lo sentimos, la operación no pudo completarse. Comunicate con la entidad emisora de la tarjeta para verificar el incoveniente o seleccioná otro medio de pago.</td></tr>
</table>

[<sub>Volver a inicio</sub>](#inicio)
