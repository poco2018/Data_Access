
from socket import MSG_CTRUNC
from archicad import ACConnection
#import archicad
import sys

conn = ACConnection.connect()


assert conn, f'Communication Link is not available -timed out'

acc = conn.commands
act = conn.types
acu = conn.utilities
'''
xx = sys.modules
for x in xx:
    print(x)
sys.exit()
'''

parameters = {}
'''
# This Script uses 3D_Test with the Dialog Command
result = acc.GetActivePenTables()
#print(result)
#sys.exit()
result =acc.GetAttributesByType("BuildingMaterial")
#print(result)
result = acc.GetBuildingMaterialAttributes([result[0].attributeId])
print(result)
sys.exit()
'''
'''
parameters["command"] = "GetBNAtt"
parameters["inParams"] = ['FontPopup']
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Dialog'),parameters)
print(response)
sys.exit()
'''
parameters["command"] = "GetBMAtt"
parameters["inParams"] = ['Masonry - Mortar']
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Dialog'),parameters)
print(response)
#sys.exit()
for output in response['outparams2']:
    print(output)
for name in response['outparams2']:
    if name[0] == 'Thermal Conductivity':                                                                                                                                                                                                                  
        out = name[0] + ' = ' + name[1]
        parameters["command"] = "SetMSG"
        parameters["inParams"] = [out]
        response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Dialog'),parameters)

sys.exit()

parameters["command"] = "GetLibraryParameters"
parameters["inParams"] = [out]
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','LibraryParams'),parameters)
