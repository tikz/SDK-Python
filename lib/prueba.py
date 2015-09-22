from todopagoconnector import TodoPagoConnector

optionsSAR_comercio = {
"Session": "ABCDEF-1234-12221-FDE1-00000200",
"Security": "1234567890ABCDEF1234567890ABCDEF",
"EncodingMethod": "XML",
"URL_OK": "http,//someurl.com/ok/",
"URL_ERROR": "http,//someurl.com/fail/",
"EMAILCLIENTE": "email_cliente@dominio.com"
}

optionsSAR_operacion = {
"MERCHANT": "2153",
"OPERATIONID": "06",
"CURRENCYCODE": "032",
"AMOUNT": "54",

"CSBTCITY": "Villa General Belgrano", 
"CSSTCITY": "Villa General Belgrano", 

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

optionsGAA = {
'Security': '1234567890ABCDEF1234567890ABCDEF',
'Merchant': "2153",
'RequestKey': '0725b17e-3a0b-42f8-8b27-efb98b9e0b42',
'AnswerKey': 'edb48330-29de-2544-f490-6db4b7d11abc'
}

optionsGAPM = {
'MERCHANT': '2153'
}
optionsGS = {
'MERCHANT': '2153',
'OPERATIONID': '02'
}

j_header_http = {
'Authorization':'PRISMA f3d8b72c94ab4a06be2ef7c95490f7d3'
}

j_wsdls = {
'Operations': 'https://developers.todopago.com.ar/services/t/1.1/Operations?wsdl',
'Authorize': 'https://developers.todopago.com.ar/services/t/1.1/Authorize?wsdl'
}




tpc = TodoPagoConnector(j_header_http, j_wsdls, 'https://developers.todopago.com.ar/')
#TODO add fraud control to SendAuthorizeRequest
print tpc.sendAuthorizeRequest(optionsSAR_comercio, optionsSAR_operacion)
print "\n\r ------------------------------------ "
print tpc.getAuthorizeAnswer(optionsGAA)
print "\n\r ------------------------------------ "
print tpc.getStatus(optionsGS)
print "\n\r ------------------------------------ "
# print tpc.getAllPaymentMethods(optionsGAPM)
# print "\n\r ------------------------------------ "