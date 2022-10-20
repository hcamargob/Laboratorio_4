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
 Para hacer la conexión, se arranca el ROS para crear un nodo:
 ```
 roscore
 ```
 
 Despues se arranca el Dinamyxel con ROS en otra terminal:
 ```
 roslaunch dynamixel_one_motor one_controller.launch
 ```
 
La carpeta _catkin\_ws_, la cual se instaló en el laboratorio 2, se tiene acceso al paquete del robot, el cual se instaló en el paso 2. Dentro de esta carpeta están los archivos de Python a modificar. 
 Los archivos que se modifican están en la carpeta _config_ dentro del _catkin\_ws_, son _basic.yaml_ y _jointPub.py_
 
 _basic.yaml_:
 
 ```
 # You can find control table of Dynamixel on emanual (http://emanual.robotis.com/#control-table)
# Control table item has to be set Camel_Case and not included whitespace
# You are supposed to set at least Dynamixel ID
joint_1:
  ID: 1
  Return_Delay_Time: 1
joint_2:
  ID: 2
  Return_Delay_Time: 1
joint_3:
  ID: 3
  Return_Delay_Time: 1
joint_4:
  ID: 4
  Return_Delay_Time: 1
joint_5:
  ID: 5
  Return_Delay_Time: 1
  # CW_Angle_Limit: 0
  # CCW_Angle_Limit: 2047
  # Moving_Speed: 512
 ```
 _jointPub.py_:
 
 ```
 import rospy
import math
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
        point = JointTrajectoryPoint()
  

        #
        point.positions = [math.radians(0),math.radians(0),math.radians(0),math.radians(0),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('1')
        rospy.sleep(3)

	#
        point.positions = [math.radians(-20),math.radians(20),math.radians(-20),math.radians(20),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('2')
        rospy.sleep(4)

	#
        point.positions = [math.radians(30),math.radians(-30),math.radians(30),math.radians(-30),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('3')
        rospy.sleep(5)
	
        
        #
        point.positions = [math.radians(-90),math.radians(15),math.radians(-55),math.radians(17),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('4')
        rospy.sleep(6)
        
        #
        point.positions = [math.radians(-90),math.radians(45),math.radians(-55),math.radians(45),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('5')
        rospy.sleep(4)
        
        print('published command')
        rospy.sleep(2)

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass
 ```
 
 Se ejecuta esta secuencia en el nodo de conexión de ROS con Python y resultó en:

 [![Watch the video](https://user-images.githubusercontent.com/112737454/196849844-58cc59df-f25b-4c3b-8961-5bf24d616d12.png)](https://www.youtube.com/watch?v=_p8Cu-6cykE)

 
 ### 5) Comparación del Toolbox y del Phantom_X
 
 1. Posición 1 (0, 0, 0, 0, 0)
 
 ![image](https://user-images.githubusercontent.com/112737454/196853903-63e5d1fe-7acd-41f6-a8ef-9686d57a5364.png) ![image](https://user-images.githubusercontent.com/112737454/196854527-f0cb7c1c-369d-4639-96fd-23f023c2e334.png)

2. Posición 2 (-20, 20, -20, 20, 0)
 
 ![image](https://user-images.githubusercontent.com/112737454/196854910-4c3e1e55-25e0-48ae-83f7-bf1af57d7358.png)  ![image](https://user-images.githubusercontent.com/112737454/196854893-c074fdd2-787f-46ea-9f93-80c1fff4951e.png)
 
3. Posición 3 (30, -30, 30, -30, 0) 
 
 ![image](https://user-images.githubusercontent.com/112737454/196855324-d25f97d0-d75f-4367-bd98-569f3ad6942e.png) ![image](https://user-images.githubusercontent.com/112737454/196855186-1cd49bcb-637f-4a97-90cd-b06a190668fa.png)

4. Posición 4 (-90, 15, -55, 17, 0)
 
 ![image](https://user-images.githubusercontent.com/112737454/196855806-80b89cca-7d81-4f7c-acd5-fb10b7a57785.png) ![image](https://user-images.githubusercontent.com/112737454/196855753-27fe0f05-bf9d-4446-aec2-f6534241598f.png)
 
5. Posición 5 (-90, 45, -55, 45, 10)

 ![image](https://user-images.githubusercontent.com/112737454/196856277-e97b2096-7a2d-4945-be33-41f16863d380.png) ![image](https://user-images.githubusercontent.com/112737454/196856232-7af2b448-26b4-4148-b2be-73429d2fe359.png)
