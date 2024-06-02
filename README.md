# commande_vocale_niryo
Ce projet programme contrôle un robot Niryo2. Le robot détecte et manipule des objets via reconnaissance vocale. Il utilise un dictionnaire pour associer formes et couleurs aux objets. Le programme inclut l'initialisation, la calibration, le déplacement du bras, et l'exécution de commandes vocales.

# Projet de Contrôle du Robot Niryo2

## Description du Projet

Ce projet utilise la bibliothèque `pyniryo2` pour contrôler un robot Niryo One afin de réaliser des tâches de détection et de manipulation d'objets basées sur la reconnaissance vocale. Le robot est programmé pour reconnaître des formes et des couleurs spécifiques et effectuer des actions en conséquence.

## Fonctionnalités

- **Initialisation du Robot** : Mise à jour de l'outil et calibration automatique du bras du robot.
- **Détection d'Objets** : Utilisation de la vision pour détecter des objets spécifiques basés sur leur forme et couleur.
- **Manipulation d'Objets** : Prise et dépose d'objets à des positions définies.
- **Convoyeur** : Activation d'un convoyeur pour le transport d'objets.
- **Reconnaissance Vocale** : Utilisation de la reconnaissance vocale pour recevoir des commandes d'utilisateur et exécuter des actions en conséquence.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone git@github.com:thoukam/DM_Analyse_De_Donnees.git
    cd DM_Analyse_De_Donnees
    ```

2. Installez les dépendances nécessaires :
    ```bash
    pip install pyniryo2 speechrecognition keyboard
    ```

## Utilisation

1. **Initialiser le robot** :
    - Assurez-vous que le robot est connecté au réseau et que l'adresse IP est correctement définie dans le script (`robot_ip_address`).
    - Assurez-vous également de definir correctement le workplace du robot niryo2 aprés l'avoir calibrer manuellement

2. **Exécuter le script** :
    - Lancez le script principal :
        ```bash
        python test_niryo2.py
        ```

3. **Interagir avec le robot** :
    - Appuyez et maintenez la touche `s` pour démarrer l'enregistrement vocal.
    - Donnez des commandes vocales telles que "cercle rouge", "carré bleu", etc.
    - Le robot exécutera les actions correspondantes basées sur la commande vocale.

## Commandes Vocales

Le robot est programmé pour reconnaître les commandes vocales suivantes :
- `cercle rouge`
- `cercle vert`
- `cercle bleu`
- `carré rouge`
- `carré vert`
- `carré bleu`
- `cercle`
- `carré`

## Structure du Code

- `init_robot(robot_ip_address)`: Initialise et calibre le robot.
- `position_de_detection(robot)`: Positionne le bras du robot pour détecter des objets.
- `position_de_pose(robot)`: Positionne le bras du robot pour déposer des objets.
- `convoyor(robot)`: Active le convoyeur.
- `pick_and_place(text)`: Effectue des actions de prise et de dépose d'objets basées sur la commande vocale.
- `listen_and_recognize()`: Écoute et reconnaît les commandes vocales.

## Auteur

Yves Thoukam Thotchum, 3A Robotique, POLYTECH DIJON
