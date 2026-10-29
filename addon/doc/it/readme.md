# reportOnce

reportOnce è un piccolo componente aggiuntivo per NVDA che impedisce a NVDA di ripetere le informazioni sulla posizione dell'oggetto (ad esempio «3 di 10») per ogni oggetto dello stesso gruppo.

### Utilizzo

1. Apri le impostazioni di NVDA e vai alla categoria Presentazione oggetti.
2. Assicurati che «Riporta informazioni sulla posizione dell'oggetto» sia selezionata. La nuova casella compare solo in questo caso.
3. Seleziona «Riporta le informazioni sulla posizione una sola volta».

Quando è attivata, NVDA riporta le informazioni sulla posizione quando ti sposti su un oggetto e non le ripete mentre ti muovi tra oggetti con lo stesso genitore, ruolo e livello. Vengono annunciate di nuovo quando entri in un gruppo diverso o torni a uno precedente.

Quando la casella non è selezionata, NVDA si comporta esattamente come prima.

### Note

- Premendo NVDA+Tab vengono sempre riportate tutte le informazioni.
- Al momento copre i cambi di focus e la navigazione tra oggetti. La modalità navigazione non è interessata.

### Requisiti

NVDA 2025.1 o successivo.
