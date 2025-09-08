# Aufgabe zum JoinEnrichment

Die organisatorischen Daten einer Geschäftsstelle mit dem Namen der Geschäftsführung und den dort arbeitenden Mitarbeiter sollen mit den Adressdaten der Geschäftsstelle angereichert werden.

Die organisatorische Daten für eine Geschäftsstelle:

```json
{
    "Geschaeftsstelle": "Wiesbaden" ,
    "Geschaeftsfuehrung": "Max Mustermann",
    "Mitarbeiter": [
        {
            "Vorname": "Emily",
            "Nachname": "Johnson",
            "Bereich": "Application Development"
        }, 
        {
            "Vorname": "Michael",
            "Nachname": "Williams",
            "Bereich": "Big Data"
        }, 
        {
            "Vorname": "Sophia",
            "Nachname": "Brown",
            "Bereich": "Cloud"
        }
    ]
}
```

Eine mögliche Anreicherung, um die nötigen Geschäftsdaten der Geschäftstelle sieht folgendermaßen aus:

```json
[ {
  "Geschaeftsstelle" : "Wiesbaden",
  "Geschaeftsfuehrung" : "Meike Muster",
  "Mitarbeiter" : [ {
    "Vorname" : "Emily",
    "Nachname" : "Johnson",
    "Bereich" : "Application Development"
  }, {
    "Vorname" : "Michael",
    "Nachname" : "Williams",
    "Bereich" : "Big Data"
  }, {
    "Vorname" : "Sophia",
    "Nachname" : "Brown",
    "Bereich" : "Cloud"
  } ],
  "Straße" : "Kreuzberger Ring",
  "Hausnummer" : "13",
  "Postleitzahl" : "65205",
  "Stadt" : "Wiesbaden"
} ]
```

Nutze dazu den JoinEnrichment Prozessor, sowie den ForkEnrichment Prozessor, wie im Seminar erklärt.
Die Aufgabe wird im Folgendem in weitere kleinere Schritte unterteilt.

## Teilaufgabe 1 : GenerateFlowFile mit Json

In dieser Übung nutzen wir ausnahmsweise den `GenerateFlowFile`. Dieser Processor kann jederzeit zu Testzwecken oder Übungszwecken genutzt werden.
Füge die obrige JSON der `organisatorischen Geschäftsdaten` in den Content des Processors.

Passe den MIME Type an.

## Teilaufgabe 2

Um die Adressdaten anzureichern brauchen wir nun den ForkEnrichment Processor,
dieser erstellt zwei Datenflüsse den `enrichment` und den `original` Datenfluss.

### Teilaufgabe 2a - Vorbereitung

Wir arbeiten nun innerhalb des Enrichment Prozessors weiter.

In einer Produktivumgebung, wüssten wir nicht, welche Adresse in der JSON steht, da
mehrere organisatorischen Geschäftstellendaten, mit Adressdaten angereichert werden
sollten.

Lade nun die Geschäftsadresse aus dem Inhalt der JSON in das Attribut des FlowFiles.

### Teilaufgabe 2b - Daten aus der Datenbank auslesen

Die Adressdaten verschiedener Geschäftsstellen sind in der Tabelle `geschaeftsstellen_adressen` in der MySQL Datenbank enthalten.
In der Tabelle `geschaeftsstellen_adressen` sind folgende Spalten enthalten:
``ID;Geschaeftsstelle;Strasse;Hausnummer;Postleitzahl;Stadt;Land``

Folgende Konfiguration wird benötigt:

- **Database Connection URL:** `jdbc:mysql://localhost:3307/users`  
- **Database Driver Class Name:** `com.mysql.cj.jdbc.Driver`  
- **Database Driver Locations:** `/opt/nifi/drivers/mysql-9.4.0`  
- **Database User:** `nifiuser`  
- **Password:** `nifipassword`

Lade mit einem SQL-Befehl die Adressdaten der Geschäftstelle aus der Datenbank, nutze dabei das GS-Attribut, welches du im Schritt davor erstellt hast.

### Teilaufgabe 3 - Das Anreichern

Füge im Folgendem die beiden Flows `original` und `enrichment` in den JoinEnrichment Processor zusammen. Achte hierbei auf die Wahl der passenden Reader und Writer Services.
Teste verschiedene Enrichment Strategien und achte darauf was passiert.
