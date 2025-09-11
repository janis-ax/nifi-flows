# Parameter Provider

Zweck dieser Aufgabe ist es die beiden URLs der APIs, welche in vielen Aufgaben genutzt werden, in einem Parameter Context zu nutzen.
Dabei sollen die beiden Angaben aus der Datenbank mithilfe eines Parameter Provider einen Parameter Context erstellt werden.
Der Parameter Context soll anschließend in den Processgruppen der Aufgaben festgelegt werden, sowie in den InvokeHTTP Prozessoren verwendet werden.
(Versuche so wenig, wie möglich die vorhandenen Folien zu verwenden.)

## Teilaufgabee 1: Parameter Provider in NiFi anlegen

Erstelle einen Parameter Provider in NiFi, der speziell für Datenbanken geeignet ist.

Die bereits vorhandene Tabelle `nifi_api_conf` in der Datenbank `configuration` sieht folgendermaßen aus:

```txt
+---------------------------+--------------------------------------------+
| name                      | value                                      |
+---------------------------+--------------------------------------------+
| dummyjson-api-users       | https://dummyjson.com/users                |
| placeholderjson-api-users | https://jsonplaceholder.typicode.com/users |
+---------------------------+--------------------------------------------+
```

Folgende Konfigurationen sind für den Database Connection Pool nötig:

- **Database Connection URL:** `jdbc:mysql://localhost:3307/configuration`  
- **Database Driver Class Name:** `com.mysql.cj.jdbc.Driver`  
- **Database Driver Locations:** `/opt/nifi/drivers/mysql-9.4.0`  
- **Database User:** `nifiuser`  
- **Password:** `nifipassword`

## Teilaufgabe 2: Parameter Context erstellen

Lade durch den Service, den Parameter Context. Achte darauf, dass beide URLs als nicht-sensitiv geladen werden.

## Teilaufgabe 3: Parameter Context in Prozessgruppen hinzufügen

- Füge mindestens einer Prozessgruppe den neu erstellten Parameter Context hinzu.
- Falls du noch keine Prozessgruppe für eine Übung erstellt hast, füge eine deiner Übungen in eine Prozessgruppe ein.
- Nutze die Parameter für die API im Invoke-HTTP Prozessor.
