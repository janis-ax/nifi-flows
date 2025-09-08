# Processors and Connections

## Übung: Erstellung einer User Abfrage

Aus der API: <https://dummyjson.com/users> sollen Nutzerdaten ausgelesen werden.

### Teilaufgabe 1

Aus der API: <https://dummyjson.com/users> sollen Nutzerdaten ausgelesen werden.
Nutze dazu den InvokeHTTP-Processor für das Einlesen der Daten aus der API.
Terminieren alle Relationships ausgenommen: NoRetry, Response, Retry. Laden diese zunächst in einen Funnel.

### Teilaufgabe 2

Verwende einen zusätzlichen Processor, um die Inhalt des FlowFiles zu zerlegen.
Jedes FlowFile soll anschließend nur die Daten einer einzelnen Person enthalten (1 FlowFile = 1 Person).
Verbinde anschließend den InvokeHTTP-Processor mit den neuen Processor mithilfe einer Connection.

### Teilaufgabe 3

Der ID der User(aus dem Inhalt des FlowFiles) soll als Attribut dargestellt werden, nutze dazu einen weiteren Processor.
Lade die FlowFiles zunächst in ein Funnel und überprüfen Sie die Attribute.
Wiederhole diesen Schritt mit der Rolle des Users
-> Hier einer der folgenden Werte eingetragen werden: 'admin','moderator','user'

### Teilaufgabe 4

- **InvokeHTTP-Processor konfigurieren:**  
  Stell ihn so ein, dass **zu Beginn jeder Minute** automatisch die API abgefragt wird.

- **Processoren umbenennen:**  
  Gib allen Processoren **aussagekräftige Namen**, damit man direkt sieht, was sie machen.

- **Connection zwischen Processor 2 und 3 anpassen:**  
  Stell sicher, dass die **ältesten FlowFiles zuletzt** verarbeitet werden.  
  → Außerdem: **Maximal 10 Objekte** dürfen gleichzeitig übertragen werden (Back Pressure Object Threshold).

- **Log Level ändern:**  
  Setz das Log Level des **InvokeHTTP-Processors** auf **INFO**. Achte darauf was passiert.
