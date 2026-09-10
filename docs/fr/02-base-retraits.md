# 2. Base : distinguer les préconditions d’un retrait

Cette fiche décrit le programme `base/withdrawer`, pas une garantie sur l’état actuel du réseau. Lecture statique le 10 septembre 2026 : aucun RPC, retrait ou transfert exécuté.

## Avant les étapes onchain

Le [code main.go](https://github.com/base/withdrawer/blob/d7364c7c14cec27e17c7b5751b7f7b7a749c62c3/main.go) fournit les contrôles suivants :

| Élément | Règle dans le code lu |
| --- | --- |
| Réseau prédéfini | Les quatre entrées Base/OP exigent `--fault-proofs`. |
| RPC | `--rpc` désigne L1 ; `--l2-rpc` désigne L2. |
| Personnalisation avec fault proofs | Fournir ensemble `--l2-rpc`, `--portal-address`, `--dgf-address` et `--asr-address`. |
| Signataire | Choisir exactement une méthode parmi clé, mnemonic ou Ledger. |
| Frais | Ne pas combiner prix legacy et options EIP-1559 ; les deux options EIP-1559 doivent être renseignées ensemble. |

**Attention aux versions :** le README actuel et le parseur utilisent tous deux `--dgf-address`. Une ancienne page indexée mentionnait `--dfg-address` ; ce problème est déjà corrigé et ne constitue pas un nouveau correctif. La configuration personnalisée actuelle exige aussi `--asr-address` (AnchorStateRegistry). Les liens ci-dessous sont fixés à la révision `d7364c7c14cec27e17c7b5751b7f7b7a749c62c3`.

## Séparer les états

L’initiation sur L2, la preuve sur L1 et la finalisation sont distinctes. Le README exige, pour son flux avec fault proofs, que l’adresse de finalisation soit celle ayant prouvé le retrait. Il précise qu’un jeu blacklisté, une résolution défavorable ou un changement de type respecté peuvent imposer une nouvelle preuve. Attendre un délai ne suffit donc pas à garantir la finalisation.

Le chemin principal du code vérifie le statut finalisé, la possibilité de prouver et l’horodatage de preuve ; si celui-ci vaut zéro, il prouve puis retourne. Sinon, il tente la finalisation. Il contient encore un TODO concernant certains cas où une nouvelle preuve est nécessaire : ne pas promettre une récupération automatique.

## Informations utiles pour un diagnostic

Noter version, réseau, hash de transaction L2, adresses de contrats, adresse publique du signataire et erreur exacte. Ne jamais publier clé privée, phrase de récupération ou URL RPC contenant un secret. La compatibilité d’une version avec un déploiement doit être vérifiée séparément.

Le [parcours existant](https://github.com/JulienKervarrec/withdrawer/tree/main/docs/fr) développe les mécanismes. Aucune nouvelle installation, compilation ou exécution de tests ; consulter les sources amont pour les vérifications ultérieures.

Retour au [sommaire](README.md).
