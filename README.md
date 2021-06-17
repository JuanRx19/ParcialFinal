# ParcialFinal

#### El problema se da en las cafeterías de la universidad Javeriana Cali, ellas están dando unos descuentos a los estudiantes y profesores para recuperarse un poco del tiempo de cuarentena que no estuvieron laborando, a los profesores les están dando un 20% de descuento y a los estudiantes un 50%. Así que ellas les pidieron ayuda a los estudiantes de Ingeniería de Sistemas de la Universidad que les ayudaran con un programa donde los estudiantes y profesores puedan hacer su propio check-out de la cafetería sin la ayuda del personal de las cafeterías. Lo primero que el programa debe preguntarle al usuario es la cédula y el rol de él, es decir si es profesor o estudiante, seguidamente se le preguntaran datos sobre el o los productos que ellos desean llevar, entonces se les preguntaría primero por el código del producto, luego la cantidad de unidades que llevan de este producto, después por el precio y al final se le pregunta si desea llevar más productos o no.

#### Nosotros para darle solución al problema decidimos usar el lenguaje de Phyton y usamos como editor Visual Studio Code. Nuestro programa mediante varias entradas de texto y datos numéricos le pedí paulatinamente la información que se necesita del usuario y productos, el orden y lo que se pide en estas entradas es:

* Datos del usuario
  1. Cédula (solo se deben ingresar los números en caso de que sea una cédula de extranjería).
  2. Rol: se le pide al usuario que escoja entre 1 o 2, donde 1 es profesor y 2 es estudiante.
* Datos de los productos que el usuario desea llevar
  1. Código del producto: se debe ingresar el código del producto a facturar (solo puede ser números). 
  2. Nombre del producto: el usuario debe ingresar el nombre del producto a facturar.
  3. Cantidad: se debe ingresar cuantos productos del producto que se está facturando desea llevar el usuario (se permite solo ingreso de datos numéricos). 
  4. Precio del producto: el usuario debe ingresar el valor unitario del producto a facturar (se permite solo datos numéricos, y pueden ser decimales o enteros). 
  5. Productos adicionales: se le pregunta al usuario si desea llevar y registrar más productos, el usuario debe digitar 1 en caso de que si lo desee, o en caso contrario 2. 

#### Las salidas de nuestro programa consiste en varias líneas, la primera le informa al usuario si es profesor o usuario y el número de la cédula, seguidamente se imprimen tres líneas donde se menciona el código, el nombre y la cantidad del primer o el único producto que se registró, si se lleva más de un producto se vuelve a repetir estas tres últimas líneas, de lo contrario o cuando se termine de imprimir todos los productos se visualizara el total a pagar por él o los productos.

#### Para calcular el total a pagar lo que hicimos nosotros fue mediante el programa y los datos de entrada, cogimos los datos del precio del producto y la cantidad que el usuario está llevando de cada producto y los multiplicamos, luego en caso de que el usuario este llevando más productos se hace lo mismo y por medio de una variable vamos sumando el dato nuevo con el producto anterior. Por último, de acuerdo al rol del usuario se le resta al total un 50% o 20%.

#### El programa que nosotros desarrollamos y que le da solución a este problema está en el archivo Parcial final - Laura Rojas y Juan Miguel Rojas.py, y en el archivo Parcial final - Laura Rojas y Juan Miguel Rojas.txt describimos algunos de los problemas que tuvimos en el desarrollo de este programa y la solución que le dimos a estos. 
