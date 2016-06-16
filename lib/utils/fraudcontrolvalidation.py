import json
from utils.validations import Validation

class FraudControlValidation:
	def __init__(self, payload):
		self.validation = Validation.TODOPAGO_JSON_VALIDATION
		self.payload = payload
	
	def validate(self):

		for v in self.validation:
			if v.get("validate") != None:
				if not(self.payload.get(v.get("field"))):
					if v.get("validate")[0].get("default"):
						self.payload[v.get("field")] = v.get("validate")[0].get("default")
					elif v.get("validate")[0].get("message"):
						raise Exception(v.get("validate")[0].get("message"))

		return self.payload