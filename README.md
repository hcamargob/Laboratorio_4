# Laboratorio 4: Cinemática Directa - Phantom X - ROS
<p align="center">
ROBÓTICA

<p align="center">
Hugo Alejandro Camargo Barrera
<p align="center">
email: hcamargob@unal.edu.co

<p align="center">
Santiago Hernández Lamprea
<p align="center">
email: shernandezl@unal.edu.co


<p align="center">
INGENIERÍA MECATRÓNICA
<p align="center">
Facultad de Ingeniería
<p align="center">
Universidad Nacional de Colombia Sede Bogotá

Para cumplir satisfactoriamente los requerimientos y tareas propuestas, se siguió el siguiente proceso:

### 1) Familiarización con el Phantom X


![image](https://user-images.githubusercontent.com/112737454/196834382-76eb4269-14da-4f22-9edf-22de416b5bbd.png)

El primer acercamiento al robot _Phantom\_X_ se realizó con el software _Dynamixel_. Se modificó cada articulación y se fijo la opción de torque para que se mantuviera fija la articulación. Esta primera interacción fue satisfactoria y nos dió pie para arrancar la comunicación de ROS con Phyton.

Al mismo tiempo se hizo el análisis DH del robot, del cual se obtuvo:

 ![Copia de Captura de pantalla 2022-10-19 203640](https://user-images.githubusercontent.com/112737454/196844235-8237576e-d5fe-4d32-89fc-ddba99498485.jpg)

 
Con este análisis podemos comparar las posiciones obtenidas con el robot a las obtenidas en MatLab con la librería de Peter Corke.
 
### 2) Conexión con Dynamixel 
  
  El primer paso fue la instalación de Dynamixel para la conexión del Robot con el PC. Para esto, se siguió el repositorio https://github.com/fegonzalez7/rob_unal_clase3, donde se explica, paso a paso, la instalación de Dynamixel Workbench. Este fue el resultado de la instalación:
  
![image](https://user-images.githubusercontent.com/112737454/196839807-f111c32f-55f5-4caa-89ce-e17673230d8a.png)
  
  Ya con el Dynamixel instalado, se hizo la conexión con el robot
  
  ![image](https://user-images.githubusercontent.com/112737454/196839992-92d64318-56f6-4ab4-8923-893001d4ef26.png)
  
![image](https://user-images.githubusercontent.com/112737454/196840064-a59cb4f8-246d-4c97-80fe-d7a4d7f12a4a.png)

  Finalmente, se obtiene:
  
  ![image](https://user-images.githubusercontent.com/112737454/196840206-6953ba82-a47c-4807-87ef-b14ee152394e.png)

 ### 3) Toolbox de MatLab
 
 ### 4) Conexión entre Python y ROS. Ejecución de las secuencias en el robot.
 Para hacer la conexión, se arranca el ROS y se crea un nodo. Despues se arranca eldinamyxel con ROS:
 ```
 roslaunch dynamixel_one_motor one_controller.launch
 ```
 
 
 ### 5) Comparación del Toolbox y del Phantom_X
 
