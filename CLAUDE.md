# mayetlab.fr — règles du dépôt

Site de l'association MayetLab. Voir README.md pour le contexte.

- `public/` est déployé tel quel (FTPS, o2switch). Rien d'autre n'est public.
- **Ne pas mélanger les genres** : ce site parle de l'association (non
  lucrative). Le lieu et l'offre commerciale sont sur cimb.fr (CIMB SAS) ;
  on y renvoie par un lien, sans reprendre ses tarifs ni son offre.
- **Aucune ressource tierce** (polices, CDN, iframes, scripts, images
  distantes) : `tools/check-third-party.py` fait échouer la CI.
- **CSP stricte** dans `public/.htaccess` : `script-src 'self'`,
  `style-src 'self'` — donc ni `<script>` exécutable, ni `onclick=`, ni
  attribut `style=`. Tout passe par `public/assets/site.css`.
- **Le logo néon** : animation `electric` de l'ancien site, à conserver telle
  quelle ; le PNG est noir sur transparent, `invert(1)` l'allume en blanc.
- `/status.pdf`, `/reglement.pdf`, `/adhesion.pdf` restent à la racine : le
  bulletin papier imprime ces adresses.
- Nouvelle page : `public/<nom>/index.html` (URL propre par l'arborescence).
- Accessibilité : garder les contrastes AA (jetons en tête de site.css),
  les `alt`, le lien d'évitement et le respect de `prefers-reduced-motion`.
