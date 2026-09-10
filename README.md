## Parcours français

[Nouvelles fiches pratiques STARK et Base](docs/fr/README.md) : relier les rejets Winterfell aux contrôles du vérificateur et identifier les préconditions des retraits Base, avec les paramètres de réseau personnalisé et les précautions de version. Lecture statique, sans exécution.

# ZK Research — STARK, SNARK & rollups

Un point d’entrée francophone pour comprendre les systèmes de preuve à partir de leur code et contribuer par des corrections documentaires ciblées.

## Deux parcours concrets

| Parcours | Ce que l’on suit dans le code | Accès |
| --- | --- | --- |
| STARK / Winterfell | Fibonacci, trace, AIR, engagements, FRI, politique d’acceptation | [6 chapitres](https://github.com/JulienKervarrec/winterfell/tree/main/docs/fr) |
| SNARK / snarkjs | Fichiers du circuit, paramètres, témoin, fullprove, vérification Groth16, export EVM | [6 chapitres](https://github.com/JulienKervarrec/snarkjs/tree/master/docs/fr) |

## Contribution proposée au projet original

[iden3/snarkjs — PR #635](https://github.com/iden3/snarkjs/pull/635) corrige cinq commandes du tutoriel : chemins des entrées et du WASM pour `fullprove`, puis cohérence du nom de clé FFLONK.

Statut à la publication, le 10 septembre 2026 : **ouverte, non fusionnée**. Le lien de la PR fait foi pour les évolutions ultérieures. La correction est isolée sur une branche dédiée, sans les chapitres français. Validation statique contre le code et le workflow du tutoriel ; aucun test exécuté.

## Comparer sans confondre

| Question | Winterfell étudié ici | snarkjs étudié ici |
| --- | --- | --- |
| Description du calcul | Trace et contraintes AIR | Circuit compilé par Circom, contraintes R1CS et témoin |
| Préparation | Pas de cérémonie de confiance annoncée par Winterfell | Powers of Tau ; phase spécifique au circuit dans le chemin Groth16 |
| Vérification suivie | Engagements, évaluations hors domaine, FRI | Combinaison des signaux publics et couplages dans le vérificateur Groth16 |
| Limite à retenir | Le README ne garantit pas une confidentialité parfaite | Les signaux publics et leur interprétation restent à la charge de l’application |

Ce tableau décrit ces implémentations, pas toutes les constructions STARK ou SNARK. Les paramètres et hypothèses de chaque protocole doivent être lus dans ses sources.

## Hyperliquid et HyperEVM

Le [parcours HyperEVM–HyperCore](https://github.com/JulienKervarrec/hyper-evm-lib/tree/main/docs/fr) suit CoreWriter, les précompiles, les conversions de montants et les ponts d’actifs. Sa checklist distingue identité du contrat, troncature décimale, émission asynchrone et observation de l’état. Il s’agit d’une lecture documentée de `hyper-evm-lib`, sans affiliation ni audit revendiqué.

## Où intervient un zk-rollup ?

Une preuve de calcul est une brique, pas un rollup complet. Pour étudier une architecture, suivre séparément :

1. La transition d’état : quelles transactions et quelles règles sont contraintes ?
2. L’énoncé public : comment ancienne et nouvelle racines d’état sont-elles liées à la preuve ?
3. Le règlement : quel contrat accepte la preuve et autorise la mise à jour ?
4. Les données : comment les utilisateurs retrouvent-ils les données nécessaires ?
5. Les opérations : dépôts, retraits, ordre des transactions et mises à jour.

Les deux forks ne mettent pas en œuvre cette chaîne complète. Une preuve de validité ne rend pas automatiquement toutes les données privées.

## Méthode et sources

Les chapitres renvoient aux fonctions lues et séparent comportement du code, limites et responsabilités de l’application. Les projets originaux restent [facebook/winterfell](https://github.com/facebook/winterfell) et [iden3/snarkjs](https://github.com/iden3/snarkjs). Le code amont et ses licences sont conservés dans les forks.

Les ajouts français sont une documentation du fork, sans validation revendiquée des mainteneurs. Aucun audit, benchmark ou résultat d’exécution n’est revendiqué.

## Pour prolonger

Mon [profil et les parcours Base](https://github.com/JulienKervarrec) regroupent aussi des lectures sur les wallets, paiements, ponts et infrastructures L2. Ces travaux sont complémentaires ; ils ne doivent pas être présentés comme des implémentations ZK.
