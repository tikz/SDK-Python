# -*- coding: utf-8 -*-
class Validation:
    TODOPAGO_JSON_VALIDATION=[
	{
		"field" : "CSBTCITY",
		"validate":[
					{ "function":"notEmpty",
					  "message": "El campo CSBTCITY es requerido"	
					}
				],
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["49"]	
					}
				]		
	},
	{
		"field" : "CSBTCOUNTRY",		
		"format":[
					{ 	"function":"hardcode",
						"params":["AR"]	
					}
				]		
	},
	{
		"field" : "CSBTCUSTOMERID",
		"validate":[
					{ "function":"notEmpty",
					  "default" : "random"		
					}
				],
		"format":[  { "function":"clean" 
					},
					{ 	"function":"truncate",
						"params":["49"]	
					}					
				]	
	},
	{
		"field" : "CSBTEMAIL",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSBTEMAIL es requerido"		
					},

					{ "function":"regex",
					  "params" : ["[^A-Za-z0-9.@_-~#]+"],
					  "message" : "El campo CSBTEMAIL es invalido"		
					}
				],
		"format":[  { "function":"clean" 
					},
					{ 	"function":"truncate",
						"params":["99"]	
					}
					
				]		
	},
	{
		"field" : "CSBTIPADDRESS",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSBTIPADDRESS es requerido"		
					},
					{ "function":"regex",
					  "params":	["[/^(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/]"],
					  "message" : "El campo CSBTIPADDRESS es invalido"		
					}
				]
	},
	{
		"field" : "CSBTPOSTALCODE",
		"validate":[
					{ "function":"notEmpty",
					  "default" : "findState"		
					}
				],
		"format":[  { "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["9"]	
					}

				]		
	},

	{
		"field" : "CSBTSTATE",
		"validate":[
					{ "function":"notEmpty",
					  "default" : "C"		
					}
					
				],
		"format":[
					{ "function":"truncate",
					  "params":["1"]	
					},
					{ "function":"regex",	
					  "params": ["\w"],
					  "message":"El campo CSBTSTATE es invalido"
					},
					{ "function":"upper" 
					}
					
				]		
	},
	{
		"field" : "CSBTFIRSTNAME",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSBTFIRSTNAME es requerido"		
					}
				],
		"format":[  { "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["59"]	
					}					
				]		
	},
	{
		"field" : "CSBTLASTNAME",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSBTLASTNAME es requerido"		
					}
				],
		"format":[  { "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["59"]	
					}
					
				]		
	},
	{
		"field" : "CSBTPHONENUMBER",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSBTPHONENUMBER es requerido"		
					}
				],
		"format":[
					{ "function":"truncate",
					  "params":["14"]	
					},
					{ "function":"phone" 
					},
					{
						"function":"regex",
						"params": ["[0-9]"]
					}
				]		
	},
	{
		"field" : "CSBTSTREET1",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSBTSTREET1 es requerido"		
					}
				],
		"format":[  { "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["59"]	
					}
				]		
	},
	{
		"field" : "CSBTSTREET2",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSBTSTREET2 es requerido"		
					}
				],
		"format":[  { "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["59"]	
					}
					
				]		
	},
	{
		"field" : "CSPTCURRENCY",
		"format":[
					{ "function":"hardcode",
					  "params":["ARS"]	
					}
				]		
	},
	{
		"field" : "CSPTGRANDTOTALAMOUNT",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSPTGRANDTOTALAMOUNT es requerido"		
					}
				],
		"format":[
					{  "function":"regex",
					   "params": ["[([0-9]{12}).([0-9]{2})]"]
					}
				]		
	},
	{
		"field" : "CSMDD6",
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSMDD7",
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSMDD8",
		"validate":[
					{ "function":"notEmpty",
					  "default" : "N"		
					},
					{ "function":"regex",
					  "params":["[YySsNn]"],
					  "default" : "N"
					}

				 ],
		"format":[
					{
					  "function":"truncate",
					  "params":["1"]
					}
				]		
	},
	{
		"field" : "CSMDD9",
		"format":[
					{ "function":"clean" 
					},		
					{
					  "function":"truncate",
					  "params":["254"]
					}
				]		
	},
	{
		"field" : "CSMDD10",
		"format":[
					{ "function":"clean" 
					},		
					{
					  "function":"truncate",
					  "params":["254"]
					}
				]		
	},
	{
		"field" : "CSMDD11",
		"format":[
					{ "function":"clean" 
					},		
					{
					  "function":"truncate",
					  "params":["254"]
					}
				]		
	},
	{
		"field" : "CSMDD44",
		"format":[
					{ "function":"clean" 
					},		
					{
					  "function":"truncate",
					  "params":["254"]
					}
				]		
	},
	{
		"field" : "CSSTCITY",
		"validate":[
					{ "function":"notEmpty",
					  "message": "El campo CSSTCITY es requerido"	
					}
				],
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["49"]	
					}
				]		
	},
	{
		"field" : "CSSTCOUNTRY",
		
		"format":[
					{ 	"function":"hardcode",
						"params":["AR"]	
					}
				]		
	},
	{
		"field" : "CSSTEMAIL",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSSTEMAIL es requerido"		
					},

					{ "function":"regex",
					  "params" : ["[^A-Za-z0-9.@_-~#]+"],
					  "message" : "El campo CSSTEMAIL es invalido"		
					}
				],
		"format":[  { "function":"clean" 
					},
					{ 	"function":"truncate",
						"params":["99"]	
					}
					
				]	
	},
	{
		"field" : "CSSTFIRSTNAME",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSSTFIRSTNAME es requerido"		
					}
				],
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["59"]	
					}
				]		
	},
	{
		"field" : "CSSTLASTNAME",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSSTLASTNAME es requerido"		
					}
				],
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["59"]	
					}
				]		
	},
	{
		"field" : "CSSTPHONENUMBER",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSSTPHONENUMBER es requerido"		
					}
				],
		"format":[
					{ "function":"truncate",
					  "params":["14"]	
					},
					{ "function":"phone" 
					},
					{
						"function":"regex",
						"params": ["[0-9]"]
					}
				]		
	},
	{
		"field" : "CSSTPOSTALCODE",
		"validate":[
					{ "function":"notEmpty",
					  "default" : "findState"		
					}
				],
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["9"]	
					}
				]		
	},
	{
		"field" : "CSSTSTATE",
		"validate":[
					{ "function":"notEmpty",
					  "default" : "C"		
					}
					
				],
		"format":[
					{ "function":"truncate",
					  "params":["1"]	
					},
					{ "function":"regex",	
					  "params": ["\w"],
					  "message":"El campo CSSTSTATE es invalido"
					},
					{ "function":"upper" 
					}
					
				]
	},
	{
		"field" : "CSSTSTREET1",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSSTSTREET1 es requerido"		
					}
				],
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["59"]	
					}
				]		
	},
	{
		"field" : "CSSTSTREET2",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSSTSTREET2 es requerido"		
					}
				],
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["59"]	
					}
				]		
	},
	{
		"field" : "CSMDD12",
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSMDD13",
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSMDD14",
		"validate":[
					{ "function":"notEmpty",
					  "default" : "N"		
					},
					{ "function":"regex",
					  "params":["[YySsNn]"],
					  "default" : "N"
					}

				 ],
		"format":[
					{
					  "function":"truncate",
					  "params":["1"]
					}
				]		
	},
	{
		"field" : "CSMDD15",
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSMDD16",
		"format":[
					{ "function":"clean" 
					},
					{ "function":"truncate",
					  "params":["254"]	
					}
				]		
	},


	{
		"field" : "CSITPRODUCTCODE",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSITPRODUCTCODE es requerido"		
					}
		           ],	
		"format":[
					{ "function":"csitFormat",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSITPRODUCTDESCRIPTION",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSITPRODUCTDESCRIPTION es requerido"		
					}
		           ],	
		"format":[
					{ "function":"csitFormat",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSITPRODUCTNAME",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSITPRODUCTNAME es requerido"		
					}
		           ],	
		"format":[
					{ "function":"csitFormat",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSITPRODUCTSKU",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSITPRODUCTSKU es requerido"		
					}
		           ],	
		"format":[
					{ "function":"csitFormat",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSITTOTALAMOUNT",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSITTOTALAMOUNT es requerido"		
					}
		           ],	
		"format":[
					{ "function":"csitFormat",
					  "params":["254"]	
					}
				]		
	},
		{
		"field" : "CSITUNITPRICE",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSITUNITPRICE es requerido"		
					}
		           ],	
		"format":[
					{ "function":"csitFormat",
					  "params":["254"]	
					}
				]		
	},
	{
		"field" : "CSITQUANTITY",
		"validate":[
					{ "function":"notEmpty",
					  "message" : "El campo CSITQUANTITY es requerido"		
					}
		           ],	
		"format":[
					{ "function":"csitFormat",
					  "params":["254"]	
					}
				]		
	}



]
