from archicad import ACConnection
import archicad
import sys
import math
conn = ACConnection.connect()

assert conn

acc = conn.commands
act = conn.types
acu = conn.utilities

elements = acc.GetElementsByType('Wall')
values = []
for element in elements:
    parameters = {}
    parameters["GuidInput"] = str(element.elementId.guid)
    response = acc.ExecuteAddOnCommand(act.AddOnCommandId('JSONCommands','Orientation'),parameters)
    x1 = response['Guid'][0] #Begin cord
    x2 = response['Guid'][2] #End cord
    y1 = response['Guid'][1]
    y2 = response['Guid'][3]
    pointer = response['Guid'][5] #north pointer
    adjustment = 0
    if pointer <= 90 or pointer >= 270:
        if pointer < 90:
            adjustment = pointer - 90
        else:
            adjustment = 90 - pointer  
    else:
            adjustment = pointer - 90
    angle = math.atan2((y2-y1),(x2-x1)) *180/3.14
    angle += adjustment 
    if angle <= 0:
        angle = 360 + angle
    location = 'North'
    if angle >= 45 and angle <= 135:
        location = 'west'
    elif angle > 135 and angle <= 225:
        location = 'South'
    elif angle > 225 and angle <= 315:
        location = 'East'
    elif angle > 315 or angle < 45:
        location = 'North'
    else:
        print('Angle Failed')
        sys.exit()
    propValue = act.NormalStringPropertyValue(location,'string','normal')
    propId = acu.GetUserDefinedPropertyId('Environment','Location')
    EPV = act.ElementPropertyValue(element.elementId,propId,propValue)
    values.append(EPV)
    
err = acc.SetPropertyValuesOfElements(values)
if(not err):
    print(err)