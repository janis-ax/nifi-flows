# RPath mit QueryRecord

## Vorbereitung

Nutze den InvokeHTTP-Processor, um die Daten aus der API <https://dummyjson.com/users> einzulesen.  
Terminiere alle Relationships außer `Response` und leite diese zunächst in einen Funnel.  
Stelle den Processor so ein, dass er **alle 10 Sekunden** die API abfragt.

Verwende einen zusätzlichen Processor, um den Inhalt des FlowFiles zu zerlegen.  
Jedes FlowFile soll anschließend nur die Daten einer einzelnen Person enthalten (`1 FlowFile = 1 Person`).  
Verbinde den InvokeHTTP-Processor mit dem neuen Processor über eine Connection.

## Aufgabe

In der aktuellen Connection befinden sich JSON Dateien folgenden Daten:

```json
{
      "id": 1,
      "firstName": "Emily",
      "lastName": "Johnson",
      "maidenName": "Smith",
      "age": 28,
      "gender": "female",
      "email": "emily.johnson@x.dummyjson.com",
      ...
      "address": {
        "address": "626 Main Street",
        "city": "Phoenix",
        "state": "Mississippi",
        "stateCode": "MS",
        "postalCode": "29112",
        "coordinates": {
          "lat": -77.16213,
          "lng": -92.084824
        },
        "country": "United States"
      },
      und viele weitere Einträge
}
```

Füge einen `QueryRecord` Processor hinzu, um die folgende Daten zu erhalten:

```json
[ {
  "id" : 29,
  "street" : "1837 Maple Street",
  "city" : "Indianapolis",
  "state" : "Delaware",
  "postalCode" : "81783",
  "country" : "United States"
} ]
```

> **Tipp:**
> Es gibt nicht nur RPath Funktionen, sondern auch beispielsweise RPATH_INT, um einen Integer als Rückgabewert zu bekommen anstatt eines Records.
