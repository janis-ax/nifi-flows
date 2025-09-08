# Ablage der ORDIX AG für die Apache NiFi Grundlagen Seminar

- [Ablage der ORDIX AG für die Apache NiFi Grundlagen Seminar](#ablage-der-ordix-ag-für-die-apache-nifi-grundlagen-seminar)
  - [Struktur des Repos](#struktur-des-repos)
  - [Hinzufügen der Demos oder Lösungen in eine bestehende NiFi Instanz über GitHub](#hinzufügen-der-demos-oder-lösungen-in-eine-bestehende-nifi-instanz-über-github)
  - [Demo Übersicht](#demo-übersicht)
  - [Übungen Übersicht](#übungen-übersicht)

## Struktur des Repos

Das GitHub Repository ist folgendermaßen aufgebaut:

```txt
demos/
├── query-record-star-wars-example.json
└── ...
sicherheitskopie/
└── json-Dateien von den beiden Repos
uebungen/
├── erweiterte-flow-komponente/
│   └── einfach-processgroups.md
├── expression-language/
│   ├── bereinige-attribute.json
│   ├── bereinige-attribute.md
│   ├── expression-language.json
│   └── expression-language.md
└── ...
Readme.md
```

Unter **Demos** befinden sich alle Flowdefinition. Eine Übersicht aller enthaltener Demos ist hier zu finden: [Demo Übersicht](#demo-übersicht)

Im Ordner **Sicherheitskopie** befindet sich der Response der Dummy URLs : [Dummy Json User](https://dummyjson.com/users) und [Placeholder Json User](https://jsonplaceholder.typicode.com/users). Da ein Großteil der Übungen auf diesen beiden URLs aufbaut, kann mit diesen JSON-Dateien anstatt eines InvokeHTTP Prozessors eine GenerateFlowFile Prozessor eingefügt werden, der fast keinen Unterschied für die Übungen darstellt.

Unter **„Übungen“** befinden sich sämtliche Flow-Definitionen sowie die Aufgabenstellungen zu den einzelnen Übungen. Diese sind jeweils in Verzeichnissen abgelegt, deren Namen den entsprechenden Foliensätzen im Seminar entsprechen. Das bedeutet: Eine Übung im Ordner „Services“ kann erst an die Seminarteilnehmer ausgegeben werden, nachdem zuvor der Foliensatz „Services“ behandelt wurde.
In der Übersicht sind auch Aufgaben enthalten, die keine Flowdefinitions brauchen: [Übungen Übersicht](#übungen-übersicht)

## Hinzufügen der Demos oder Lösungen in eine bestehende NiFi Instanz über GitHub

Dieses Repository kann in jede NiFi Instanz ab NiFi 2.0 als Registry Client (GitHubFlowRegistryClient) hinterlegt werden.

Folgende Konfiguration muss genutzt werden:

````txt
GitHub API URL: https://api.github.com/
Repository Owner: janis-ax
Repository Name: nifi-flows
Default Branch: main
Repository Path: je nachdem ob uebungen oder demos gebraucht werden --> Anpassung
Directory Filter Exclusion: [.].*
````

Die Auth-Konfiguration ist intern entnommen werden.

Der **Repository Path** muss angepasst werden, je nachdem ob *uebungen* oder *demos* gezeigt werden sollen:

| Anzuzeigen in NiFi  | Repository Path | Als Bucket in NiFi|
| --------------- | ---------- | ---------- |
| uebungen  | uebungen | die einzelnen Ordner im uebungen Ordner |
| demos | Property leer lassen | demos, sicherheitskopie und uebungen (Aber nur in Demos welche enthalten) |

## Demo Übersicht

| Kategorie: behandelte Processoren  | Zweck der Demos | "Use Case" | Flowdefinition |
| --------------- | ---------- |----|----|
| **Processors and Connection:** GenerateFlowFile, QueryRecord | verschiedene Query Records Anfragen (sind ebenfalls in den Folien enthalten), letzte Abfrage ist sehr ähnlich zur Übung | |[Flow Defintion](/demos/query-record-star-wars-example.json)|
| **Services:** ExecuteSQL, ConvertRecord, QueryRecord | Vertiefen der Services inkl. DBCPConnectionPool | Alle Produkte einer Firma, werden aus der Datenbank abgefragt und nach Kategorie geroutet |[Flow Defintion](/demos/product-data-routing.json)|
| **JoinEnrichment:** ForkEnrichment, JoinEnrichment, ExecuteSQL, QueryRecord  | Zwei Beispiele für JoinEnrichment zeigen, zweite Demo ist sehr ähnlich zur späteren Übung | **Erste:** Die Liste mit der Stückanzahl der verkauften Menge (je Datum und GS-Standort) soll mit den Preisdaten des Produktes anhand der ID angereichert werden. Ziel des Flows sind zwei weitere Spalten in der Tabelle mit "Gesamtpreis/Total" und Preis des Produktes</br> **Zweite:** Gleicher Usecase, nur diesemal nur für eine Verkaufsanzahl von einer GS an einem Tag |[Flow Defintion](/demos/product-data-join-enrichment.json)|

## Übungen Übersicht

| Aufgabenbeschreibung | behandelte Processoren  |  behandelte Themen  |Level |Flowdefinition|
| ----- | ---------- | ---------- |----|----|
| **Processors und Connections** |||||
| [Einfache Übung zu Processors and Connections](/uebungen/processors-and-connection/einfach-processors-and-connections.md) | InvokeHTTP | FlowFiles, Relationships, Funnel | sehr leicht | nicht nötig |
| [Mittlere Übung zu Processors and Connections](/uebungen/processors-and-connection/mittel-processors-and-connections.md) | InvokeHTTP, EvaluateJSONPath, SplitJSON | Scheduling, Log-Level,Properties, Namensänderung, JSON Path, Relationships, Prioritizers, Back Pressure| mittel | [Flow Definition](uebungen/processors-and-connection/mittel-processors-and-connections.json) |
| [RPath in Query Record](/uebungen/processors-and-connection/rpath-with-query-record.md) | QueryRecord | RPath, RPath_String |mittel|[Flow Definition](uebungen/processors-and-connection/rpath-in-query-record.json)|
| **Expression Language** |||||
| [Expression Language](/uebungen/expression-language/expression-language.md) | InvokeHTTP, SplitJson,UpdateAttribute, RouteOnAttribute | Scheduling,Properties, Expression Language, JsonPath| leicht | [Flow Definition](uebungen/expression-language/expression-language.json) |
| [Bereinige Attribute](/uebungen/expression-language/bereinige-attribute.md) | InvokeHTTP, EvaluteJSONPath, UpdateAttribute, GenerateFlowFile | Properties, Expression Language| leicht | [Flow Definition](uebungen/expression-language/expression-language.json) |
| **Erweiterte Flow-Komponenten** |||||
| [Einfache Process Group Übung](/uebungen/erweiterte-flow-komponenten/einfach-processgroups.md) |  |  Processgroups, In/Out Port, **Achtung, zumindest die Expression Language muss erledigt sein** | sehr leicht| nicht nötig|
| **Services** |||||
| [Erweiterte Flow Komponenten einfach](/uebungen/services/einfach-erweiterte-flow-komponenten.md) | InvokeHTTP, EvaluteJSONPath, SplitJson,UpdateAttribute, RouteOnAttribute, MergeRecord |  Scheduling,Properties, Process Groups (mit In/Out Port), **Services**(JSONTreeReader, JsonRecordWriter)| leicht | [Flow Definition](uebungen/services/einfach-erweiterte-flow-komponenten.json) |
| [Erweiterte Flow Komponenten Schwer](/uebungen/services/schwer-erweiterte-flow-komponenten.md) | InvokeHttp, SplitJson, EvaluateJsonPath, UpdateAttribute, QueryRecord, LookupRecord, EvaluateJsonPath, PutFile | Process Groups, Arbeiten mit Attribute und Content, Flow Definition, **Services**(JsonTreeReader, JsonRecordWriter, DatabaseConnectionPool,DatabaseRecordLookupService), Expression Language | schwer |[Flow Definition](uebungen/services/schwer-erweiterte-flow-komponente.json)|
| [Datenbankverbindung Einfach](/uebungen/services/einfach-datenbankverbindung.md) | Execute SQL | Service auf Root Ebene: **Database Connection Pool**| leicht | [Flow Definition](uebungen/services/einfach-datenbankverbindung.json) |
| [Datenbankverbindung Mittel](/uebungen/services/mittel-datenbankverbindung.md) | ExecuteSQL, InvokeHTTP, QueryRecord,PutDatabaseRecord |  Relationship Retry, Service auf Root Ebene: **Database Connection Pool** (zusätzlich in Teilaufgabe 2 Process Groups und Funnel)| mittel| [Flow Definition](uebungen/services/mittel-datenbankverbindung.json) |
| [Join Enrichment](/uebungen/join-enrichment/join-enrichment.md)|GenerateFlowFile, ForkEnrichment, JoinEnrichment, EvaluateJsonPath, ExecuteSQLRecord|JoinEnrichment, **Database Connection Pool**|mittel|[Flow Definition](uebungen/services/join-enrichment.json)|
| [Monitoring](/uebungen/services/monitoring.md)|GenerateFlowFile,InvokeHTTP, LogAttribute|ExpressionLanguage, Relationships, Bulletin Board, DataProvenance (inkl. Lineage), **Bonusaufgaben:** ,Flow Configuration History, Summary </br> **Wichtig:** In der Aufgabe sollen die Teilnehmer auch abschätzen, wie viele User von der API bereitgestellt werden. (Ende 100, Anfang 200 ist eine gute Schätzung) -> die API stellt genau 208 zur Verfügung |mittel|[Flow Definition](uebungen/services/monitoring.json)|
| [Reporting Task](/uebungen/services/reporting-task.md)||**Reporting Task:** MonitorMemory, NiFi API| leicht/mittel | keine vonnöten |
