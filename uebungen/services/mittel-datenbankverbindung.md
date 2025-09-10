# Datenbankverbindung

## Übung: Userdaten in die Datenbank laden

Das Ziel dieser Übung ist Account Daten aus der API <https://jsonplaceholder.typicode.com/users> zu fetchen und diese in eine Datenbank zu speichern.
Dabei sollen die wichtigsten Daten aus den Userdaten gefiltert werden.

### Teilaufgabe 1

Lege einen **Controller Service** namens **Database Connection Pool** auf **Root-Ebene** an.  
Nutze folgende Konfiguration:

- **Database Connection URL:** `jdbc:mysql://localhost:3307/users`  
- **Database Driver Class Name:** `com.mysql.cj.jdbc.Driver`  
- **Database Driver Locations:** `/opt/nifi/drivers/mysql-9.4.0`  
- **Database User:** `nifiuser`  
- **Password:** `nifipassword`

Verifiziere, dass die Verbindung zur Datenbank hergestellt werden kann.  
Aktiviere den **Controller Service**.

### Teilaufgabe 2

Aus der API <https://jsonplaceholder.typicode.com/users> sollen die Nutzer in eine Datenbank gespeichert werden.

Nutze den **InvokeHTTP-Processor**, um die Daten aus der API zu laden. Terminiere alle Relationships außer `Response`. Stelle den Processor so ein, dass er **alle 10 Sekunden** die API abfragt.

Verwende einen zusätzlichen Processor, um die Inhalt des FlowFiles zu zerlegen.
Jedes FlowFile soll anschließend nur die Daten einer einzelnen Person enthalten (1 FlowFile = 1 Person).

#### Teilaufgabe 3

#### Teilaufgabe 3a

Aus dieser JSON:

```json
{
  "id" : 1,
  "name" : "Leanne Graham",
  "username" : "Bret",
  "email" : "Sincere@april.biz",
  "address" : {
    "street" : "Kulas Light",
    "suite" : "Apt. 556",
    "city" : "Gwenborough",
    "zipcode" : "92998-3874",
    "geo" : {
      "lat" : "-37.3159",
      "lng" : "81.1496"
    }
  },
  "phone" : "1-770-736-8031 x56442",
  "website" : "hildegard.org",
  "company" : {
    "name" : "Romaguera-Crona",
    "catchPhrase" : "Multi-layered client-server neural-net",
    "bs" : "harness real-time e-markets"
  }
  ...
}
```

soll folgendes JSON werden:

```json
{
  "userID" : 1,
  "name" : "Leanne Graham",
  "username" : "B.biz",
  "email" : "Sincere@april.biz"
}
```

In diesem Schritt müssen die Daten so angepasst werden,
dass sie genauso heißen, wie in der Tabelle oder im kleineren JSON vorgegeben.
Außerdem sollen in diesem Schritt die Daten gefiltert werden, nach den Userdaten.
Die Tabelle hat folgende Spalten. Der erste Eintrag ist noch nicht in der Tabelle vorhanden, sondern dient nur der Darstellung.

```csv
+---------------+--------------------------+------------------+---------------------------+
| userID        | name                     | username         | email                     |
+---------------+--------------------------+------------------+---------------------------+
|             1 | Leanne Graham            | Bret             | Sincere@april.biz         |
+---------------+--------------------------+------------------+---------------------------+
```

Verwende zur Anpassung einen Processor, der die Daten aus einer JSON filtern kann.
> Tipp: QueryRecord eignet sich.

#### Teilaufgabe 3b

Füge einen Processor hinzu, der **jedes FlowFile als Record** in die Datenbank schreibt (Tabelle: `userdata`). Nutze die retry Funktion des Processors.

Starte den Processor zum Aufrufen der API nur einmal um Fehlermeldungen zu vermeiden. (Fehlermeldungen würden durch doppelte Einträge mit der gleichen ID in der Datenbank entstehen)
Starte den restlichen Process.

#### Teilaufgabe 3c

Teste, ob das Laden der Daten in die Datenbank funktioniert hat anhand eines weiteren Processors, der alle Daten aus der Tabelle ausliest.
Überprüfe, welches Dateiformat das FlowFile hat.
