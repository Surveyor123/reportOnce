# reportOnce

reportOnce é um pequeno complemento do NVDA que impede o NVDA de repetir as informações de posição do objeto (por exemplo, "3 de 10") para cada objeto do mesmo grupo.

### Uso

1. Abra as configurações do NVDA e vá para a categoria Apresentação de objetos.
2. Verifique se "Relatar informações de posição do objeto" está marcada. A nova caixa de seleção só aparece nesse caso.
3. Marque "Relatar informações de posição apenas uma vez".

Quando ativada, o NVDA relata as informações de posição ao mover para um objeto e não as repete enquanto você se move entre objetos com o mesmo pai, função e nível. Elas são anunciadas novamente quando você entra em um grupo diferente ou volta a um grupo.

Quando a caixa de seleção não está marcada, o NVDA se comporta exatamente como antes.

### Observações

- Pressionar NVDA+Tab sempre relata todas as informações.
- Atualmente abrange mudanças de foco e navegação por objetos. O modo de navegação não é afetado.

### Requisitos

NVDA 2025.1 ou posterior.
