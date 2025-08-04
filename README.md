# README

[TOC]

## Motivation

Die manuelle Pflege von Daten erfolgt nicht selten über MS-Excel Dateien.

*	**Vorteile**:

	*	*MS-Excel ist überall verfügbar*. Notfalls auch per Cloud oder sogar
		über Google-Docs (Dateien im MS-Excel Format können erstellt werden).
	
	*	*LowCost Eingabe-UI*. Nahezu Jeder kann es bedienen.

	*	*Dateiformat* ist mit vielen Programmiersprachen *verarbeitbar*.

*	**Nachteile**:

	*	*Keine UTF-8 Kodierung!*
	
	*	*VBA Anteile*sind potentielle Viren-Überträger.
	
	*	Eine *automatische Testabsicherung* ist nur mit hohem Aufwand über 
		externe Tools (GUI Click Automation) durchführbar.
	
	*	*Validierung der Eingabedaten* -- speziell Daten-übergreifende 
		Validierungen selten durchgängig!
	
	*	*Datenformat* bzw. Dateiformat `XLSX` (Textdateien in einem ZIP Container)
		ist *nicht per GIT sinnvoll versionierbar*. Daher ist das 
		*Nachverfolgen von Datenänderungen* sehr müßig!

**Abhilfe** schafft hier ein Datenkonverter, der Dateien im MS-Excel einlesen, 
validieren und in ein maschinenlesbares Textformat (z.B. JSON, XML) überführt.
Das Textformat sollte zu Zwecken der Sichtkontrolle *human readable* und über
GIT zum Nachverfolgen von Änderungen versionierbar sein.

Liegen manuell gesammelte Daten ersteinmal validiert in einem maschinenlesbaren
Format vor, können diese schnell und wiederkehrend für weitere Prozesse genutzt
oder sogar in Datenbanken (z.B. PostgreSQL, ORACLE, DB2) importiert werden.

Dieses Projekt implementiert einen simplen Konverter in der Programmiersprache
Python, der Excel-Dateien mit Beispieldaten einliest (Zeichencodierung Windows),
die Datensätze validiert und die Daten als JSON wieder herausschreibt.


## Applikation lokal ausführen

### Voraussetzungen

Dieses Python Projekt benötigt als Python Paket- und Projekt-Manager das Tool
`uv`. Siehe hierzu auch [GitHub: `UV`](https://github.com/astral-sh/uv).

Es muss lokal bereits Python in der Version 3.13 oder höher installiert sein.

`uv` installieren:

`python -m pip install uv`


### Source Code lokal installieren

Danach kann diese Projekt von Github lokal als ZIP-Archiv heruntergeladen und 
entpackt oder per GIT geclont werden.


### Applikation starten

Nachdem diese Python Projekt lokal verfügbar ist, kann die Applikation 
ausgeführt werden mit:

`uv run src\main.py`

