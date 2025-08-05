# CONVERTER_XLSX_JSON

Das Programm liest alle `.xlsx`-Dateien in einem Verzeichnis ein, verarbeitet 
dabei nur Tabellenblätter mit dem Präfix `SST_` und speichert deren Inhalte 
in einer internen Datenstruktur. 

Nach optionalen Datenvalidierungen mit Protokollierung bei Fehlern werden die 
geprüften Daten als strukturierte JSON-Datei exportiert.


## Motivation

Die manuelle Pflege von Daten erfolgt nicht selten über MS-Excel Dateien.

*	**Vorteile**:

	*	*MS-Excel ist überall verfügbar*.

		Notfalls auch per Cloud oder sogar über Google-Docs (Dateien im 
		MS-Excel Format können erstellt werden).
	
	*	*LowCost Eingabe-UI*.
	
		Nahezu Jeder kann es bedienen.

	*	*Dateiformat* ist mit vielen Programmiersprachen *verarbeitbar*.

*	**Nachteile**:

	*	*Keine UTF-8 Kodierung!*
	
	*	*VBA Anteile* sind potentielle Viren-Überträger.
	
	*	Eine *automatische Testabsicherung* ist nur mit hohem Aufwand über 
		externe Tools (GUI Click Automation) durchführbar.
	
	*	*Validierung der Eingabedaten* -- speziell Daten-übergreifende 
		Validierungen selten durchgängig!
	
	*	*Datenformat* bzw. Dateiformat `XLSX` (Textdateien in einem ZIP Container)
		ist *nicht per GIT sinnvoll versionierbar*. Daher ist das 
		*Nachverfolgen von Datenänderungen* sehr müßig!

**Abhilfe**

Die oben aufgeführten Nachteile sind gravierend! Um die Vorteile für den Einsatz
von MS-Excel als Dateneingabewerkzeuge sinnvoll nutzen zu können, sorgt ein 
Datenkonverter Abhilfe, der Dateien im MS-Excel einlesen, validieren und in ein 
maschinenlesbares Textformat (z.B. JSON, XML) überführen kann.

Das Textformat sollte zu Zwecken der Sichtkontrolle *human readable* und über
GIT zum Nachverfolgen von Änderungen versionierbar sein.

Liegen manuell gesammelte Daten ersteinmal validiert in einem maschinenlesbaren
Format vor, können diese schnell und wiederkehrend für weitere Prozesse genutzt
oder sogar in Datenbanken (z.B. PostgreSQL, ORACLE, DB2) importiert und persistent 
abgelegt werden.

Dieses Projekt implementiert einen simplen Konverter in der Programmiersprache
Python, der Excel-Dateien mit Beispieldaten einliest (Zeichenkodierung Windows),
die Datensätze validiert und die Daten als JSON (Zeichenkodierung UTF-8) wieder 
herausschreibt.

Es soll als Vorlage für ähnliche Aufgabenstellungen dienen. Daher ist es modular
aufgebaut, so dass das einzulesende Datenformat und die erforderlichen Validierungen
schnell an neue Bedrüfnisse angepasst werden können, ohne alles komplett neu
implementieren zu müssen. Validierungen können auch wesentlich umfangreicher 
implementiert werden, um auch Wechselwirkungen zwischen mehreren Datensätzen 
(z.B. Vermeidung von Duplikaten, maximale Anzahl von Datensätzen) zu berücksichtigen.
Auch kann ein Sortieren oder Umstrukturieren vor dem Datenexport noch 
berücksichtigt werden. Auch eine Aufteilung in mehrere, zu exportierende Dateien
(z.B. zur Reduzierung von Datenredundanzen hinsichtlich *Normalform*) kann
berücksichtig werden.

Wichtige Eigenschaften des vorliegenden Projekts:

*	Zentral verfügbare Projektkonfiguration über die Datei `config.py`, die an 
	die jeweiligen, lokalen Bedingungen (z.B. Verzeichnissnamen, Ausgabedateinamen)
	angepasst werden kann.

*	Zentral verfügbare Logging-Konfiguration über die Datei `logging_config.yaml`,
	die Ausgaben in Datei, Standard-Konsole und Error-Konsole zulässt.

*	Fehler werden als Exit-Code an mögliche aufrufende Prozesse zurückgegeben, um
	automatisierte Ausführungen in Rahmen von Batch-Prozessen zu ermöglichen.


## Schritte zur Initialisierung und Ausführung der Applikation mit dem Tool `UV`

### Voraussetzungen

Dieses Python Projekt benötigt zur Ausführug ein lokal installiertes Python 
in der Version 3.13 oder höher.

Als Python Paket- und Projekt-Manager kommt das Tool `uv` zum Einsatz.
Siehe hierzu auch [GitHub: `UV`](https://github.com/astral-sh/uv).

`uv` installieren mit Python und `pip`:

`python -m pip install uv`

### Source Code lokal installieren

Danach kann dieses Projekt von Github lokal als ZIP-Archiv heruntergeladen und 
entpackt oder alternativ per `git` geklont werden.

```
git clone https://github.com/marctrommen/converter_xlsx_json.git
cd converter_xlsx_json
```

Dies setzt voraus, dass `git` lokal installiert wurde. Siehe hierzu auch 
[Git installieren](https://git-scm.com/book/de/v2/Erste-Schritte-Git-installieren) 
oder [Git Download for Windows](https://git-scm.com/downloads/win)

### Virtuelles Environment erstellen

Lege eine `.venv`-Ordnerstruktur an (standardmäßig im Projektverzeichnis):

`uv venv`

###  Abhängigkeiten installieren aus `pyproject.toml`

`uv` erkennt die Abhängigkeiten automatisch im `pyproject.toml` unter 
`[project.dependencies]` und installiert sie ins `.venv` Verzeichnis.

`uv pip install -r pyproject.toml`

### (Optional) 🔒 Lock-Datei generieren (für reproduzierbare Builds)

Erzeuge eine `uv.lock` Datei:

`uv pip compile`

Danach kann mit exakt gleichen Versionen gearbeiten werden über:

`uv pip sync`

### Virtuelle Umgebung aktivieren

Falls direkt mit python gearbeiten werden soll:

`.venv\Scripts\activate.bat` (Windows)

`source .venv/bin/activate` (Linux)

### Applikation starten

Nachdem dieses Python Projekt lokal verfügbar ist, kann die Applikation 
über zwei alternative Wege ausgeführt werden.

**Alternative 1: `uv`**

Im Projektverzeichnis kann folgender `uv` Befehl genutzt werden:

`uv run src\main.py`

**Alternative 2: `venv` und `Python`**

Im Projektverzeichnis kann das *virtual Environment* aktiviert werden (siehe oben).
Danach erfolgt die Ausführung im Projektverzeichnis über:

`python src\main.py`

**Alternative 3:** Bei Verwendung von Visual Studio Code als 
Entwicklungsumgebung ist noch der Ort des virtual Environment bekannt zu geben.

Um in Visual Studio Code (VS Code) ein bestehendes Python virtual Environment 
(venv) für die Ausführung der Datei main.py zu nutzen, ist folgendermaßen 
vorzugehen:

1.	VS Code öffnen und Projektordner laden

	Öffne VS Code und lade den Ordner, in dem sich `main.py` und das virtual 
	Environment befinden.

2.	Python-Interpreter auswählen

	1.	Öffne die Befehls-Palette mit:

		`Strg` + `Shift` + `P` (Windows/Linux)
	
	2.	Gib ein: `Python: Interpreter auswählen` 
		(Englisch: `Python: Select Interpreter`)
	
	3.	Wähle den Interpreter aus, der zu dem Virtual Environment gehört:
		
		`.venv/Scripts/python.exe` (bei Windows)

3.	Datei ausführen mit dem richtigen Interpreter

	Jetzt kann die Datei `main.py` mit dem virtuellen Environment ausgeführt
	werden, z. B. über:

	Rechtsklick auf die Datei und dann im Kontextmenü auswählen
	"Python-Datei im Terminal ausführen" (oder Englisch: "Run Python File in Terminal").

