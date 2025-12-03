# JOLT Übungsaufgaben mit Hinweisen

## Aufgabe 1 – Keys umbenennen & verschachteln
### Input
```json
{
  "firstName": "Anna",
  "lastName": "Fischer",
  "age": 28
}
```

### Ziel
```json
{
  "person": {
    "name": {
      "first": "Anna",
      "last": "Fischer"
    },
    "age": 28
  }
}
```

### Hinweis
- Direktes Feldmapping
- Keine Wildcards notwendig
- Nutze Pfade wie "person.name.first"

---

## Aufgabe 2 – Alle Felder dynamisch kopieren
### Input
```json
{
  "x": 12,
  "y": 99,
  "z": 42
}
```

### Ziel
```json
{
  "values": {
    "x": 12,
    "y": 99,
    "z": 42
  }
}
}
```

### Hinweis
- Verwende * für alle Keys
- Verwende & um Key-Namen zu übernehmen
- Beispiel: "*": "values.&"

---

## Aufgabe 3 – Array filtern & transformieren
### Input
```json
{
  "products": [
    {"name": "A", "price": 10},
    {"name": "B", "price": 25},
    {"name": "C", "price": 30}
  ]
}
```

### Ziel
```json
{
  "prices": [10, 25, 30]
}
```

### Hinweis
- Nutze "products": { "*": { "price": "prices[]" } }
- Nutze "*" zur Iteration des Arrays

---

## Aufgabe 4 – Dynamischer Key als Wert
### Input
```json
{
  "items": {
    "k1": {"value": 100},
    "k2": {"value": 200}
  }
}
```

### Ziel
```json
{
  "result": [
    {"id": "k1", "value": 100},
    {"id": "k2", "value": 200}
  ]
}
```

### Hinweis
- $ → aktueller Key (k1, k2)
- &1 → Index der Arrayposition
- Nutze: result[&1].id und result[&1].value

---

## Aufgabe 5 – Default-Werte & Zeitstempel (für NiFi)
### Input
```json
{
  "user": "tom"
}
```

### Ziel
```json
{
  "user": "tom",
  "status": "${status}",
  "timestamp": "${now():format('yyyy-MM-dd HH:mm:ss')}"
}
```

### Hinweis
- Nutze default Operation
- ${...} wird von NiFi ersetzt, nicht von JOLT
- Gültige JSON-Strings beachten

---

## Aufgabe 6 – Tiefe Verschachtelung flatten
### Input
```json
{
  "data": {
    "nested": {
      "value1": 1,
      "value2": 2
    }
  }
}
```

### Ziel
```json
{
  "value1": 1,
  "value2": 2
}
```

### Hinweis
- Du gehst zwei Ebenen tief
- Nutze "data": { "nested": { "*": "&" } }

---

## Aufgabe 7 – Arrays zu Objekt gruppieren
### Input
```json
{
  "keys": ["a", "b", "c"],
  "values": [10, 20, 30]
}
```

### Ziel
```json
{
  "mapped": {
    "a": 10,
    "b": 20,
    "c": 30
  }
}
```

### Hinweis
- Beide Arrays haben denselben Index
- Indexmatching notwendig

---

## Aufgabe 8 – Bedingtes Mapping (leicht)
### Input
```json
{
  "user": {
    "role": "admin",
    "name": "Lena"
  }
}
```

### Ziel
```json
{
  "type": "admin",
  "username": "Lena"
}
```

### Hinweis
- Direktes Mapping ohne Wildcards
- "user.role" → "type"
- "user.name" → "username"

---

## Aufgabe 9 – Mehrstufiges Array mappen
### Input
```json
{
  "departments": [
    {
      "name": "IT",
      "employees": [
        {"name": "Max", "id": 1},
        {"name": "Sara", "id": 2}
      ]
    },
    {
      "name": "HR",
      "employees": [
        {"name": "Tom", "id": 3}
      ]
    }
  ]
}
```

### Ziel
```json
{
  "employeeIds": [1, 2, 3]
}
```

### Hinweis
- Zwei *-Ebenen notwendig
- Greife tief innen auf "id" zu
- Nutze "employeeIds[]" im Zielpfad

---

## Aufgabe 10 – Kombination von Wildcards
### Input
```json
{
  "orders": {
    "o1": {"total": 100, "currency": "EUR"},
    "o2": {"total": 200, "currency": "USD"}
  }
}
```

### Ziel
```json
{
  "orderList": [
    {"orderId": "o1", "total": 100},
    {"orderId": "o2", "total": 200}
  ]
}
```

### Hinweis
- $ → aktueller Key (o1, o2)
- &1 → Array-Index
- Nutze orderList[&1].orderId und orderList[&1].total
