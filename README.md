# Gestor-de-Usuarios
## Este proyecto es basico ya que se realizo una aplicacion para android con kivymd , da altas , modifica usuarios , los elimina y realiza un login , se conecta a una base de datos creada en SQL

1. Se importan librerias 

[![1.png](https://i.postimg.cc/6QSrPwRs/1.png)](https://postimg.cc/cKRtKpXT)

2. Se le dan propiedades a las cajas de texto e imagen insertada

[![2.png](https://i.postimg.cc/nzBDwmp7/2.png)](https://postimg.cc/R6ChWN3V)
[![3.png](https://i.postimg.cc/VNbrdtST/3.png)](https://postimg.cc/R34VYNLQ)

3. Se crea la clase de la aplicacion y se realiza la conexion a la base de datos
- se ingresan los datos en varibles como server , db (base de datos) , usuario , contrasena
- se crea la variable conexion en donde se realiza la conexion con la libreria pyodbc seleccionando el driver y uniendo las demas varibles para que realice la conexion, ademas que se hace global ya que se utiliza en otras funciones

[![4.png](https://i.postimg.cc/g0pYVtNv/4.png)](https://postimg.cc/SnZFqd0s)

4. Funcion login
- se genera un boton con el cual permite cerrar la ventana con la funcion dialog close
- se genar una variable para interactuar con los datos 
- se ejecuta un comando para que la base de datos busque el usuario y contrasena 
- se recuperan los datos de la consulta
- si el usuario no ingreso nada manda el mensaje : tienes que introducir usuario y contrasena

[![5-1.png](https://i.postimg.cc/25XrsjCx/5-1.png)](https://postimg.cc/xkHwH2Jk)

- si el usuario ingresa los datos de un usario exitente manda el mensaje : acceso exitoso

[![5-2.png](https://i.postimg.cc/JhH2hRbx/5-2.png)](https://postimg.cc/gwdDSFtL)

- si el usuario ingresa los datos erroneos manda el mensaje : acceso fallido 

[![5-3.png](https://i.postimg.cc/fLxqx5q0/5-3.png)](https://postimg.cc/dkV9FRYq)

- despues de finalizar las validaciones se ponen en blanco las cajas de texto
- se realiza un commit a la base de datos para que se guarde todo por si se realizo alguna modificacion
- se cierra la base de datos 

[![5.png](https://i.postimg.cc/zG6hqNDq/5.png)](https://postimg.cc/PCbJMB87)

5. Funcion newUser 
- se genera un boton con el cual permite cerrar la ventana con la funcion dialog close
- se genar una variable para interactuar con los datos 
- se ejecuta un comando para que la base de datos busque el usuario 
- se recuperan los datos de la consulta
- si el usuario no ingreso nada manda el mensaje : tienes que introducir usuario y contrasena

[![6-1.png](https://i.postimg.cc/L8KTVjft/6-1.png)](https://postimg.cc/LnDL9Yx5)

- si el usuario existe manda el mensaje : usuario ya existe 

[![6-2.png](https://i.postimg.cc/R0GL98Yd/6-2.png)](https://postimg.cc/PLpwQ6Tv)

- si no existe el usuario ejecuta el comando en la base de datos para insertarlos en la tabla y manda el mensaje : exitoso

[![6-3.png](https://i.postimg.cc/RFD1Jt4n/6-3.png)](https://postimg.cc/dkGZzL7q)

- despues de finalizar las validaciones se ponen en blanco las cajas de texto
- se realiza un commit a la base de datos para que se guarde todo por si se realizo alguna modificacion
- se cierra la base de datos 

[![6.png](https://i.postimg.cc/V6dGhmNn/6.png)](https://postimg.cc/KkhDkXB8)

6. Funcion delUser
- se genera un boton con el cual permite cerrar la ventana con la funcion dialog close
- se genar una variable para interactuar con los datos 
- se ejecuta un comando para que la base de datos busque el usuario 
- se recuperan los datos de la consulta
- si el usuario no ingreso nada manda el mensaje : tienes que introducir usuario y contrasena

[![7-1.png](https://i.postimg.cc/1tGH2XQg/7-1.png)](https://postimg.cc/R60KnMq9)

- si el usuario existe lo elimina y manda el mensaje : exitoso

[![7-2.png](https://i.postimg.cc/XNDG33YX/7-2.png)](https://postimg.cc/bdkNH7bj)

- si el usuario no existe en la tabla manda el mensaje : usuario no existe

[![7-3.png](https://i.postimg.cc/xdR8ZVZf/7-3.png)](https://postimg.cc/VSJzSp1p)

- despues de finalizar las validaciones se ponen en blanco las cajas de texto
- se realiza un commit a la base de datos para que se guarde todo por si se realizo alguna modificacion
- se cierra la base de datos 

[![7.png](https://i.postimg.cc/y8CNYN46/7.png)](https://postimg.cc/ZCjmw45X)

7. Funcion userMod
- se genera un boton con el cual permite cerrar la ventana con la funcion dialog close
- se genar una variable para interactuar con los datos 
- se ejecuta un comando para que la base de datos busque el usuario 
- se recuperan los datos de la consulta
- si el usuario no ingreso nada manda el mensaje : tienes que introducir usuario y contrasena

[![8-1.png](https://i.postimg.cc/MGvZ9f1D/8-1.png)](https://postimg.cc/jWYr55gw)

- si el usuario existe cambia la contrasena del usuario y manda el mensaje : exitoso 

[![8-2.png](https://i.postimg.cc/QM9sQGrY/8-2.png)](https://postimg.cc/3yTPhqN2)

- si el usuario no existe manda el mensaje : usuario no existe

[![8-3.png](https://i.postimg.cc/65MNF5W1/8-3.png)](https://postimg.cc/0bK3wvJp)

- despues de finalizar las validaciones se ponen en blanco las cajas de texto
- se realiza un commit a la base de datos para que se guarde todo por si se realizo alguna modificacion
- se cierra la base de datos 

[![8.png](https://i.postimg.cc/PxQ7Z2NF/8.png)](https://postimg.cc/G89znPFk)

8. Funcion build
- se escoge el color del bg y de los bordes de los botones 
- se crea la variable screen para poder agregar todo como botones, cajas , etiquetas e imagenes
- se crean las variables para tomar las propiedades de las cajas de texto e imagen que se pusieron al inicio
- se crean los botones y se le dan propiedades tambien agregando las funciones que van a realizar al momento de presionarlos 
- se agregan las las cajas , botones, imagenes y etiquetas a la pantalla y la retorna 
- se crea una funcion dialog_close la cual utilizamos para cerrar la ventana 

[![9.png](https://i.postimg.cc/7YWWgCYD/9.png)](https://postimg.cc/3d21hxvb)

###                     ********* Aplicacion *********

[![10.png](https://i.postimg.cc/brM4NdZz/10.png)](https://postimg.cc/0KYVVkG3)

###                     ********* Muestra de datos ingresados *********

[![11.png](https://i.postimg.cc/dtPzXZcB/11.png)](https://postimg.cc/XXLHBJJG)

