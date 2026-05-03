# Class Diagram (Mermaid.js)

## Mermaid Diagram 

``` mermaid
classDiagram
class Train {
  -trainId: String
  -status: String
  -location: String
  +start()
  +stop()
  +updateLocation()
}

class Track {
  -trackId: String
  -condition: String
  -location: String
  +updateCondition()
}

class Sensor {
  -sensorId: String
  -type: String
  -status: String
  +detect()
  +sendData()
}

class Alert {
  -alertId: String
  -message: String
  -severity: String
  -timestamp: Date
  +triggerAlert()
  +notifyOperator()
}

class Operator {
  -operatorId: String
  -name: String
  -role: String
  +monitorSystem()
  +respondToAlert()
}

class Maintenance {
  -maintenanceId: String
  -schedule: Date
  -status: String
  +scheduleRepair()
  +performRepair()
}

Train "1" -- "1" Track : runsOn
Track "1" -- "1..*" Sensor : has
Sensor "1" -- "0..*" Alert : generates
Operator "1" -- "0..*" Alert : handles
Alert "1" -- "0..1" Maintenance : triggers
Maintenance "1" -- "1..*" Track : repairs
Maintenance "1" -- "0..*" Train : services
```

------------------------------------------------------------------------

## Plain Text Version (Fallback)

-   Train → runs on → Track (1:1)\
-   Track → has → Sensor (1 to many)\
-   Sensor → generates → Alert (1 to many)\
-   Operator → handles → Alert (1 to many)\
-   Alert → triggers → Maintenance (0 or 1)\
-   Maintenance → repairs → Track (1 to many)\
-   Maintenance → services → Train (0 to many)
