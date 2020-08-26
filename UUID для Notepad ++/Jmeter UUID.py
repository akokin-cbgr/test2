import uuid

def add_1(m):
    return '>urn:uuid:${__UUID}</wsa:MessageID>'
	
def add_2(m):
    return '>urn:uuid:${__UUID}</int:ConversationID>'
	
def add_3(m):
    return '>urn:uuid:${__UUID}</int:ProcedureID>'
	
def add_4(m):
    return '>${__UUID}</csdo:EDocId>'
	
def add_5(m):
    return '<csdo:EDocDateTime>${__time(yyyy-MM-dd,)}T${__time(HH:mm:ss,)}Z</csdo:EDocDateTime>'


editor.rereplace(">urn:uuid:.*</wsa:MessageID>", add_1)
editor.rereplace(">urn:uuid:.*</int:ConversationID>", add_2)
editor.rereplace(">urn:uuid:.*</int:ProcedureID>", add_3)
editor.rereplace(">.*</csdo:EDocId>", add_4)
editor.rereplace("<csdo:EDocDateTime>.*</csdo:EDocDateTime>", add_5)

#Zamena vseh UUID aktivnogo dokumenta na odin i tot ge
#editor.rereplace("\S{8}-\S{4}-\S{4}-\S{4}-\S{12}", str(uuid.uuid4()))


