# -*- coding: utf-8 -*-
from todopagoconnector import TodoPagoConnector
import os.path, sys, urllib, urlparse, warnings
from utils.fraudcontrolvalidation import FraudControlValidation
import json


warnings.simplefilter('always')

optionsSAR_comercio = {
"Security": "15406018567890AB40E46ABD10E",
"EncodingMethod": "XML",
"URL_OK": "http,//someurl.com/ok/",
"URL_ERROR": "http,//someurl.com/fail/",
"EMAILCLIENTE": "email_cliente@dominio.com"
}

optionsSAR_operacion = {
"MERCHANT": "2866",
"OPERATIONID": "06",
"CURRENCYCODE": "032",
"AMOUNT": "54",

"CSBTCITY": "Villa General Belgrano",
"CSSTCITY": "Villa General Belgrano",
"CSMDD6" : "",
"CSBTCOUNTRY": "AR",
"CSSTCOUNTRY": "AR",

"CSBTEMAIL": "todopago@hotmail.com",
"CSSTEMAIL": "todopago@hotmail.com",

"CSBTFIRSTNAME": "Juan",
"CSSTFIRSTNAME": "Juan",

"CSBTLASTNAME": "Perez",
"CSSTLASTNAME": "Perez",

"CSBTPHONENUMBER": "541160913988",
"CSSTPHONENUMBER": "541160913988",

"CSBTPOSTALCODE": "1010",
"CSSTPOSTALCODE": "1010",

"CSBTSTATE": "B",
"CSSTSTATE": "B",

"CSBTSTREET1": "Cerrito 740",
"CSSTSTREET1": "Cerrito 740",


"CSBTSTREET2": "Cerrito 740",
"CSSTSTREET2": "Cerrito 740",

"CSBTCUSTOMERID": "453458",
"CSBTIPADDRESS": "192.0.0.4",
"CSPTCURRENCY": "ARS",
"CSPTGRANDTOTALAMOUNT": "125.38",
"CSMDD7": "",
"CSMDD8": "Y",
"CSMDD9": "",
"CSMDD10": "",
"CSMDD11": "",
"STCITY": "rosario",
"STCOUNTRY": "",
"STEMAIL": "jose@gmail.com",
"STFIRSTNAME": "Jose",
"STLASTNAME": "Perez",
"STPHONENUMBER": "541155893737",
"STPOSTALCODE": "1414",
"STSTATE": "D",
"STSTREET1": "San Martin 123",
"CSMDD12": "",
"CSMDD13": "",
"CSMDD14": "",
"CSMDD15": "",
"CSMDD16": "",
"CSITPRODUCTCODE": "electronic_good",
"CSITPRODUCTDESCRIPTION": "NOTEBOOK L845 SP4304LA DF TOSHIBA",
"CSITPRODUCTNAME": "NOTEBOOK L845 SP4304LA DF TOSHIBA",
"CSITPRODUCTSKU": "LEVJNSL36GN",
"CSITTOTALAMOUNT": "1254.40",
"CSITQUANTITY": "1",
"CSITUNITPRICE": "1254.40"
}



j_header_http = {
'Authorization':'TODOPAGO 1540601877EB2059EF50240E46ABD10E'
}

j_wsdls = {
'Operations': 'Operations',
'Authorize': 'Authorize'
}


tpc = TodoPagoConnector(j_header_http, "test")

result = tpc.sendAuthorize(optionsSAR_comercio, optionsSAR_operacion)

encoding = sys.stdout.encoding
if (encoding is None):
	encoding = "cp850"
for k, val in result.iteritems():
	if (isinstance(val, int)):
		strval = str(val)
		print(k + " : " + strval.encode(encoding))
	else:
		print(k + " : " + val.encode(encoding))
