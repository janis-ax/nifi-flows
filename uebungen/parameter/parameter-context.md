# Parameter Context für Datenbanken

Ziel der Aufgabe ist es, einen Parameter Context für die Datenbankaufgaben zu erstellen und diesen innerhalb des Database-Connection-Pool-Services und innerhalb der Prozessoren zu verwenden.

## Teilaufgabe 1

Erstelle einen Parameter Context `Database`, welcher die Database-Connection-URL, den Driver-Class-Name und die Location des Database-Drivers sowie die verwendeten Zugangsdaten des Nutzers und die Tabellen speichert.

Unterteile diese Parameter in zwei verschiedene Parameter „Contexte“ und vererbe sie dem Parameter „Context Database“.

Beispielsweise folgendermaßen:

```txt
Database
├── Database Connection
└── Tabellen
```

## Teilaufgabe 2

Verschiebe die verschiedenen Prozessgruppen (oder Flows), in welchen du eine Verbindung zur Datenbank benötigst, in eine Prozessgruppe und füge den Parameter Context `Database` hinzu.
Passe die Propertys im Service (Database Connection) und in den Prozessoren an, sodass diese die Parameter verwenden.

> **Tipp:** Der Service darf nicht auf der Root Ebene sein, sondern muss innerhalb der neu erstellten Prozessgruppe sein. Überlege kurz warum.
