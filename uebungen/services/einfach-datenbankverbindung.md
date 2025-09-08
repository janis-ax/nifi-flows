# Datenbankverbindung

## Übung: Erstellen einer Datenbankverbindung

### Teilaufgabe 1

Lege einen **Controller Service** mit dem Namen **Database Connection Pool** auf **Root-Ebene** an.  
Nutze dafür folgende Konfiguration:

- **Database Connection URL:** `jdbc:mysql://localhost:3307`  
- **Database Driver Class Name:** `com.mysql.cj.jdbc.Driver`  
- **Database Driver Locations:** `/opt/nifi/drivers/mysql-9.4.0`  
- **Database User:** `nifiuser`  
- **Password:** `nifipassword`

Überprüfe, ob die Verbindung zur Datenbank erfolgreich hergestellt werden kann.  // valdieren anstatt erfolgreich herstellen
Aktiviere anschließend den **Controller Service**.

### Teilaufgabe 2

Füge den Processor ExecuteSQL hinzu und teste ihn mit dem einfachen Kommando `show databases;`.  
Leite die success-Relationship in einen Funnel und schau dir den Inhalt des FlowFiles an.  
Welches **Dateiformat** hat das FlowFile?
