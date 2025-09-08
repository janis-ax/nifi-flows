# Monitoring

## Übung: Erstellung eines Loggings für API

Aus der API: <https://dummyjson.com/users> sollen Nutzerdaten ausgelesen werden.
Um fehlgeschlagene Anfragen aufzudecken, wird hier besonders auf Monitoring-
Möglichkeiten eingegangen.

### Teilaufgabe 1 - Abfrage vorbereiten

Nutze den GenerateFlowFile-Prozessor, um leere FlowFiles mit einem eigenen Attribut `id` zu generieren.
Die `id` soll eine zufällige Zahl zwischen 1 und 300 sein.
> Tipp: random():mod(10) erstellt eine Zahl zwischen 1 und 10.

Nutze den InvokeHTTP-Prozessor für das Einlesen der Daten aus der API: <https://dummyjson.com/users/${id}>
Achte darauf, dass dabei die eben erstelle ID genutzt wird.

Weitere Anpassungen:

- Stelle das Logging-Level des InvokeHTTP-Prozessors auf INFO.
- Passe das Scheduling des GenerateFlowFile-Prozessors so an, dass jede Sekunde ein FlowFile generiert wird.

### Teilaufgabe 2 - Logging

In diesem Schritt sollen die fehlgeschlagenen und erfolgreichen API-Anfragen geloggt werden.
Füge dazu zwei LogAttribute-Prozessoren rechts neben dem InvokeHTTP-Prozessor hinzu.
Verbinde nun alle "success" Relationships mit einem Processor (i.F. "Success Logging Processor")
und alle fehlschlagenden Relationships mit dem zweiten Processor.   (i.F. "Failure Logging Processor")
Übrige Relationships sollen terminiert werden.
> **Tipp:** Achte auf die Status Code der Relationships vom InvokeHTTP Prozessor, um zu bestimmen, welche FlowFiles fehlschlagen.

Passe die Log-Level beider Log-Attribute-Prozessoren sinnvoll an.
Achte darauf, dass das die Einstellungen in den Property getroffen werden.

Passe die Attribute, die geloggt werden sollen, an.
Beispielsweise wie folgt:

- LogAttribute bei "Success Logging Processor": content-type und invokehttp.request.url
- LogAttribute bei "Failure Logging Processor": invokehttp.request.url, invokehttp.status.code und invokehttp.response.body

### Teilaufgabe 3 - Bulletin Board

Sieh dir die Fehlermeldungen im Bulletin Board an.
Filtere nach Meldungen des InvokeHTTP-Prozessors über die ID.
Filtere nach ``404`` und schätze ab, wie viele User durch die API bereitgestellt werden.
Wichtig: Schätzung, kein Nachschauen in der API!

### Teilaufgabe 4 - Data Provenance

Für diesen Schritt ist es hilfreich alle anderen Flows, die evtl. bei dir noch laufen sollten zu stoppen.

Gehe ins Data Provenance und sortiere die Events nach der UUID der FlowFiles.
Sieh dir die Events für ein FlowFile an

- welches am Ende durch den "Failure Logging Processor" geloggt wurde
- welches am Ende durch den "Success Logging Processor" geloggt wurde

Wo liegt der Unterschied, was fällt dir auf ?

Schaue dir die einzelnen Schritte der "Lineage" an. (einmal failure, einmal sucess)
**Wiederholungsfrage:** Wo werden diese Events gespeichert ?

### Bonusaufgaben

Navigiere unter dem Burgermenü in die Flow Configuration History und die Summary von NiFi.
Sieh dir an, welche Übersichten du dort vorfindest und welche Einstellungen du von dort aus treffen
kannst. Mach dir am besten Notizen.
