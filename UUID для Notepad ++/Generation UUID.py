import uuid

def add_1(m):
    return '>urn:uuid:' + str(uuid.uuid4()) + '</wsa:MessageID>'
	
def add_2(m):
    return '>urn:uuid:' + str(uuid.uuid4()) + '</int:ConversationID>'
	
def add_3(m):
    return '>urn:uuid:' + str(uuid.uuid4()) + '</int:ProcedureID>'
	
def add(m):
    return '\n]}'

def add_5(m):
    return '<csdo:EDocDateTime>2019-07-15T18:02:28.904Z</csdo:EDocDateTime>'
	
	
editor.rereplace(">urn:uuid:.*</wsa:MessageID>", add_1)
editor.rereplace(">urn:uuid:.*</int:ConversationID>", add_2)
editor.rereplace(">urn:uuid:.*</int:ProcedureID>", add_3)
editor.rereplace(">.*</csdo:EDocId>", add_4)
editor.rereplace("<csdo:EDocDateTime>.*</csdo:EDocDateTime>", add_5)

#Zamena vseh UUID aktivnogo dokumenta na odin i tot ge
#editor.rereplace("\S{8}-\S{4}-\S{4}-\S{4}-\S{12}", str(uuid.uuid4()))

def add(m):
    return '\n]\n}'
editor.rereplace(",\n]\n}", add)