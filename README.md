# Übungen und Demos zu Apache NiFi

Table of Contents:

- [Übungen und Demos zu Apache NiFi](#übungen-und-demos-zu-apache-nifi)
  - [Struktur des Repos](#struktur-des-repos)
  - [Hinzufügen der Demos oder Lösungen in eine bestehende NiFi-Instanz über GitHub](#hinzufügen-der-demos-oder-lösungen-in-eine-bestehende-nifi-instanz-über-github)
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

Unter **Demos** befinden sich alle Flowdefinitionen. Eine Übersicht aller enthaltener Demos ist hier zu finden: [Demo Übersicht](#demo-übersicht)

Im Ordner **Sicherheitskopie** befinden sich die Response der Dummy-URLs: [Dummy Json User](https://dummyjson.com/users) und [Placeholder Json User](https://jsonplaceholder.typicode.com/users). Da ein Großteil der Übungen auf diesen beiden URLs aufbaut, kann mit diesen JSON-Dateien anstatt eines InvokeHTTP-Prozessors ein GenerateFlowFile-Prozessor eingefügt werden, der fast keinen Unterschied für die Übungen darstellt.

Unter **„Übungen“** befinden sich sämtliche Flowdefinitionen sowie die Aufgabenstellungen zu den einzelnen Übungen.
Diese sind nach Themen in Verzeichnissen abgelegt. Alle Übungen befinden sich unten in der Übersicht: [Übungen Übersicht](#übungen-übersicht)

## Hinzufügen der Demos oder Lösungen in eine bestehende NiFi-Instanz über GitHub

Dieses Repository kann in jede NiFi-Instanz ab NiFi 2.0 als Registry-Client (GitHubFlowRegistryClient) hinterlegt werden.

**Folgende Konfiguration muss genutzt werden:**

![GitHub FlowRegistry-Client](/doc/images/githubclient.png)

Die Auth-Konfiguration kann intern entnommen werden.

Der **Repository-Path** muss angepasst werden, je nachdem, ob *Übungen* oder *Demos* gezeigt werden sollen:

| Anzuzeigen in NiFi  | Repository Path | Als Bucket in NiFi|
| --------------- | ---------- | ---------- |
| Übungen  | uebungen | die einzelnen Ordner (z. B. processors and connection) im uebungen Ordner |
| Demos | Property leer lassen | Demos, Sicherheitskopie und Übungen (aber nur in Demos, sind Flowdefinitionen  enthalten) |

## Demo Übersicht

| Kategorie: behandelte Processoren  | Zweck der Demos | "Use Case" | Flowdefinition |
| --------------- | ---------- |----|----|
| **Processors and Connection:** GenerateFlowFile, QueryRecord | verschiedene Query Records Anfragen (sind ebenfalls in den Folien enthalten), letzte Abfrage ist sehr ähnlich zur Übung | |[Query Record Star Wars](/demos/product-data-routing.json)|
|  **Processors and Connection:** GenerateFlowFile, QueryRecord  | Einfache Demo | Werte von Preisen auf zwei Nachkommastellen runden |[Werte Runden](/demos/werte-runden.json)|
| **Processors and Connection:** GenerateFlowFile, RetryFlowFile | | Ein kleiner Flow, welcher Prozessoren mit dem RetryFlowFile Prozessor warten lässt |[Sleep](/demos/sleep.json)|
|  **Processgroups:** Einfache Prozessoren mit InvokeHTTP, QueryRecord und Processgruppen | Einfache Demo | **Erste Prozessgroup:** Diese Prozessgruppe macht drei verschiedene API-Calls, gegen eine IP aus Italien, Deutschland und den USA. Alternativ kann auch ein JSON-Array über den Input-Port gegeben werden. Danach werden die FlowFiles mit Query-Record gefiltert (nach Deutschland, Italien, USA und andere Nationen). </br> **Zweite Prozessgroup:** Diese Prozessgruppe macht mehrere Abfragen gegen eine API und merged die FlowFiles dann mit der Bin-Packing Strategie.  |[API Calls and Query Record](/demos/API-Calls-und-QueryRecord.json) </br></br> [API Call and Merging with Bin Strategy](/demos/Multiple-Abfragen-Merge.json) |
| **Services:** ExecuteSQL, ConvertRecord, QueryRecord | Vertiefen der Services inkl. DBCPConnectionPool | Alle Produkte einer Firma, werden aus der Datenbank abgefragt und nach Kategorie geroutet |[Product Routing](/demos/product-data-routing.json)|
| **JoinEnrichment:** ForkEnrichment, JoinEnrichment, ExecuteSQL, QueryRecord  | Zwei Beispiele für JoinEnrichment zeigen, zweite Demo ist sehr ähnlich zur späteren Übung | **Erste:** Die Liste mit der Stückanzahl der verkauften Menge (je Datum und GS-Standort) soll mit den Preisdaten des Produktes anhand der ID angereichert werden. Ziel des Flows sind zwei weitere Spalten in der Tabelle mit "Gesamtpreis/Total" und Preis des Produktes</br> **Zweite:** Gleicher Usecase, nur diesemal nur für eine Verkaufsanzahl von einer GS an einem Tag |[Join Enrichment](/demos/product-data-join-enrichment.json)|
| **JDBC-Treiber Download:** Download von Postgres und SQL-Datenbank Treibern| Download von JDBC Treibern | Einfache Prozessoren + Parameter |[JDBC Treiber](/demos/Download-JDBC-Treiberjson.json)|
| **Performance Turning** |  | Ein kleiner Flow, der zeigt, wie Compressing von FlowFiles zu besser Performance führt. | [Perfomance Turning](/demos/perfomance-turning.json)|

## Übungen Übersicht

| Link zur Aufgabenbeschreibung | behandelte Processoren | behandelte Themen | Level | Flowdefinition |
| ----- | ---------- | ---------- |----|----|
| **Processors and Connections** |||||
| [Einfache Übung zu Processors and Connections](/uebungen/processors-and-connection/einfach-processors-and-connections.md) | InvokeHTTP | FlowFiles, Relationships, Funnel | sehr leicht | nicht nötig |
| [Mittlere Übung zu Processors and Connections](/uebungen/processors-and-connection/mittel-processors-and-connections.md) | InvokeHTTP, EvaluateJSONPath, SplitJSON | Scheduling, Log-Level, Properties, Namensänderung, JSON Path, Relationships, Prioritizers, Back Pressure | mittel | [Flowdefinition](uebungen/processors-and-connection/mittel-processors-and-connections.json) |
| [RPath in Query Record](/uebungen/processors-and-connection/rpath-with-query-record.md) | QueryRecord | RPath, RPath String |mittel|[Flowdefinition](uebungen/processors-and-connection/rpath-in-query-record.json)|
| **Expression Language** |||||
| [Expression Language](/uebungen/expression-language/expression-language.md) | InvokeHTTP, SplitJson, UpdateAttribute, RouteOnAttribute | Scheduling, Properties, Expression Language, JsonPath | leicht | [Flowdefinition](uebungen/expression-language/expression-language.json) |
| [Bereinige Attribute](/uebungen/expression-language/bereinige-attribute.md) | InvokeHTTP, EvaluteJSONPath, UpdateAttribute, GenerateFlowFile | Properties, Expression Language | leicht | [Flowdefinition](uebungen/expression-language/expression-language.json) |
| **Erweiterte Flow-Komponenten** |||||
| [Einfache Process Group Übung](/uebungen/erweiterte-flow-komponenten/einfach-processgroups.md) | | Process groups, In/Out Port, **Achtung, zumindest die Expression Language muss erledigt sein** | sehr leicht | nicht nötig |
| **Services** |||||
| [Erweiterte Flow Komponenten einfach](/uebungen/services/einfach-erweiterte-flow-komponenten.md) | InvokeHTTP, EvaluteJSONPath, SplitJson, UpdateAttribute, RouteOnAttribute, MergeRecord | Scheduling, Properties, Process Groups (mit In/Out Port), **Services**(JSONTreeReader, JsonRecordWriter) | leicht | [Flowdefinition](uebungen/services/einfach-erweiterte-flow-komponenten.json) |
| [Erweiterte Flow Komponenten Schwer](/uebungen/services/schwer-erweiterte-flow-komponenten.md) | InvokeHttp, SplitJson, EvaluateJsonPath, UpdateAttribute, QueryRecord, LookupRecord, EvaluateJsonPath, PutFile | Process Groups, Arbeiten mit Attribute und Content, Flowdefinition, **Services**(JsonTreeReader, JsonRecordWriter, DatabaseConnectionPool, DatabaseRecordLookupService), Expression Language | schwer |[Flowdefinition](uebungen/services/schwer-erweiterte-flow-komponente.json)|
| [Datenbankverbindung Einfach](/uebungen/services/einfach-datenbankverbindung.md) | Execute SQL | Service auf Root Ebene: **Database Connection Pool**| leicht | [Flowdefinition](uebungen/services/einfach-datenbankverbindung.json) |
| [Datenbankverbindung Mittel](/uebungen/services/mittel-datenbankverbindung.md) | ExecuteSQL, InvokeHTTP, QueryRecord, PutDatabaseRecord | Relationship Retry, Service auf Root Ebene: **Database Connection Pool** (zusätzlich in Teilaufgabe 2 Process Groups und Funnel) | mittel | [Flowdefinition](uebungen/services/mittel-datenbankverbindung.json) |
| [Join Enrichment](/uebungen/join-enrichment/join-enrichment.md)|GenerateFlowFile, ForkEnrichment, JoinEnrichment, EvaluateJsonPath, ExecuteSQLRecord|JoinEnrichment, **Database Connection Pool**|mittel|[Flowdefinition](uebungen/services/join-enrichment.json)|
| [Monitoring](/uebungen/services/monitoring.md)|GenerateFlowFile,InvokeHTTP, LogAttribute | ExpressionLanguage, Relationships, Bulletin Board, DataProvenance (inkl. Lineage), **Bonusaufgaben:** Flow Configuration History, Summary </br> **Wichtig:** In der Aufgabe sollen die Teilnehmer auch abschätzen, wie viele User von der API bereitgestellt werden. (Ende 100, Anfang 200 ist eine gute Schätzung) -> die API stellt genau 208 zur Verfügung |mittel|[Flowdefinition](uebungen/services/monitoring.json)|
| [Reporting Task](/uebungen/services/reporting-task.md)||**Reporting Task:** MonitorMemory, NiFi API | leicht/mittel | keine vonnöten |
