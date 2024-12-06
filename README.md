English below

# ZIP Password Cracker

Ein Python-Skript, das versucht, das Passwort einer ZIP-Datei mithilfe von Brute-Force zu knacken. Es generiert Kombinationen aus Buchstaben, Zahlen und Sonderzeichen und testet diese gegen die ZIP-Datei.

## Funktionen

- Knackt ZIP-Datei-Passwörter durch Brute-Force.
- Anpassbarer Zeichensatz (Buchstaben, Zahlen, Sonderzeichen).
- Multi-Threading für schnellere Passwortversuche.

## Voraussetzungen

- Python 3.6 oder höher

## Installation

1. Installiere Python: [Python-Download](https://www.python.org/downloads/).
2. Speichere das Skript als `zip_password_cracker.py`.

## Verwendung

1. **Bearbeite das Skript**:
   - Ersetze `"ZipFile Path"` mit dem Pfad zu deiner ZIP-Datei.
   - Passe `myletters` an, um den gewünschten Zeichensatz festzulegen.
   - Ändere den Bereich `(1, 10)`, um die zu testende Passwortlänge zu definieren.
2. **Führe das Skript aus**:
   ```bash
   python zip_password_cracker.py

## Beispiel
Wenn sich deine ZIP-Datei unter C:/example/protected.zip befindet, aktualisiere diese Zeile:
  zipfile=zipfile.ZipFile("C:/example/protected.zip")

Um nur Kleinbuchstaben und Ziffern im Brute-Force-Angriff zu verwenden:
  myletters = string.ascii_lowercase + string.digits

## Hinweise
Warnung: Brute-Force-Angriffe können zeitaufwendig sein, insbesondere bei langen und komplexen Passwörtern.
Stelle sicher, dass du die Erlaubnis hast, die ZIP-Datei zu knacken. Unerlaubte Nutzung könnte gegen Gesetze oder Richtlinien verstoßen.

## Haftungsausschluss
Dieses Tool ist ausschließlich zu Bildungszwecken gedacht. Der Autor übernimmt keine Verantwortung für Missbrauch oder Schäden, die durch dieses Skript verursacht werden.

# ZIP Password Cracker

A Python script that attempts to crack the password of a ZIP file using brute force. It generates combinations of letters, numbers, and special characters and tests them against the ZIP file.

## Features

- Cracks ZIP file passwords using brute force.
- Customizable character set (letters, numbers, special characters).
- Multi-threaded for faster password attempts.

## Requirements

- Python 3.6 or higher

## Installation

1. Install Python: [Python Download](https://www.python.org/downloads/).
2. Save the script as `zip_password_cracker.py`.

## Usage

1. **Edit the script**:
   - Replace `"ZipFile Path"` with the path to your ZIP file.
   - Adjust `myletters` to include the desired character set.
   - Modify the range `(1, 10)` to define the password length range to test.
2. **Run the script** in the command line:
   ```bash
   python zip_password_cracker.py

## Example
If your ZIP file is located at C:/example/protected.zip, update this line:
  zipfile=zipfile.ZipFile("C:/example/protected.zip")

To include only lowercase letters and digits in the brute-force attack:
  myletters = string.ascii_lowercase + string.digits

## Notes
Warning: Brute-force attacks can be time-consuming, especially for long and complex passwords.
Ensure you have permission to crack the ZIP file; unauthorized use may violate laws or policies.

## License
This script is provided "as is" without any warranties. Use at your own risk.

## Disclaimer
This tool is intended for educational purposes only. The creator is not responsible for any misuse or damage caused by this script.
