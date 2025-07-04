````markdown
# 📹 Surveillance Vidéo Avancée avec YOLO  
*Détection d’objets en temps réel pour une sécurité proactive*

Ce projet implémente un système de surveillance vidéo en temps réel basé sur le modèle **YOLO (You Only Look Once)**.  
Il détecte et suit des objets — principalement des personnes — dans une zone d’intérêt prédéfinie, offrant une solution rapide, précise et réactive, idéale pour les environnements exigeant une vigilance accrue.

---

## 📜 Description & Utilité  

Ce système analyse un flux vidéo via des techniques avancées de vision par ordinateur et apprentissage automatique. Il détecte les objets et signale leur présence dans une zone configurée par un polygone.  
Applications principales :  
- 🏢 Surveillance de parkings, accès et zones sensibles  
- 🚨 Sécurité publique proactive et prévention d’incidents  
- ⏱️ Analyse vidéo en temps réel pour des interventions rapides  

---

## ✨ Fonctionnalités clés  

- 🕵️‍♂️ **Détection d’objets** (personnes, véhicules, etc.) en temps réel avec YOLOv8  
- 📍 **Zone d’intérêt paramétrable** via polygone affiché en magenta  
- 🎨 **Visualisation intuitive** avec cadres rouges autour des objets dans la zone  
- 🖱️ **Interaction souris** : affichage en console des coordonnées et valeurs BGR des pixels survolés  
- 📡 **Traitement frame par frame** depuis fichier vidéo ou flux en direct  

---

## 🛠️ Prérequis  

- OS : Windows, macOS ou Linux  
- Python 3.8+  
- Bibliothèques Python :  
  - `opencv-python`  
  - `ultralytics`  
  - `pandas`  
  - `numpy`  
- Modèle YOLO (`yolov8s.pt`) disponible localement ou téléchargé automatiquement  
- Fichier classes COCO (`coco.txt`) dans le dossier projet  
- Vidéo `.mp4` (ex : `VIDEO.mp4`)  

---

## 🚀 Installation & démarrage rapide  

1. Cloner le dépôt :  
   ```bash
   git clone https://github.com/HaMzaCheh/Advanced-Video-Surveillance-YOLO.git
   cd Advanced-Video-Surveillance-YOLO
````

2. Créer et activer un environnement virtuel (fortement recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. Installer les dépendances :

   ```bash
   pip install opencv-python ultralytics pandas numpy
   ```

4. Préparer les fichiers :

   * Placer `coco.txt` dans le dossier du projet
   * Mettre la vidéo `.mp4` (ex : `VIDEO.mp4`) dans le dossier ou ajuster son chemin dans `main.py`

5. Lancer l’application :

   ```bash
   python main.py
   ```

---

## 🖥️ Utilisation

* La fenêtre `Ecran_detection` s’ouvre et affiche la vidéo avec :

  * Cadres rouges autour des objets détectés **dans la zone d’intérêt**
  * Zone d’intérêt tracée en magenta
* Survolez la fenêtre avec la souris pour voir dans la console coordonnées et valeurs BGR des pixels
* Appuyez sur `ESC` pour quitter
* Modifiez la variable `area` dans `main.py` pour changer la zone surveillée

---

## 🧠 Architecture & fonctionnement

* Chargement du modèle YOLOv8 via `ultralytics`
* Lecture vidéo frame par frame avec OpenCV
* Détection des objets dans chaque frame
* Vérification de la présence dans la zone via `cv2.pointPolygonTest`
* Affichage des cadres et de la zone d’intérêt
* Gestion des événements souris

Le code est modulaire et adaptable à différents flux ou zones.

---

## 🎥 Démonstration / Simulation

* Lancez `python main.py` pour visualiser la détection en temps réel
* Testez différentes vidéos ou modifiez la zone d’intérêt
* Recommandé : vidéo avec personnes dans un environnement surveillé (parking, entrée, etc.)

---

## 🤝 Contribution

Contributions bienvenues !

* Forkez le projet
* Créez une branche :

  ```bash
  git checkout -b ma-nouvelle-fonctionnalite
  ```
* Modifiez et testez
* Soumettez une pull request claire

Merci de respecter PEP 8 et d’inclure des tests si possible.

---

💬 **Merci pour votre intérêt ! Vos retours sont essentiels pour améliorer ce projet 🚀**
N’hésitez pas à ouvrir une issue ou me contacter via GitHub.
