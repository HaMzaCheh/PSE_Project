import cv2
import pandas as pd
from ultralytics import YOLO
import numpy as np

# Chargement du modèle YOLO
model = YOLO('yolov8s.pt')


# Définition de la fonction pour le callback de la souris
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = frame[y, x]
        print("BGR:", colorsBGR, "Coordinate:", x, y)


# Chargement de la vidéo
cap = cv2.VideoCapture('c:/Users/PC/Documents/Projet_PYTHON/VIDEO.mp4')

# Lecture du fichier des classes COCO
with open("c:/Users/PC/Documents/Projet_PYTHON/coco.txt", "r") as my_file:
    data = my_file.read()
class_list = data.split("\n")

# Définition de la zone d'intérêt
area = [(320, 310), (250, 495), (850, 495), (775, 320)]

# Boucle pour la lecture et l'affichage des frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionnement de la frame
    frame = cv2.resize(frame, (1020, 500))

    # Prédiction des objets dans la frame
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    # Parcours des prédictions et dessin des cadres et marquages
    for index, row in px.iterrows():
        x1, y1, x2, y2, d = int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[5])
        c = class_list[d]
        if 'person' in c:
            result = cv2.pointPolygonTest(np.array(area, np.int32), (x1, y2), False)
            print(result)
            if result >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.circle(frame, (x1, y2), 4, (255, 0, 0), -1)

    # Dessin de la zone d'intérêt
    cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 0, 255), 2)

    # Affichage de la frame
    cv2.imshow("Ecran_detection", frame)

    # Appel du callback pour afficher les coordonnées RGB
    cv2.setMouseCallback('Ecran_detection', RGB)

    # Attendre l'appui sur la touche 'ESC' pour quitter
    if cv2.waitKey(25) & 0xFF == 27:
        break

# Libération des ressources et fermeture des fenêtres
cap.release()
cv2.destroyAllWindows()
