
"""
Bibliotecas usadas
"""
import csv  # Funcion donde se guardara la informacion del robot
import os  # Ubicacio de archivos
from PIL import Image, ImageTk
import threading
import time  # Funcion para el tiempo
from multiprocessing.resource_sharer import \
    stop  # Funcionpra que el robot pare de moverse
from threading import Thread
from tkinter import *  # Interfaz grafica
from tkinter import PhotoImage, messagebox, ttk  # interfaz grafica
from turtle import forward
import PIL.Image

import pygame  # reproductor de musica

"""	
Global variables
"""
robot_info = []

"""
Funcion que carga la imagen de fondo
"""
def Fondo(img):  
    ruta = os.path.join("Adicionales",img) 
    imagen = PhotoImage(file=ruta)
    return imagen 

def Imagenes(img,size):
    ruta = None
    if size != None:
        ruta = PIL.Image.open("Adicionales/"+img).resize((size))
    else:
        ruta = PIL.Image.open("Adicionales/"+img)
    imagen = ImageTk.PhotoImage(ruta)
    return imagen              

"""
leerRobot:Funcion que lee el archivo de texto con las caracteristica del robot
E:None
R:None
S:None
"""
def leerRobot():
    with open("robot_info.csv",'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            robot_info.append(line)

"""
Funcion que escribe en el archivo de texto(Actualiza el archivo)
"""
def escribirR():
    with open("robot_info.csv",'w',newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(robot_info)

"""
--> Clase que contiene los metodos para el robot
-> Contiene como metodos o funciones: 
Window: ventana principal
Todos los set and get por si llegaran a ser nesesarios
Y tambien todas las ordenes que se le pueden dar al robot
"""       
class Robot:
    def __init__(self,nombre,imagen,fecha,indicador,ventana_robot,consola):
        self.nombre = nombre
        self.imagen = imagen
        self.fecha = fecha
        self.indicador = indicador
        self.ventana_robot = ventana_robot
        self.Window()
        self.consola = consola
        self.Window1()
        self.comando = ""

    """
    Window: ventana principal
    E: No recibe parametros
    S: No retorna nada
    R: No tiene restricciones
    """	
    def Window(self):

        #self.imagen1 = Fondo("Fondo.png")
        #self.Lbl = Label(self.ventana_robot, image = self.imagen1).place(x = 0,y = 0)
        self.ventana_robot.configure(bg = "white")
        self.ventana_robot.update()

        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(1)
        self.robot1 = Imagenes("derecha 1.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()

    """
    Drak: Funcion hace que simule que el robot se va a descanzar cerrando la ventana en donde el se encuentra
    E: No recibe parametros
    S: No retorna nada
    R: No tiene restricciones
    """
    def Dark(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound-largo.mp3')
        pygame.mixer.music.play()

        messagebox.showinfo("","I am going to sleep")

        self.ventana_robot.destroy()
        self.consola.destroy()
        escribirR()

    """
    Good_morning: Funcion que hace que el robot reaccione al comando good morning saludando
    E: No recibe parametros
    S: No retorna nada
    R: No tiene restricciones
    """
    def Good_morning(self):

        messagebox.showinfo("","Good morning today is " + time.asctime())

        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound-largo.mp3')
        pygame.mixer.music.play()

        self.Nombre = Label(self.ventana_robot, font=("Arial ",20), text="Nombre: " + robot_info[0][0]
             ,height = 1,width = 15)
        self.Nombre.place(x = 50, y = 50)

        self.Fecha = Label(self.ventana_robot, font=("Arial ",20), text="Fecha de creacion: " + robot_info[0][2]
             ,height = 1,width = 35)
        self.Fecha.place(x = 150, y = 150)

    #Obtiene el nombre del robot
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    #Metodo que obtiene la imagen la imagen del robot
    def get_imagen(self):
        return self.imagen

    def set_imagen(self,imagen):
        self.imagen = imagen

    #Metodo que obtiene la fecha de creacion del robot
    def get_fecha(self):
        return self.fecha

    def set_fecha(self,fecha):
        self.fecha = fecha

    #Metodo que obtiene el indicador de la imagen
    def get_indicador(self,):
        self.indicador

    def set_indicador(self,indicador):
        self.indicador = indicador

    """
    sayhello: Funcion que hace que el robot se presente	
    E: self
    S: Mensaje de presentacion
    R: No aplica
    """
    def sayhello(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 1.mp3')
        pygame.mixer.music.play()

        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("derecha 1.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()

        messagebox.showinfo("","Hi!!!\nMy name is " + robot_info[0][0] + " \nand today is " + time.asctime())

    """
    built: Funcion que hace que el robot diga su fecha de creacion
    E: self
    S: Mensaje de fecha de creacion
    R: No aplica
    """
    def built(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()

        messagebox.showinfo("","I was created on"  + robot_info[0][2])
        messagebox.showinfo("","Im ready to play with you")

    """
    forward: Funcion que hace que el robot se mueva hacia adelante
    E: self
    S: Mensaje de movimiento hacia adelante y el movimiento
    R: No aplica
    """
    def forward(self): 

        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("zoom.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()

        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()

        messagebox.showinfo("","I am moving forward")

    #Funcion que hace que el robot se mueva hacia atras
    def backward(self): # falta logica de validacion para las imagenes
        
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(1)
        self.robot1 = Imagenes("atras.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()

        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()

        messagebox.showinfo("","I am moving backward")

    """
    Stop: Funcion que hace que el robot se detenga
    E: self
    S: Mensaje de detencion
    R: No aplica
    """
    def Stop(self):
        pygame.mixer.music.stop() 
        self.stop()
        messagebox.showinfo("I am stoped")

    """
    turnright: Funcion que hace que el robot se mueva hacia la derecha
    E: self
    S: Mensaje de movimiento hacia la derecha y el movimiento
    R: No aplica
    """
    def turnright(self): 
        
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("derecha.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("derecha 1.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()

        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()

        messagebox.showinfo("","I am turning right")

    """
    turnleft: Funcion que hace que el robot gire hacia la izquierda
    E: self
    S: Mensaje de giro hacia la izquierda y el giro
    R: No aplican
    """
    def turnleft(self): 
             
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("izquierda.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)

        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()

        messagebox.showinfo("","I am turning right")

    #Funcion que hace que el robot de una vuelta completa
    def turnaround(self): # falta logica de validacion para las imagenes
                
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG = Label(self.ventana_robot, image = self.robot1)
        self.IMG.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("izquierda.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("derecha.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("derecha 1.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("derecha.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()
        time.sleep(0.05)
        self.robot1 = Imagenes("normal.png",(400,400))
        self.IMG2 = Label(self.ventana_robot, image = self.robot1)
        self.IMG2.place(x = 200, y = 300)
        self.ventana_robot.update()

        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()

        messagebox.showinfo("","I am turning around")
    #Funcion que hace que el robot baile
    def dance(self): #Faltan las imagenes que simularan el movimiento
        for i in range(4):
            self.forward(100)
            self.right(90)
        self.Stop()
        print("I am dancing")

    """
    music_on: Funcion que hace que el robot reproduzca musica
    E: self
    S: Reproduccion de musica
    R: No aplica
    """
    def music_on(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/Welcome to the Jungle.mp3')
        pygame.mixer.music.play(-1)
        messagebox.showinfo("","I am playing music")

    """
    music_off: Funcion que hace que el robot deje de reproducir musica
    E: self
    S: No reproduccion de musica
    R: No aplica
    """
    def music_off(self): 
        pygame.mixer.music.stop()
        messagebox.showinfo("","I am stop playing music")
    
    """
    light_on: Funcion que hace que el robot nos diga que esta listo para jugar
    E: self
    S: Mensaje de listo para jugar
    R: No aplica
    """
    def light_on(self):
        self.Good_morning()
    
    """
    light_off: Funcion que hace que el robot nos diga que se va a dormir
    E: self
    S: Mensaje de que se va a dormir
    R: No aplica
    """
    def light_off(self):
        messagebox.showinfo("","I am turning off the light")
        self.Dark()

    """
    smile: Funcion que hace que el robot sonria, tambien dependendiendo de su estado de animo dira una frase distinta
    E: self
    S: Mensaje de animo
    R: No aplica
    """
  
    def smile(self):
      
      robot_info[0][3] = str(int(robot_info[0][3]) + 5)

      pygame.mixer.init()
      pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
      pygame.mixer.music.play()

      messagebox.showinfo("","I am smiling")
      
      self.Indicador = Label(self.ventana_robot, font=("Arial ",20), text="Indicador: " + robot_info[0][3]
             ,height=1,width=15)
      self.Indicador.place(x=300,y=50)

      messagebox.showinfo("","I am very happy")

      if int(robot_info[0][3]) >= 61 and int(robot_info[0][3]) <= 100:
            messagebox.showinfo("","Im  happy")

      elif int(robot_info[0][3]) >= 41 and int(robot_info[0][3]) <= 100:
            messagebox.showinfo("","Im happy, but tired")

      elif int(robot_info[0][3]) <= 40 and int(robot_info[0][3]) >= 0:
            messagebox.showinfo("","Im sad")

      elif int(robot_info[0][3]) > 100:
            robot_info[0][3] = str(int(robot_info[0][3]) - 50)
            messagebox.showinfo("","I am very happy, I dont want to cry")

      elif int(robot_info[0][3]) < 0:
            robot_info[0][3] = str(int(robot_info[0][3]) + 50)
            messagebox.showinfo("","I am very sad, I  want to smile")
      else:
            messagebox.showerror("Error","I dont know how I feel")

    """
    cry: Funcion que hace que el robot llore, tambien dependendiendo de su estado de animo dira una frase distinta
    E: self
    S: Mensaje de animo
    R: No aplica
    """	
    def cry(self): 

        robot_info[0][3] = str(int(robot_info[0][3]) - 5) 

        self.Indicador = Label(self.ventana_robot, font=("Arial ",20), text="Indicador: " + robot_info[0][3]
             ,height=1,width=15)
        self.Indicador.place(x=300,y=50)

        pygame.mixer.init()
        pygame.mixer.music.load('Adicionales/BB-8 sound 2.mp3')
        pygame.mixer.music.play()

        messagebox.showinfo("","I am crying")

        if int(robot_info[0][3]) >= 61 and int(robot_info[0][3]) <= 100:
            messagebox.showinfo("","Im very happy")

        elif int(robot_info[0][3]) >= 41 and int(robot_info[0][3]) <= 100:
            messagebox.showinfo("","Im happy, but tired")

        elif int(robot_info[0][3]) <= 40 and int(robot_info[0][3]) >= 0:
            messagebox.showinfo("","Im sad")

        elif int(robot_info[0][3]) > 100:
            robot_info[0][3] = str(int(robot_info[0][3]) - 50)
            messagebox.showinfo("","I am very happy, I dont want to cry")

        elif int(robot_info[0][3]) < 0:
            robot_info[0][3] = str(int(robot_info[0][3]) + 50)
            messagebox.showinfo("","I am very sad, I  want to smile")    
        else:
            messagebox.showerror("Error","I dont know how I feel")

    """
    Window: Funcion que crea la ventana de la shell, y se le dan algunas carcteristicas como una entrada de texto,
    un boton para ejecutar una funcion y una lista donde se podran ver todos los comandos que se puedan ejecutar
    E: self
    S: Ventana de la shell
    R: No aplica
    """
    def Window1(self):
        
        #Configuracion de la ventana

        self.consola.configure(bg ="dodgerblue4")

        #Esta pare permitira ver los comaandos que se pueden ingresar

        self.ordenes = ttk.Treeview(self.consola)
        self.item1 = self.ordenes.insert("",0,END,text = "Comandos")
        self.ordenes.insert(self.item1,END,text = "sayhello")
        self.ordenes.insert(self.item1,END,text = "built")
        self.ordenes.insert(self.item1,END,text = "forward")
        self.ordenes.insert(self.item1,END,text = "backward")
        self.ordenes.insert(self.item1,END,text = "stop")
        self.ordenes.insert(self.item1,END,text = "turnright")
        self.ordenes.insert(self.item1,END,text = "turnleft")
        self.ordenes.insert(self.item1,END,text = "dance")
        self.ordenes.insert(self.item1,END,text = "music_on")
        self.ordenes.insert(self.item1,END,text = "music_off")
        self.ordenes.insert(self.item1,END,text = "smile")
        self.ordenes.insert(self.item1,END,text = "cry")
        self.ordenes.insert(self.item1,END,text = "turnaround")
        self.ordenes.insert(self.item1,END,text = "light_on")
        self.ordenes.insert(self.item1,END,text = "light_off")


        self.ordenes.pack()
        self.ordenes.place(x= 180, y =250)

        #Esta parte permitira ingresar el comando que se desea ejecutar

        self.Lbl = Label(self.consola, text = "Digite la orden", bg = "DeepSkyBlue2",font = ("Arial", 20))
        self.Lbl.place(x = 170, y = 50)

        self.Comando = Entry(self.consola, width = 10, bg = "DeepSkyBlue4",font = ("Arial Ce",20))
        self.Comando.place(x = 190, y = 110)
    
        self.Aceptar = Button(self.consola, text = "Aceptar", bg = "DeepSkyBlue4",font = ("Roman",20)
            , command = self.Validacion)
        self.Aceptar.place(x = 220, y = 170)

    """
    Validacion: Funcion que valida que el comando ingresado sea correcto
    E: self
    S: Mensaje de error o ejecucion del comando
    R: No aplica
    """
    def Validacion(self):
        escribirR()
        self.comando = self.Comando.get()
    
        if self.comando == "sayhello": #Comando que hace que el robot diga hola
                self.sayhello()

        elif self.comando == "built": #Comando que hace que el robot diga el dia de su creacion
                self.built()

        elif self.comando == "forward":
                self.forward()

        elif self.comando == "backward":
                self.robot.backward()

        elif self.comando == "stop": #Comando que hace que el robot se detenga
                self.Stop()

        elif self.comando == "turnright":
                self.turnright()

        elif self.comando == "turnleft":
                self.turnleft()

        elif self.comando == "turnaround":
                self.turnaround()

        elif self.comando == "dance": #Comando que hace que el robot baile
                self.dance()

        elif self.comando == "music_on": #Comando que hace que el robot reproduzca musica
                self.music_on()

        elif self.comando == "music_off": #Comando que hace que el robot deje de reproducir musica
                self.music_off()

        elif self.comando == "light_on": #Comando que hace que el robot encienda la luz
                self.light_on()

        elif self.comando == "light_off": #Comando que hace que el robot apague la luz
                self.light_off()

        elif self.comando == "smile": #Comando que hace que el robot se sonria
                self.smile()

        elif self.comando == "cry": #Comando que hace que el robot se ponga triste
                self.cry()
        else:
                messagebox.showinfo("Error"," I dont understand")

#Parte final del codigo, aqui se implementa las condiciones para abri y cerrar la simulacion, ademas tambien se establece 
                #las funciones que se ejecutaran al mismo tiempo que el codigo

"""
Atributos o funciones en inicializarse al ejecutar el codigo
"""
leerRobot() #Se habre el archivo donde se encuentra la informacion del robot

"""
Funcion que cierra ambas ventanas cuando se cumple cierta condicion
"""
def close (): 
    escribirR() #Antes de cerrar la ventana se escribe en el archivo
    window.destroy() #Se cierra la ventana principal o donde se encuentra el robot
    shell.destroy() #Se cierra la ventana de la shell

"""
Lo que se ejecuta apenas se corre el codigo de las clases
"""

#Ventana principal
window = Tk()
window.geometry('800x700+0+0') #Tamaño de la ventana
window.title("Robot Simulator") #Titulo de la ventana
window.iconbitmap('Adicionales/robot.ico') #Añade un icono distinto
window.resizable(False,False) #No permite cambiar el tamaño de la ventana

#Ventana de la consola
shell = Tk()
shell.geometry('550x700+800+0') #Tamaño de la ventana
shell.title("Shell Robot") #Titulo de la ventana
shell.iconbitmap('Adicionales/robot.ico') #Añade un icono distinto
shell_simulation = Robot(robot_info[0][0],robot_info[0][1],robot_info[0][2],robot_info[0][3],window,shell) #Ventana de simulacion
shell.resizable(False,False) #No permite cambiar el tamaño de la ventana

#Condicion para que se cierre la ventana, nos permite cerrar las dos ventanas al mismo tiempo
window.protocol ("WM_DELETE_WINDOW", close) #Si se cierra la ventana window, se cierra la ventana shell
shell.protocol ("WM_DELETE_WINDOW", close) # Si se cierra la ventana shell, se cierra la ventana window
 
mainloop()



 

