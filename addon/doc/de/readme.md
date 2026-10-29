# reportOnce

reportOnce ist ein kleines NVDA-Add-on, das verhindert, dass NVDA die Positionsinformationen von Objekten (zum Beispiel „3 von 10“) für jedes Objekt in derselben Gruppe wiederholt.

### Verwendung

1. Öffnen Sie die NVDA-Einstellungen und wechseln Sie zur Kategorie Objektpräsentation.
2. Stellen Sie sicher, dass „Positionsinformationen von Objekten ansagen“ aktiviert ist. Das neue Kontrollkästchen erscheint nur dann.
3. Aktivieren Sie „Positionsinformationen nur einmal ansagen“.

Wenn die Option aktiviert ist, sagt NVDA die Positionsinformationen beim Wechsel zu einem Objekt an und wiederholt sie nicht, solange Sie zwischen Objekten mit demselben übergeordneten Objekt, derselben Rolle und derselben Ebene wechseln. Sie werden erneut angesagt, wenn Sie eine andere Gruppe betreten oder zu einer Gruppe zurückkehren.

Ist das Kontrollkästchen nicht aktiviert, verhält sich NVDA genau wie zuvor.

### Hinweise

- NVDA+Tab sagt immer die vollständigen Informationen an.
- Derzeit werden Fokuswechsel und Objektnavigation abgedeckt. Der Lesemodus ist nicht betroffen.

### Voraussetzungen

NVDA 2025.1 oder neuer.
