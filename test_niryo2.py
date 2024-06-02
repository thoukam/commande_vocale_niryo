from pyniryo2 import *
import time
import keyboard
import speech_recognition as sr


# Set robot address
# ip list (robot 75-871-948)
# 192.168.0.201 WIFI (Connected to the TB3-N-5GHz router)
robot_ip_address = "192.168.0.147"

# workspace name
workspace_name = "default_workspace"

# Création d'un dictionnaire pour la correspondance forme-couleur
shape_color_mapping = {
    "cercle": ObjectShape.CIRCLE,
    "carré": ObjectShape.SQUARE,
    "rouge": ObjectColor.RED,
    "bleu": ObjectColor.BLUE,
    "vert": ObjectColor.GREEN
}

command=['cercle rouge','cercle vert','cercle bleu','carré rouge','carré vert','carré bleu','cercle','carré']


def init_robot(robot_ip_address):
    print("initialisation du robot")
    robot=NiryoRobot(robot_ip_address)

    #mise à jour de l'outil
    robot.tool.update_tool()

    #calibration
    robot.arm.calibrate_auto()
    print("fin de calibration")

    return robot


def position_de_detection(robot):
    robot.arm.move_joints([-1.479, 0.165, -0.583, -0.074, -1.235, 0.011])

def position_de_pose(robot):
    robot.arm.move_joints([0.024, -0.272, -0.357, -0.035, -1.034, 0.015])

def convoyor(robot):
    conveyor_id = robot.conveyor.set_conveyor()
    robot.conveyor.run_conveyor(conveyor_id)

def pick_and_place(text):
    #text=text.lower()
    if text in command:
        if text==command[0]:
            position_de_detection(robot)
            robot.vision.vision_pick(workspace_name, shape=ObjectShape.CIRCLE, color=ObjectColor.RED)
            position_de_pose(robot)
            robot.tool.release_with_tool()
            convoyor(robot)

        elif text==command[1]:
            position_de_detection(robot)
            robot.vision.vision_pick(workspace_name, shape=ObjectShape.CIRCLE, color=ObjectColor.GREEN)
            position_de_pose(robot)
            robot.tool.release_with_tool()

        elif text==command[2]:
            position_de_detection(robot)
            robot.vision.vision_pick(workspace_name, shape=ObjectShape.CIRCLE, color=ObjectColor.BLUE)
            position_de_pose(robot)
            robot.tool.release_with_tool()

        elif text==command[3]:
            position_de_detection(robot)
            robot.vision.vision_pick(workspace_name, shape=ObjectShape.SQUARE, color=ObjectColor.RED)
            position_de_pose(robot)
            robot.tool.release_with_tool()

        elif text==command[4]:
            position_de_detection(robot)
            robot.vision.vision_pick(workspace_name, shape=ObjectShape.SQUARE, color=ObjectColor.GREEN)
            position_de_pose(robot)
            robot.tool.release_with_tool()

        elif text==command[5]:
            position_de_detection(robot)
            robot.vision.vision_pick(workspace_name, shape=ObjectShape.SQUARE, color=ObjectColor.BLUE)
            position_de_pose(robot)
            robot.tool.release_with_tool()

        elif text==command[6]:
            position_de_detection(robot)
            robot.vision.vision_pick(workspace_name, shape=ObjectShape.CIRCLE, color=ObjectColor.ANY)
            position_de_pose(robot)
            robot.tool.release_with_tool()
        
        elif text==command[7]:
            position_de_detection(robot)
            robot.vision.vision_pick(workspace_name, shape=ObjectShape.SQUARE, color=ObjectColor.ANY)
            position_de_pose(robot)
            robot.tool.release_with_tool()

    else:
        print("cette commande est introuvable, veuillez fournir une autre commande")
    

def listen_and_recognize():
    # Utilisation du microphone comme source audio
    with microphone as source:
        print("Ecoute...")
        # Réduction du bruit ambiant pour améliorer la précision de la reconnaissance
        recognizer.adjust_for_ambient_noise(source)
        
        # Enregistrement de l'audio à partir du microphone
        audio = recognizer.listen(source)

        try:
            print("Reconnaissance vocale en cours...")
            # Reconnaissance du texte à partir de l'audio en utilisant Google Speech Recognition
            text_reconnu = recognizer.recognize_google(audio, language="fr-FR")
            print("Vous avez dit : " + text_reconnu)
            return text_reconnu
        except sr.UnknownValueError:
            print("Google Speech Recognition n'a pas pu comprendre l'audio.")
        except sr.RequestError as e:
            print("Impossible de récupérer les résultats du service Google Speech Recognition ; {0}".format(e))


#initialisation du robot
robot=init_robot(robot_ip_address)

# creation des instances recognized et microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

print("appuyez et maintenez s pour demarer l'enregistrement...")
while True:
    if keyboard.is_pressed('s'):  # if 's' is pressed
        text = listen_and_recognize()
        pick_and_place(text)
        time.sleep(3)  # wait for 5 seconds before next iteration
        print('appuyez sur s pour effectuer une nouvelle commande')
        #keyboard.wait('esc')  # Attendre que la touche 'esc' soit pressée pour quitter le programme
