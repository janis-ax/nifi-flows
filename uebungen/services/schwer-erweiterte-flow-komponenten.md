# Erweiterte Flow Komponenten

## Übung: Zusammenführung von User Daten

Aus der APIs <https://dummyjson.com/users> sollen die Kontaktdaten von Personen gefiltert werden und mit den Adressdaten des Users anhand der ID aus der Datenbank zusammengefügt werden.

Beispiel für gefilterte Daten aus der API:

```json
[{
    "id": 1,
    "firstName": "Emily",
    "lastName": "Johnson",
    "email": "emily.johnson@x.dummyjson.com",
    "phone": "+81 965-431-3024"
}]
```

Beispiel für Eintrag aus der Datenbank:

```json
{
  "id" : 1,
  "street" : "626 Main Street",
  "postalCode" : "29112",
  "city" : "Phoenix",
  "state" : "Mississippi",
  "country" : "United States"
}
```

Das Ergebnis soll folgendermaßen aussehen:

```json
[ {
  "id" : 1,
  "email" : "emily.johnson@x.dummyjson.com",
  "phone" : "+81 965-431-3024",
  "name" : "Emily Johnson",
  "address" : {
    "id" : 1,
    "street" : "626 Main Street",
    "postalCode" : "29112",
    "city" : "Phoenix",
    "state" : "Mississippi",
    "country" : "United States"
  }
} ]
```

### Teilaufgabe 1

Aus der API: <https://dummyjson.com/users> sollen Nutzerdaten ausgelesen werden.
Nutze dazu den InvokeHTTP-Processor für das Einlesen der Daten aus der API.
Terminieren alle Relationships ausgenommen: Response. Laden diese zunächst in einen Funnel.
Passen den Processor an, dass dieser alle 10 Sekunden die API abfrägt.

### Teilaufgabe 2

Verwende einen zusätzlichen Processor, um die Inhalt des FlowFiles zu zerlegen.
Jedes FlowFile soll anschließend nur die Daten einer einzelnen Person enthalten (1 FlowFile = 1 Person).
Verbinde anschließend den InvokeHTTP-Processor mit dem neuen Processor mithilfe einer Connection.

### Teilaufgabe 3

Ziel ist es diesen Aufbau in der Json zu erzeugen:

```json
[{
    "id": 1,
    "email": "emily.johnson@x.dummyjson.com",
    "phone": "+81 965-431-3024",
    "name": "Emily Johnson",
}]
```

Um dies zu erreichen, müssen einige Schritte durchlaufen werden, da die ursprüngliche JSON wie folgt aussieht:

```json
{
      "id": 1,
      "firstName": "Emily",
      "lastName": "Johnson",
      "maidenName": "Smith",
      "age": 28,
      "gender": "female",
      "email": "emily.johnson@x.dummyjson.com",
      "phone": "+81 965-431-3024",
      "username": "emilys",
      "password": "emilyspass",
      "birthDate": "1996-5-30",
      "image": "https://dummyjson.com/icon/emilys/128",
      "bloodGroup": "O-",
      und viele weitere Einträge
}
```

#### Teilaufgabe 3a - Die JSON verkleinern

Als erstes soll die JSON, um unnötige Key-Value-Paare verkleinert werden. Dieser Processor benötigt Services, denke daran diese auf Root Ebene anzulegen. An dieser Stelle ist es noch nicht nötig, `firstName` und `lastName` zusammenzufügen.

> Tipp: Der Processor QueryRecord eignet sich dazu gut.

#### Teilaufgabe 3b

Um `firstName` und `lastName` am einfachsten zusammenzufügen, schreibe beide Key-Value-Paare als Attribute in die FlowFiles.
Nutze Expression Language, um beide Attribute als neues Attribut `name` in die FlowFiles zu schreiben.
Füge diese Prozessoren am besten vor dem den Prozessor aus Teilaufgabe 3a, dadurch sparst du dir Zwischenschritte.

> Tipp: Du kannst auch mehrere Processoren dazu verwenden.

#### Teilaufgabe 3c

Füge nun das neue Attribute `name` als key-Value-Paar wieder in den Content der FlowFiles.

### Teilaufgabe 4

Addressdaten mit folgenden Aufbau sollen aus der Datenbank eingelesen werden und den Kontaktdaten der Personen hinzugefügt werden:

```json
{
  "id" : 1,
  "street" : "626 Main Street",
  "postalCode" : "29112",
  "city" : "Phoenix",
  "state" : "Mississippi",
  "country" : "United States"
}
```

Das Ergebnis kann beispielsweise folgendermaßen aussehen:

```json
[ {
  "id" : 1,
  "email" : "emily.johnson@x.dummyjson.com",
  "phone" : "+81 965-431-3024",
  "name" : "Emily Johnson",
  "address" : {
    "id" : 1,
    "street" : "626 Main Street",
    "postalCode" : "29112",
    "city" : "Phoenix",
    "state" : "Mississippi",
    "country" : "United States"
  }
} ]
```

Folgende Konfigurationen für die Verbindung zur Datenbank werden benötigt:

- **Database Connection URL:** `jdbc:mysql://localhost:3307/users`  
- **Database Driver Class Name:** `com.mysql.cj.jdbc.Driver`  
- **Database Driver Locations:** `/opt/nifi/drivers/mysql-9.4.0`  
- **Database User:** `nifiuser`  
- **Password:** `nifipassword`

Die Daten sollen passend zur ID der Person verknüpft werden. Das bedeutet, wenn die Person die ID 1 hat, soll sie passend auch die Adressdaten mit ID 1 erhalten.

### Teilaufgabe 5

Füge einen PutFile Prozessor hinzu, um alle JSON Dateien abzulegen. Es ist nötig davor einen weiteren Processor hinzuzufügen, um die FlowFiles umzubenennen, damit diese nicht doppelt im Ordner existieren.
