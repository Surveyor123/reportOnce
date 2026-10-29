# reportOnce

reportOnce est une petite extension NVDA qui empêche NVDA de répéter les informations de position de l'objet (par exemple « 3 sur 10 ») pour chaque objet d'un même groupe.

### Utilisation

1. Ouvrez les paramètres de NVDA et accédez à la catégorie Présentation des objets.
2. Vérifiez que « Signaler les informations de position de l'objet » est cochée. La nouvelle case n'apparaît que dans ce cas.
3. Cochez « Signaler la position une seule fois ».

Lorsque l'option est activée, NVDA signale la position quand vous passez à un objet et ne la répète pas tant que vous vous déplacez entre des objets ayant le même parent, le même rôle et le même niveau. Elle est annoncée de nouveau lorsque vous entrez dans un autre groupe ou que vous revenez à un groupe.

Lorsque la case n'est pas cochée, NVDA se comporte exactement comme avant.

### Remarques

- Appuyer sur NVDA+Tab signale toujours toutes les informations.
- Couvre actuellement les changements de focus et la navigation par objet. Le mode navigation n'est pas concerné.

### Prérequis

NVDA 2025.1 ou version ultérieure.
