# -*- coding: utf-8 -*-

from bottle import Bottle, run, route, install, template, static_file, response, request
import sqlite3, datetime, json, os, sys, urllib, warnings, sys, string
from random import randint
#reload(sys)
#sys.setdefaultencoding('utf8')

# Librería TodoPago
sys.path = ['../lib'] + sys.path
print(sys.path)
from todopagoconnector import TodoPagoConnector


app = Bottle()
@app.route('/login_form')
def login_form():
	output = template('login_form')
	return output

@app.route('/login_action', method='POST')
def login_action():
	j_header_http = {
		#'Authorization':''
	}

	datosUsuario = {
		'USUARIO' : request.POST.user.strip(), 
		'CLAVE' : request.POST.pwd.strip()	
	}

	tpc = TodoPagoConnector(j_header_http,  str(request.POST.mode.strip()))
	result = tpc.getCredentials(datosUsuario)
	print(result)

	
	arrSecurity=str(result["Credentials"]["APIKey"]).split(' ')

	if result["Credentials"]["resultado"]["codigoResultado"]==0:
		response.set_header('Set-Cookie', 'merchandid='+str(result["Credentials"]["merchantId"]))
		response.add_header('Set-Cookie', 'security='+arrSecurity[1])
		response.add_header('Set-Cookie', 'mode='+str(request.POST.mode.strip()))
		return("<p><strong>getCredentials</strong> correcto.<div></div><a href='/list'>Continuar</a></p>")
	else:
		return("<p>Error en el login.</p><p>mensajeResultado: </p><pre>"+str(result["Credentials"]["resultado"]["mensajeResultado"])+"</pre>")
	

@app.route('/list')
def list():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()
	c.execute('CREATE TABLE if not exists operacion ( id integer PRIMARY KEY, data text, operationid varchar(255), merchantId INT NOT NULL, security varchar(255), authorizationhttp varchar(255), status varchar(255), params_SAR text, response_SAR text, second_step TINYINT, params_GAA text, response_GAA text, request_key varchar(255), public_request_key varchar(255), answer_key varchar(255), url_request varchar(255), mode varchar(255), sar text, pago tinyint, gaa text, refound tinyint )')

	c.execute("SELECT id, status, operationid FROM operacion")
	result = c.fetchall()
	c.close()

	output = template('make_table', rows=result)
	return output

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

@app.route('/new')    
def new():
	output = template('new', merchandid=request.get_cookie('merchandid'),
		apikey=request.get_cookie('apikey'),
		security=request.get_cookie('security'),
		mode=request.get_cookie('mode'),
		operation='sdk_php'+str(randint(1,1000000)))
	return output

@app.route('/new_action', method='POST')    
def new_action():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()

	data_operacion={
		'MERCHANT': request.POST.merchant.strip(),
		'OPERATIONID':  request.POST.operacion.strip(),
		'CURRENCYCODE':  32,
		'AMOUNT': request.POST.amount.strip(),
		'MININSTALLMENTS': request.POST.MININSTALLMENTS.strip(),
		'MAXINSTALLMENTS': request.POST.MAXINSTALLMENTS.strip(),
		'EMAILCLIENTE': request.POST.email.strip(),   
		'CSBTCITY': request.POST.CSBTCITY.strip(),   
		'CSBTCOUNTRY': request.POST.CSBTCOUNTRY.strip(),
		'CSBTCUSTOMERID': request.POST.CSBTCUSTOMERID.strip(),
		'CSBTIPADDRESS': request.POST.CSBTIPADDRESS.strip(),
		'CSBTEMAIL': request.POST.CSBTEMAIL.strip(),
		'CSBTFIRSTNAME': request.POST.CSBTFIRSTNAME.strip(),
		'CSBTLASTNAME': request.POST.CSBTLASTNAME.strip(),
		'CSBTPHONENUMBER': request.POST.CSBTPHONENUMBER.strip(),    
		'CSBTPOSTALCODE': request.POST.CSBTPOSTALCODE.strip(),
		'CSBTSTATE': request.POST.CSBTSTATE.strip(),
		'CSBTSTREET1': request.POST.CSBTSTREET1.strip(),
		'CSBTSTREET2': request.POST.CSBTSTREET2.strip(),
		'CSPTCURRENCY': request.POST.CSPTCURRENCY.strip(),
		'CSPTGRANDTOTALAMOUNT': request.POST.CSPTGRANDTOTALAMOUNT.strip(),
		'CSMDD7': request.POST.CSMDD7.strip(),
		'CSMDD8': request.POST.CSMDD8.strip(),
		'CSMDD9': request.POST.CSMDD9.strip(),
		'CSMDD10': request.POST.CSMDD10.strip(),
		'CSMDD11': request.POST.CSMDD11.strip(),
		'CSSTCITY': request.POST.CSSTCITY.strip(), 
		'CSSTCOUNTRY': request.POST.CSSTCOUNTRY.strip(),
		'CSSTEMAIL': request.POST.CSSTEMAIL.strip(),
		'CSSTFIRSTNAME': request.POST.CSSTFIRSTNAME.strip(),
		'CSSTLASTNAME': request.POST.CSSTLASTNAME.strip(),
		'CSSTPHONENUMBER': request.POST.CSSTPHONENUMBER.strip(),
		'CSSTPOSTALCODE': request.POST.CSSTPOSTALCODE.strip(),
		'CSSTSTATE': request.POST.CSSTSTATE.strip(),
		'CSSTSTREET1': request.POST.CSSTSTREET1.strip(),
		'CSMDD12': request.POST.CSMDD12.strip(),
		'CSMDD13': request.POST.CSMDD13.strip(),
		'CSMDD14': request.POST.CSMDD14.strip(),
		'CSMDD15': request.POST.CSMDD15.strip(),
		'CSMDD16': request.POST.CSMDD16.strip(),
		'CSITPRODUCTCODE': request.POST.CSITPRODUCTCODE.strip(),
		'CSITPRODUCTDESCRIPTION': request.POST.CSITPRODUCTDESCRIPTION.strip(),
		'CSITPRODUCTNAME': request.POST.CSITPRODUCTNAME.strip(),
		'CSITPRODUCTSKU': request.POST.CSITPRODUCTSKU.strip(),
		'CSITTOTALAMOUNT': request.POST.CSITTOTALAMOUNT.strip(),
		'CSITQUANTITY': request.POST.CSITQUANTITY.strip(),
		'CSITUNITPRICE': request.POST.CSITUNITPRICE.strip(),
		'URL_OK': request.POST.URL_OK.strip(),
		'URL_ERROR': request.POST.URL_ERROR.strip(),
	}

	c.execute("INSERT INTO operacion (merchantid, security, authorizationhttp, status, params_SAR, response_SAR, second_step, params_GAA, response_GAA, request_key, public_request_key, answer_key, url_request, mode, sar, pago, gaa, refound, data, operationid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",   (request.POST.merchant.strip(), request.POST.security.strip(), request.POST.authorizationhttp.strip(), 'Pendiente', '0', '0', '0', '0', '0', '0', '0', '0', '0', request.get_cookie('mode'), '0', '0', '0', '0', json.dumps( data_operacion ), request.POST.operacion.strip(),))
	conn.commit()
	c.close()
	return '<a href="/list">Continuar</a>';

@app.route('/sar')    
def sar():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()
	c.execute("SELECT data, security, mode, id FROM operacion where id = ?", (request.GET.id.strip(),))
	result = c.fetchone()
	c.close()

	operacion = json.loads(result[0])

	optionsSAR_comercio = {
	"Security": str(result[1]),
	"EncodingMethod": "XML",
	"URL_OK": str(operacion["URL_OK"]),
	"URL_ERROR": str(operacion["URL_ERROR"]),	
	"EMAILCLIENTE": str(operacion["EMAILCLIENTE"])
	}
	print(optionsSAR_comercio)


	optionsSAR_operacion = {
	"MERCHANT": str(operacion["MERCHANT"]),
	"OPERATIONID": str(operacion["OPERATIONID"]),
	"CURRENCYCODE": str(operacion["CURRENCYCODE"]),
	"AMOUNT": str(operacion["AMOUNT"]),
	"MININSTALLMENTS": str(operacion["MININSTALLMENTS"]),
	"MAXINSTALLMENTS": str(operacion["MAXINSTALLMENTS"]),
	"CSBTCITY": str(operacion["CSBTCITY"]),
	"CSSTCITY": str(operacion["CSSTCITY"]),
	"CSMDD6" : "",
	"CSBTCOUNTRY": str(operacion["CSBTCOUNTRY"]),
	"CSSTCOUNTRY": str(operacion["CSSTCOUNTRY"]),

	"CSBTEMAIL": str(operacion["CSBTEMAIL"]),
	"CSSTEMAIL": str(operacion["CSSTEMAIL"]),

	"CSBTFIRSTNAME": str(operacion["CSBTFIRSTNAME"]),
	"CSSTFIRSTNAME": str(operacion["CSSTFIRSTNAME"]),

	"CSBTLASTNAME": str(operacion["CSBTLASTNAME"]),
	"CSSTLASTNAME": str(operacion["CSSTLASTNAME"]),

	"CSBTPHONENUMBER": str(operacion["CSBTPHONENUMBER"]),
	"CSSTPHONENUMBER": str(operacion["CSSTPHONENUMBER"]),

	"CSBTPOSTALCODE": str(operacion["CSBTPOSTALCODE"]),
	"CSSTPOSTALCODE": str(operacion["CSSTPOSTALCODE"]),

	"CSBTSTATE": str(operacion["CSBTSTATE"]),
	"CSSTSTATE": str(operacion["CSSTSTATE"]),

	"CSBTSTREET1": str(operacion["CSBTSTREET1"]),
	"CSSTSTREET1": str(operacion["CSSTSTREET1"]),


	"CSBTSTREET2": str(operacion["CSBTSTREET2"]),
	"CSSTSTREET2": str(operacion["CSBTSTREET2"]),

	"CSBTCUSTOMERID": str(operacion["CSBTCUSTOMERID"]),
	"CSBTIPADDRESS": str(operacion["CSBTIPADDRESS"]),
	"CSPTCURRENCY": str(operacion["CSPTCURRENCY"]),
	"CSPTGRANDTOTALAMOUNT": str(operacion["CSPTGRANDTOTALAMOUNT"]),
	"CSMDD7": str(operacion["CSMDD7"]),
	"CSMDD8": str(operacion["CSMDD8"]),
	"CSMDD9": str(operacion["CSMDD9"]),
	"CSMDD10": str(operacion["CSMDD10"]),
	"CSMDD11": str(operacion["CSMDD11"]),
	"STCITY": str(operacion["CSSTCITY"]),
	"STCOUNTRY": str(operacion["CSSTCOUNTRY"]),
	"STEMAIL": str(operacion["CSSTEMAIL"]),
	"STFIRSTNAME": str(operacion["CSSTFIRSTNAME"]),
	"STLASTNAME": str(operacion["CSSTLASTNAME"]),
	"STPHONENUMBER": str(operacion["CSSTPHONENUMBER"]),
	"STPOSTALCODE": str(operacion["CSSTPOSTALCODE"]),
	"STSTATE": str(operacion["CSSTSTATE"]),
	"STSTREET1": str(operacion["CSSTSTREET1"]),
	"CSMDD12": str(operacion["CSMDD12"]),
	"CSMDD13": str(operacion["CSMDD13"]),
	"CSMDD14": str(operacion["CSMDD14"]),
	"CSMDD15": str(operacion["CSMDD15"]),
	"CSMDD16": str(operacion["CSMDD16"]),
	"CSITPRODUCTCODE": str(operacion["CSITPRODUCTCODE"]),
	"CSITPRODUCTDESCRIPTION": str(operacion["CSITPRODUCTDESCRIPTION"]),
	"CSITPRODUCTNAME": str(operacion["CSITPRODUCTNAME"]),
	"CSITPRODUCTSKU": str(operacion["CSITPRODUCTSKU"]),
	"CSITTOTALAMOUNT": str(operacion["CSITTOTALAMOUNT"]),
	"CSITQUANTITY": str(operacion["CSITQUANTITY"]),
	"CSITUNITPRICE": str(operacion["CSITUNITPRICE"])
	}

	j_header_http = {
	'Authorization':'TODOPAGO '+result[1]
	}

	j_wsdls = {
	'Operations': 'Operations',
	'Authorize': 'Authorize'
	}


	tpc = TodoPagoConnector(j_header_http, result[2])

	result = tpc.sendAuthorize(optionsSAR_comercio, optionsSAR_operacion)

	#encoding = sys.stdout.encoding
	#if (encoding is None):
	#	encoding = "cp850"
	#for k, val in result.iteritems():
	#	if (isinstance(val, int)):
	#		strval = str(val)
	#		print(k + " : " + strval.encode(encoding))
	#	else:
	#		print(k + " : " + val.encode(encoding))
	
	#Guarda respuesta
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()	
	c.execute("UPDATE operacion SET response_SAR=?, request_key=?, url_request=?, public_request_key=?, status='Sar correcto' WHERE id=?", (json.dumps(optionsSAR_operacion), result['RequestKey'], result['URL_Request'], result['PublicRequestKey'], request.GET.id.strip()))
	conn.commit()
	c.close()

	output = template('sar', statusCode=result['StatusCode'], result=result)
	return output




@app.route('/gaa')    
def gaa():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()
	c.execute("SELECT data, security, mode, id, request_key, answer_key FROM operacion where id = ?", (request.GET.id.strip(),))
	result = c.fetchone()

	operacion = json.loads(result[0])

	j_header_http = {
		'Authorization': 'TODOPAGO '+str(result[1])
	}

	j_wsdls = {
		'Operations': 'Operations',
		'Authorize': 'Authorize'
	}

	optionsGAA = {
		'Security': str(result[1]),
		'Merchant': str(operacion["MERCHANT"]),
		'RequestKey': str(result[4]),
		'AnswerKey': str(result[5])
	}
	print(optionsGAA)

	tpc = TodoPagoConnector(j_header_http, result[2])
	result = tpc.getAuthorize(optionsGAA)

	c.execute("UPDATE operacion set status=? WHERE id=?", ('GAA correcto', request.GET.id.strip()))
	conn.commit()

	output = template('gaa', statusCode=result['StatusCode'], result=result)
	return output



@app.route('/getstatus')    
def getstatus():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()
	c.execute("SELECT data, security, mode, id, request_key, answer_key FROM operacion where id = ?", (request.GET.id.strip(),))
	result = c.fetchone()

	operacion = json.loads(result[0])

	j_header_http = {
		'Authorization': 'TODOPAGO '+str(result[1])
	}

	j_wsdls = {
		'Operations': 'Operations',
		'Authorize': 'Authorize'
	}
	
	optionsGS = {
		'MERCHANT': str(operacion["MERCHANT"]),
		'OPERATIONID': str(operacion["OPERATIONID"]),
	}


	tpc = TodoPagoConnector(j_header_http, result[2])
	result = tpc.getByOperationId(optionsGS)

	output = template('getstatus', result=result)
	return output



@app.route('/devolver', method='POST')    
def devolucion_total():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()
	c.execute("SELECT data, security, mode, id, request_key, answer_key FROM operacion where id = ?", (request.POST.id.strip(),))
	result = c.fetchone()

	operacion = json.loads(result[0])

	j_header_http = {
		'Authorization': 'TODOPAGO '+str(result[1])
	}

	j_wsdls = {
		'Operations': 'Operations',
		'Authorize': 'Authorize'
	}
	

	#Devolucion parcial
	if request.POST.parcial.strip():
		tipoDevolucion='Parcial'
		optionsVoid = {
		    "Security": str(result[1]),
		    "Merchant": str(operacion["MERCHANT"]),
		    "RequestKey": str(result[4]),
		    "Amount": str(request.POST.amount.strip())
		}

		tpc = TodoPagoConnector(j_header_http, result[2])
		result = tpc.returnRequest(optionsVoid)

	#Devolucion total
	else:
		tipoDevolucion='total'
		optionsVoid = {
		    "Security": str(result[1]),
		    "Merchant": str(operacion["MERCHANT"]),
		    "RequestKey": str(result[4])
		}
		tpc = TodoPagoConnector(j_header_http, result[2])
		result = tpc.voidRequest(optionsVoid)
	
	output = template('devolver', statusCode=result['StatusCode'], tipoDevolucion=tipoDevolucion, result=result)
	return output		



@app.route('/devolucion_form')    
def devolucion_form():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()
	c.execute("SELECT data FROM operacion where id = ?", (request.GET.id.strip(),))
	result = c.fetchone()
	c.close()

	dataOperation = json.loads(result[0])

	output = template('devolucion_form', id=request.GET.id.strip(), amount=dataOperation["AMOUNT"])
	return output


@app.route('/pagar')    
def pagar():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()
	c.execute("SELECT url_request FROM operacion where id = ?", (request.GET.id.strip(),))
	result = c.fetchone()
	c.close()

	return('<a href="'+result[0]+'">Pagar</a>')

@app.route('/mostrar_ok')    
def mostrar_ok():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()
	c.execute("UPDATE operacion set status=?, answer_key=? WHERE operationid=?", ('Pago correcto', request.GET.Answer.strip(), request.GET.id.strip()))
	print(request.GET.Answer.strip())


	conn.commit()

	output = template('mostrar_msg_pago.tpl', status=-1)
	return output


@app.route('/mostrar_error')    
def mostrar_error():
	conn = sqlite3.connect('operaciones.db')
	c = conn.cursor()
	c.execute("UPDATE operacion set status=?, answer_key=? WHERE id=?", ('Pago erroneo', request.GET.Answer.strip(), request.GET.id.strip()))
	conn.commit()

	output = template('mostrar_msg_pago.tpl', status=0)
	return output


run(app, host='localhost', port=8080)