📹 Surveillance Vidéo Avancée avec YOLO
Ce projet implémente un système de surveillance vidéo basé sur le modèle YOLO (You Only Look Once) pour la détection d'objets en temps réel. Il permet d'identifier et de suivre des objets, notamment des personnes, dans une vidéo, en mettant en évidence ceux qui entrent dans une zone d'intérêt prédéfinie. Ce système est conçu pour des applications de sécurité, offrant une détection rapide et précise pour alerter les opérateurs en cas de situation anormale.
📜 Description et Utilité
Ce projet utilise des techniques avancées de vision par ordinateur et d'apprentissage automatique pour analyser des flux vidéo. En combinant le modèle YOLO avec une zone d'intérêt définie par un polygone, il détecte les objets (principalement des personnes) et signale leur présence dans une zone spécifique. Ses applications incluent :

Surveillance de zones sensibles (parkings, entrées, zones sécurisées).
Détection proactive pour la sécurité publique.
Analyse en temps réel pour une intervention rapide.

✨ Fonctionnalités

🕵️‍♂️ Détection d'objets : Identification en temps réel des objets (personnes, véhicules, etc.) dans une vidéo à l'aide du modèle YOLOv8.
📍 Zone d'intérêt : Mise en évidence des objets situés dans une zone définie par un polygone configurable.
🎨 Visualisation : Dessin de cadres rouges autour des objets détectés et affichage de la zone d'intérêt en magenta.
🖱️ Interaction : Affichage des coordonnées RGB et des positions des pixels via un callback de souris.
📡 Traitement vidéo : Analyse frame par frame d'une vidéo ou d'un flux en direct.

🛠️ Prérequis
Pour exécuter ce projet, vous aurez besoin des éléments suivants :

Système d'exploitation : Windows, macOS, ou Linux.
Python : Version 3.8 ou supérieure.
Bibliothèques Python :
opencv-python pour le traitement vidéo.
ultralytics pour le modèle YOLO.
pandas pour la manipulation des données.
numpy pour les calculs numériques.


Modèle YOLO : Fichier yolov8s.pt (inclus dans le dépôt ou téléchargeable via Ultralytics).
Fichier des classes COCO : Fichier coco.txt contenant la liste des classes d'objets détectables.
Vidéo d'entrée : Une vidéo au format .mp4 (exemple : VIDEO.mp4).

🚀 Installation et Mise en Marche
Suivez ces étapes pour configurer et exécuter le projet :

Clonez le dépôt GitHub :
git clone https://github.com/HaMzaCheh/Advanced-Video-Surveillance-YOLO.git
cd Advanced-Video-Surveillance-YOLO


Créez un environnement virtuel (recommandé) :
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate


Installez les dépendances :
pip install opencv-python ultralytics pandas numpy


Téléchargez le modèle YOLO :

Le fichier yolov8s.pt est téléchargeable automatiquement par Ultralytics lors de l'exécution du script, ou vous pouvez le placer manuellement dans le dossier du projet.


Ajoutez les fichiers nécessaires :

Assurez-vous que le fichier coco.txt est dans le répertoire du projet.
Placez votre vidéo d'entrée (par exemple, VIDEO.mp4) dans le répertoire ou mettez à jour le chemin dans le script main.py.


Lancez le script :
python main.py



🖥️ Utilisation
Une fois le script lancé, voici comment interagir avec le système :

Visualisation : Une fenêtre nommée Ecran_detection affiche la vidéo avec :
Les cadres rouges autour des personnes détectées dans la zone d'intérêt.
La zone d'intérêt délimitée par un polygone magenta.


Interaction avec la souris : Déplacez le curseur sur la fenêtre pour afficher les coordonnées (x, y) et les valeurs BGR des pixels dans la console.
Sortie : Appuyez sur la touche ESC pour quitter l'application.
Personnalisation : Modifiez les coordonnées de la zone d'intérêt dans main.py (variable area) pour ajuster la zone surveillée.

🧠 Architecture du Code
Le script principal (main.py) est structuré comme suit :

Chargement du modèle : Utilisation de yolov8s.pt via la bibliothèque ultralytics.
Lecture de la vidéo : Utilisation d'OpenCV pour lire les frames de la vidéo.
Détection d'objets : Application du modèle YOLO pour identifier les objets dans chaque frame.
Zone d'intérêt : Vérification si les objets (personnes) se trouvent dans la zone définie à l'aide de cv2.pointPolygonTest.
Visualisation : Dessin des cadres autour des objets détectés et de la zone d'intérêt.
Interaction : Gestion des événements de souris pour afficher les informations de pixels.

Le code est modulaire et peut être adapté pour d'autres vidéos ou zones d'intérêt.
🎥 Simulation / Démo

Lancez le script main.py comme décrit dans la section Installation.
La fenêtre Ecran_detection affiche la vidéo avec les détections en temps réel.
Déplacez la souris sur la fenêtre pour voir les informations de pixels dans la console.
Testez avec différentes vidéos ou modifiez les coordonnées de la zone d'intérêt pour observer les changements.

Pour une démonstration, utilisez une vidéo contenant des personnes dans un environnement surveillé (par exemple, un parking ou une entrée). Le système mettra en évidence les personnes entrant dans la zone d'intérêt.
🤝 Contribution
Nous accueillons toutes les contributions ! Pour contribuer :

Forkez le dépôt.
Créez une branche pour vos modifications :git checkout -b ma-nouvelle-fonctionnalite


Faites vos modifications et testez-les.
Soumettez une pull request avec une description claire de vos changements.

Veuillez respecter les conventions de codage Python (PEP 8) et inclure des tests si possible.

💬 Note Finale
Merci d'explorer ce projet ! Si vous avez des questions, des idées d'amélioration, ou des retours, n'hésitez pas à ouvrir une issue ou à me contacter. Votre feedback est précieux pour faire évoluer ce système de surveillance ! 🚀
