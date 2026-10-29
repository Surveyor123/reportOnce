# reportOnce

reportOnce es un pequeño complemento de NVDA que evita que NVDA repita la información de posición del objeto (por ejemplo, «3 de 10») para cada objeto del mismo grupo.

### Uso

1. Abra los ajustes de NVDA y vaya a la categoría Presentación de objetos.
2. Asegúrese de que «Informar de la posición del objeto» esté marcada. La nueva casilla solo aparece en ese caso.
3. Marque «Informar de la posición solo una vez».

Cuando está activada, NVDA informa de la posición al moverse a un objeto y no la repite mientras se desplaza entre objetos con el mismo padre, rol y nivel. Se anuncia de nuevo al entrar en un grupo diferente o al volver a uno.

Si la casilla no está marcada, NVDA se comporta exactamente como antes.

### Notas

- Al pulsar NVDA+Tab siempre se informa de toda la información.
- Actualmente cubre los cambios de foco y la navegación por objetos. El modo exploración no se ve afectado.

### Requisitos

NVDA 2025.1 o posterior.
