# Objectifs du projet:

## Un site fonctionnel listant 20+ différentes lentilles de contact, notamment...
    - 1-Day Acuvue Moist DONE
    - 1 Day Acuvue Moist for Astigmatism DONE
    - 1 Day Acuvue Moist Multifocal DONE
    - Biomedics 1 Day Extra
    - Clariti 1 Day Multifocal
    - Dailies AquaComfort Plus
    - Dailies All Day Comfort
    - Dailies AquaComfort Plus Toric
    - Dailies AquaComfort Plus Multifocal
    - Dailies Total 1 Multifocal
    - Proclear 1 day
    - SofLens Daily Disposable


## ... Avec leurs prix repectifs pour au moins 5 revendeurs ainsi que les liens pour les acheter...
    - LenStore
    - VisionDirect
    - LentillesMoinsCheres
    - MaLentille
    - OpticalDiscount


##... Mais aussi
# Next steps
- Réduire à 20 le nombre de produits
- Prendre les colonnes correspondantes des 5 et les réunir dans un fichier unique
        - DONE LenStore
        - DONE VisionDirect
        - DONE LentillesMoinsCheres 
        - DONE MaLentille
        - OpticalDiscount

Situation au 18 juin 2021;
- Une première version du site est fonctionelle
- Prochains objectifs:
    - Freeze une colonne + améliorer responsiveness du site sur les téléphones
    - Highlight en vert les cellules avec les prix les moins chers
    - Rendre plus visible les colonnes "revendeurs" des colonnes marque et nom produit
    - Automatiser la transformation de CSV vers HTML
        --> Trouver un moyen de remplacer automatiquement toutes les erreurs liées à la conversion CSV/HTML facilement
        --> DONE Trouver un moyen de faire exécuter tous les quatre fichiers en une fois

--> Nouvelle fork: essayer de créer un tableau responsive avec Flexbox


CleanCSVToHtml
TOUT REUSSI à automatiser sauf
- le fichier CSV en lui-même (+ figure out que faire en cas de trou)
- la mise à jour régulière du script sur LWS