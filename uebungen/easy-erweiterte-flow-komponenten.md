# Erweiterte Flow Komponenten

Wenn du die Aufgabe **Expression Language** bereits gemacht hast, überspringe den ersten Teil und starte direkt mit [Übung: Erstellung von Process Groups.](#übung-erstellung-von-process-groups)

## Übung: Erstellung einer User-Abfrage

Aus der API <https://dummyjson.com/users> sollen Nutzerdaten ausgelesen werden.  
Vergiss nicht, deinen Processoren aussagekräftige Namen zu geben.

### Teilaufgabe 1

Nutze den InvokeHTTP-Processor, um die Daten aus der API <https://dummyjson.com/users> einzulesen.  
Terminiere alle Relationships außer `Response` und leite diese zunächst in einen Funnel.  
Stelle den Processor so ein, dass er **alle 10 Sekunden** die API abfragt.

### Teilaufgabe 2

Verwende einen zusätzlichen Processor, um den Inhalt des FlowFiles zu zerlegen.  
Jedes FlowFile soll anschließend nur die Daten einer einzelnen Person enthalten (`1 FlowFile = 1 Person`).  
Verbinde den InvokeHTTP-Processor mit dem neuen Processor über eine Connection.

### Teilaufgabe 3

Die **Rolle des Users** (aus dem Inhalt des FlowFiles) soll als **Attribut** dargestellt werden.  
Leite die FlowFiles zunächst in einen Funnel und überprüfe die Attribute.  
Es soll einer der folgenden Werte eingetragen werden: `'admin'`, `'moderator'`, `'user'`.

> Tipp: Die Rolle findest du ganz am Ende des JSON-Objekts jedes Users.

### Teilaufgabe 4

4a Erstelle ein neues Attribut „userSalary“:

- User mit der Rolle admin erhalten 5000 €  
- Alle anderen erhalten 3000 €

4b Erstelle ein Routing basierend auf dem Gehalt:  
→ `3000` für „Mitarbeiter“,  
→ `5000` für „Vorgesetzte“

> Tipp: Die ersten fünf User sind Admins, die restlichen nicht.

## Übung: Erstellung von Process Groups

Erstelle aus den vorhandenen Processoren **Process Groups**.  
Gruppiere nicht zu klein – **zwei Gruppen reichen** für diesen Dataflow.

Beispielsweise:

- `Fetch Data from API` – Processoren zur Datenabfrage  
- `Transforming and Routing` – Processoren zur Verarbeitung und Weiterleitung

## Übung: Arbeiten mit MergeRecord

Füge zwei weitere Processoren hinzu.  
Diese sollen alle *Vorgesetzten* und alle *Mitarbeiter* jeweils in *ein FlowFile* zusammenführen.

> **Tipp:**  
> Im FlowFile der Vorgesetzten sollten **5 Einträge** sein,  
> im FlowFile der Mitarbeiter **25 Einträge**.

## Übung: Arbeiten mit Flowdefinitions

Exportiere eine FlowFile-Definition von einer Process Group deiner Wahl (möglichst mit eine Process Group auswählen, die auch einen Service enthält):

- einmal **mit External Services**  
- einmal **ohne External Services**

Importiere beide Versionen erneut und beobachte, **was sich verändert**.
