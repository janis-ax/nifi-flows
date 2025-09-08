# Expression Language

## Übung: Erstellung einer User-Abfrage

Aus der API: <https://dummyjson.com/users> sollen Nutzerdaten ausgelesen werden.

### Teilaufgabe 1

Nutze den **InvokeHTTP-Processor**, um die Daten aus der API <https://dummyjson.com/users> abzurufen.  
Stelle ihn so ein, dass er **alle 10 Sekunden** die API abfragt.  
Alle Relationships außer `Response` werden terminiert und zunächst in einen Funnel geleitet.

### Teilaufgabe 2

Verwende einen zusätzlichen **Processor**, um den Inhalt des FlowFiles zu zerlegen.  
Jedes FlowFile soll nur die Daten einer einzelnen Person enthalten (`1 FlowFile = 1 Person`).  
Verbinde den **InvokeHTTP-Processor** mit dem **neuen Processor** über eine Connection.

### Teilaufgabe 3

Überschreibe den Namen des FlowFiles mit der ID des Users und einem Zeitstempel deiner Wahl.  
Das Namensschema soll wie folgt aussehen: `id-zeitstempel.json`

> Tipp: Nutze eine Kombination aus `EvaluateJSONPath` und `UpdateAttribute`.

### Teilaufgabe 4

Die **Rolle des Users** (aus dem Inhalt des FlowFiles) soll als **Attribut** dargestellt werden.  
Lade die FlowFiles zunächst in einen **Funnel** und überprüfe die Attribute.  
Es soll einer der folgenden Werte eingetragen werden: `'admin'`, `'moderator'`, `'user'`.

> Tipp: Die Rolle findest du ganz am Ende des JSON-Objekts jedes Users.

### Teilaufgabe 5

Erstelle ein neues Attribut **`userSalary`**:  

- User mit der Rolle **admin** erhalten **5000 €**  
- Alle anderen erhalten **3000 €**

Erstelle ein **Routing basierend auf dem Gehalt**:  
→ `5000` geht an die Relationship „Vorgesetzte“  
→ Alles darunter an „Mitarbeiter“

> Tipp: Die ersten fünf User sind Admins, die restlichen nicht.

Vergiss nicht, allen Processoren **aussagekräftige Namen** zu geben.
