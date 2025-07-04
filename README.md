# 📹 Surveillance Vidéo Avancée avec YOLO

Ce projet met en œuvre un système de **surveillance vidéo en temps réel** utilisant le modèle d'intelligence artificielle **YOLO (You Only Look Once)**, reconnu pour sa rapidité et sa précision dans la détection d’objets. Conçu principalement pour identifier et suivre des personnes, ce système analyse chaque image (frame) d’un flux vidéo afin de détecter la présence d’objets spécifiques au sein d’une zone d’intérêt définie par l’utilisateur via un polygone.

Grâce à sa capacité à traiter les vidéos en temps réel, il offre une solution efficace et réactive pour des environnements où la sécurité est cruciale. Le système ne se limite pas à la simple détection : il met en évidence uniquement les objets situés dans une zone prédéfinie, permettant ainsi de focaliser la surveillance sur des espaces stratégiques ou sensibles.

Ce projet est idéal pour les organisations souhaitant automatiser la surveillance vidéo et réduire le besoin d’intervention humaine constante, tout en augmentant la rapidité de détection d’événements critiques.

---

## 📜 Description et Utilité

Le cœur du système repose sur des techniques avancées de **vision par ordinateur** et d’**apprentissage profond**, permettant d’extraire en temps réel des informations pertinentes d’un flux vidéo. À chaque image analysée, le modèle YOLO identifie les objets (personnes, véhicules, etc.) présents, puis vérifie s’ils se trouvent dans la zone d’intérêt, définie précisément par un polygone paramétrable.

L’intérêt principal réside dans la surveillance ciblée, qui permet :

* **Surveillance de parkings, accès, et zones sensibles** : La détection ciblée dans ces espaces critiques améliore la sécurité en alertant immédiatement en cas d’intrusion ou de mouvement suspect.  
* **Sécurité publique proactive et prévention** : En détectant rapidement la présence d’individus dans des zones stratégiques, le système facilite l’intervention avant qu’un incident ne se produise.  
* **Analyse vidéo en temps réel pour intervention rapide** : La capacité à traiter les données vidéo en direct offre un avantage essentiel dans les scénarios d’urgence, permettant aux opérateurs d’agir instantanément sur les alertes générées.

Ce système s’adresse aussi bien aux entreprises, administrations publiques, organismes de sécurité, qu’à toute structure ayant besoin d’une surveillance vidéo intelligente et automatisée. Sa modularité et sa flexibilité permettent d’adapter facilement la zone d’intérêt et le type d’objets détectés en fonction des besoins spécifiques du site surveillé.


---

## ✨ Fonctionnalités clés

* 🕵️‍♂️ **Détection d’objets en temps réel** (personnes, véhicules, etc.) avec YOLOv8
* 📍 **Zone d’intérêt paramétrable** par polygone (affichage magenta à l’écran)
* 🎨 **Visualisation intuitive** avec cadres rouges sur les objets détectés dans la zone
* 🖱️ **Interaction via souris** : coordonnées (x, y) et valeurs BGR des pixels affichées dans la console
* 📡 **Traitement frame par frame** à partir d’un fichier vidéo ou d’un flux direct

---

## 🛠️ Prérequis

* Système d’exploitation : Windows, macOS ou Linux
* Python version 3.8 ou supérieure
* Bibliothèques Python nécessaires :

  * `opencv-python`
  * `ultralytics`
  * `pandas`
  * `numpy`
* Modèle YOLO (`yolov8s.pt`) accessible localement ou téléchargé automatiquement
* Fichier de classes COCO (`coco.txt`) dans le répertoire du projet
* Vidéo d’entrée au format `.mp4` (exemple : `VIDEO.mp4`)

---

## 🚀 Installation et démarrage rapide

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/HaMzaCheh/Advanced-Video-Surveillance-YOLO.git
   cd Advanced-Video-Surveillance-YOLO
   ```

2. **Créer et activer un environnement virtuel (fortement recommandé) :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances :**

   ```bash
   pip install opencv-python ultralytics pandas numpy
   ```

4. **Préparer les fichiers nécessaires :**

   * Placer `coco.txt` dans le dossier du projet
   * Mettre votre vidéo `.mp4` (exemple : `VIDEO.mp4`) dans le même dossier ou modifier son chemin dans `main.py`

5. **Lancer l’application :**

   ```bash
   python main.py
   ```

---

## 🖥️ Utilisation

* Une fenêtre nommée `Ecran_detection` s’ouvre et affiche la vidéo avec les objets détectés.
* Les objets détectés **dans la zone d’intérêt** sont entourés d’un cadre rouge.
* La zone d’intérêt est tracée en magenta.
* Déplacez la souris sur la fenêtre pour voir s’afficher dans la console les coordonnées du pixel sous le curseur ainsi que sa couleur BGR.
* Appuyez sur la touche `ESC` pour fermer l’application.
* Pour modifier la zone surveillée, ajustez la variable `area` dans `main.py` (coordonnées du polygone).

---

## 🧠 Architecture et fonctionnement du code

* Chargement du modèle YOLOv8 via la bibliothèque `ultralytics`.
* Lecture et traitement vidéo image par image avec OpenCV.
* Détection des objets dans chaque frame analysée.
* Vérification de la position des objets détectés au sein de la zone définie via `cv2.pointPolygonTest`.
* Affichage des résultats (zones, cadres) et gestion des interactions souris.
* Code modulaire, facilement adaptable à différents flux vidéo ou zones d’intérêt.

---

## 🎥 Démonstration / Simulation

* Exécutez le script `python main.py` pour voir la détection en temps réel.
* Testez avec diverses vidéos ou modifiez la zone d’intérêt pour observer l’effet.
* Recommandé : utiliser une vidéo contenant des personnes dans un espace surveillé (parking, entrée, etc.) pour visualiser les alertes.

---

## 🤝 Contribution

Les contributions sont chaleureusement bienvenues !

* Forkez ce dépôt
* Créez une branche pour votre fonctionnalité :

  ```bash
  git checkout -b ma-nouvelle-fonctionnalite
  ```
* Effectuez vos modifications et testez-les soigneusement
* Soumettez une pull request claire et documentée

Merci de respecter les bonnes pratiques Python (PEP 8) et d’inclure des tests quand c’est possible.

---

💬 **Merci d’avoir consulté ce projet ! Vos retours et suggestions sont précieux pour son amélioration continue 🚀**
N’hésitez pas à ouvrir une issue ou à me contacter via GitHub.
