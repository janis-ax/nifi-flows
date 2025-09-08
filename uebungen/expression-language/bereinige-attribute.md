# Bereinige Attribute durch Expression Language

Durch die Prozessoren werden durch komplexe Flows viele eigene oder prozessorspezifische Attribute hinzugefügt,
diese sind teilweise unnötig und erschweren die Arbeit mit Attributen.

## Teilaufgabe 1

Erstelle zur Veranschaulichung folgenden kurzen Dataflow aus InvokeHTTP und SplitJson.

1. Aus der API: <https://dummyjson.com/users> sollen Nutzerdaten ausgelesen werden.
Nutze dazu den InvokeHTTP-Processor für das Einlesen der Daten aus der API: <https://dummyjson.com/users>.
Terminieren alle Relationships ausgenommen: Response. Laden diese zunächst in einen Funnel.

1. Schaue dir an, wie viele neue Attribute in deinen aktuellen FlowFiles stehen.

## Teilaufgabe 2

Als Vergleich kannst du einen GenerateFlowFile Processor auf dein Board ziehen und ein eigenes FlowFile erstellen.
Füge dazu folgenden Json Ausschnitt als Custom Text ein und passe den Mime Type im GenerateFlowFile Processor an:

```json
{
  "id" : 1,
  "name" : "Leanne Graham",
  "username" : "Bret",
  "email" : "Sincere@april.biz"
}
```

Füge eine Connection zu einem Funnel und schaue dir an,
wie viele Attribute das FlowFile vom GenerateFlowFile Prozessor im Vergleich hat.

## Teilaufgabe 3

Lösche nun alle unnötigen Attribute mit einem Processor.
