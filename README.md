````markdown
# 📹 Surveillance Vidéo Avancée avec YOLO

Un système de **surveillance vidéo en temps réel** basé sur le modèle **YOLO (You Only Look Once)** pour la détection et le suivi d’objets, principalement des personnes, dans une zone d’intérêt définie.  
Idéal pour des applications de sécurité nécessitant une détection rapide et précise.

---

## 📜 Description et Utilité

Ce projet utilise la vision par ordinateur et l’apprentissage automatique pour analyser un flux vidéo, détecter des objets, et signaler leur présence dans une zone prédéfinie par un polygone.  
Applications typiques :  
- Surveillance de parkings, entrées, zones sensibles  
- Sécurité publique proactive  
- Analyse vidéo en temps réel pour intervention rapide

---

## ✨ Fonctionnalités

- 🕵️‍♂️ Détection d’objets (personnes, véhicules, etc.) en temps réel avec YOLOv8  
- 📍 Zone d’intérêt configurable par polygone (affichage magenta)  
- 🎨 Visualisation avec cadres rouges autour des objets détectés dans la zone  
- 🖱️ Interaction souris affichant coordonnées et valeurs RGB des pixels  
- 📡 Traitement vidéo frame par frame depuis fichier ou flux direct

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
- Fichier des classes COCO (`coco.txt`) dans le dossier projet  
- Vidéo d’entrée au format `.mp4` (ex : `VIDEO.mp4`)

---

## 🚀 Installation et Mise en Marche

1. Cloner le dépôt :  
   ```bash
   git clone https://github.com/HaMzaCheh/Advanced-Video-Surveillance-YOLO.git
   cd Advanced-Video-Surveillance-YOLO
````

2. Créer et activer un environnement virtuel (recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows : venv\Scripts\activate
   ```

3. Installer les dépendances :

   ```bash
   pip install opencv-python ultralytics pandas numpy
   ```

4. Placer les fichiers nécessaires :

   * `coco.txt` dans le dossier projet
   * Vidéo `.mp4` (ex: `VIDEO.mp4`) ou modifier le chemin dans `main.py`

5. Lancer le script :

   ```bash
   python main.py
   ```

---

## 🖥️ Utilisation

* Une fenêtre `Ecran_detection` affiche la vidéo analysée.
* Les objets détectés dans la zone d’intérêt sont encadrés en rouge.
* La zone d’intérêt est dessinée en magenta.
* Déplacez la souris dans la fenêtre pour afficher coordonnées (x,y) et valeurs BGR des pixels dans la console.
* Appuyez sur `ESC` pour quitter.
* Pour modifier la zone surveillée, ajustez la variable `area` dans `main.py`.

---

## 🧠 Architecture du Code

* **Chargement du modèle** YOLOv8 via `ultralytics`.
* **Lecture vidéo** frame par frame avec OpenCV.
* **Détection d’objets** dans chaque frame.
* **Vérification** si les objets détectés sont dans la zone définie (`cv2.pointPolygonTest`).
* **Visualisation** des détections et de la zone d’intérêt.
* **Gestion d’interactions souris** pour affichage des infos pixel.

Le code est modulaire et facilement adaptable à d’autres vidéos ou zones.

---

## 🎥 Simulation / Démo

* Lancez `python main.py` et observez la détection en temps réel.
* Testez avec différentes vidéos ou modifiez la zone d’intérêt pour voir l’impact.
* Utilisez une vidéo avec des personnes dans un environnement surveillé (parking, entrée, etc.) pour une démonstration réaliste.

---

## 🤝 Contribution

Contributions bienvenues !

* Forkez le projet
* Créez une branche dédiée :

  ```bash
  git checkout -b ma-nouvelle-fonctionnalite
  ```
* Testez vos modifications
* Ouvrez une pull request claire et documentée

Merci de respecter PEP 8 et d’inclure des tests si possible.

---

💬 **Merci d’explorer ce projet ! Vos retours sont précieux pour l’améliorer 🚀**

```
