# 1. Winterfell : localiser un rejet de preuve

Fiche de lecture statique, 10 septembre 2026. Elle complète le parcours Fibonacci par un diagnostic orienté intégration.

| Contrôle | Rejet ou étape | Vérification à faire dans les artefacts |
| --- | --- | --- |
| Politique | `InsufficientConjecturedSecurity`, `InsufficientProvenSecurity`, `UnacceptableProofOptions` | Comparer les options de la preuve avec la politique attendue ; ne pas abaisser le seuil pour faire passer un échantillon. |
| Corps | `UnsupportedFieldExtension` | Aligner le corps de base et l’extension entre producteurs et consommateurs. |
| Évaluation hors domaine | `InconsistentOodConstraintEvaluations` | Comparer AIR, entrées publiques et versions des deux côtés ; ce rejet ne désigne pas à lui seul une contrainte fautive. |
| Grinding | `QuerySeedProofOfWorkVerificationFailed` | Vérifier l’intégrité de la preuve et les paramètres utilisés. |
| FRI | `FriVerificationFailed` | Conserver l’erreur interne et la configuration ; distinguer cet échec des étapes précédentes. |

Source : [verify et AcceptableOptions, révision étudiée](https://github.com/facebook/winterfell/blob/2f78ee9bf667a561bdfcdfa68668d0f9b18b8315/verifier/src/lib.rs). Les pistes de diagnostic sont des recommandations de lecture, pas des causes démontrées.

Un ticket reproductible devrait indiquer révision, types AIR/hachage/engagement, options, entrées publiques communicables et erreur exacte. Ne pas joindre de témoin confidentiel. Une preuve décodée n’est pas encore une preuve acceptée.

Aucune installation ni exécution. Pour prolonger : [tests Fibonacci](https://github.com/facebook/winterfell/blob/2f78ee9bf667a561bdfcdfa68668d0f9b18b8315/examples/src/fibonacci/fib2/tests.rs), sans résultat revendiqué ici.

Suite : [Retraits Base : préconditions](02-base-retraits.md).
