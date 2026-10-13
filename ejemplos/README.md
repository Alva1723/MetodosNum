curso: unidad de enseñanza-aprendizaje y clave,
trimestre, licenciatura que cursa, su nombre completo, su matrícula, el nombre del profesor y la
fecha.

# Metodos Numericos En Ingeniería CTG06
# 26O
# Ingenieria Electrica
# Alejandro Aldair Alvarez Alarcon 2193044854
# GABRIEL HURTADO AVILES 
# 12/01/2026 



# Introducción a los Métodos Numéricos

## 1. ¿Qué son los métodos numéricos?

Los métodos numéricos son técnicas matemáticas que permiten obtener soluciones aproximadas a problemas que no pueden resolverse de manera exacta o cuya solución analítica resulta demasiado compleja. Estos métodos transforman problemas matemáticos en una secuencia de operaciones aritméticas que pueden ejecutarse en una computadora. Son ampliamente utilizados en ciencia e ingeniería para resolver ecuaciones, sistemas de ecuaciones lineales, problemas de interpolación, integración, derivación y ecuaciones diferenciales.

La principal diferencia entre una solución analítica y una solución numérica es que la solución analítica proporciona una expresión matemática exacta, mientras que la solución numérica genera una aproximación de la respuesta. Debido a que los métodos numéricos trabajan con aproximaciones sucesivas y con una cantidad finita de operaciones, los resultados obtenidos contienen errores asociados al truncamiento y al redondeo.

El error desempeña un papel fundamental en los métodos numéricos, ya que permite evaluar qué tan cercana es una aproximación respecto al valor real. Por esta razón, gran parte del análisis numérico se enfoca en desarrollar algoritmos que reduzcan el error y mejoren la estabilidad y precisión de los cálculos.

**Referencias del apartado**

Burden y Faires (2011) explican que los métodos numéricos se utilizan para obtener aproximaciones computacionales de problemas matemáticos cuya solución exacta es difícil o imposible de calcular. Asimismo, Chapra y Canale (2015) destacan la importancia del análisis del error como parte esencial de cualquier procedimiento numérico.

**Citas APA 7 dentro del texto:** (Burden & Faires, 2011; Chapra & Canale, 2015)

---

## 2. Aplicación de los métodos numéricos en la Ingeniería Eléctrica

Mi licenciatura es **Ingeniería Eléctrica**. En esta área los métodos numéricos son indispensables debido a la complejidad de los sistemas eléctricos modernos, los cuales suelen involucrar grandes cantidades de variables y ecuaciones que no pueden resolverse mediante fórmulas cerradas.

### Problema 1: Flujo de potencia en sistemas eléctricos

Uno de los problemas más importantes consiste en determinar los voltajes, corrientes y potencias que circulan en una red eléctrica. Para ello se utilizan métodos iterativos como Newton-Raphson o Gauss-Seidel, ya que las ecuaciones involucradas son no lineales y pueden incluir decenas o cientos de nodos. Una fórmula simple no es suficiente debido a la complejidad de las interacciones entre los distintos elementos de la red.

### Problema 2: Análisis de sistemas transitorios

Otro problema frecuente es el estudio de fenómenos transitorios en líneas de transmisión, transformadores y sistemas de potencia. Estos fenómenos se describen mediante ecuaciones diferenciales que normalmente no poseen una solución analítica sencilla. Por ello se emplean métodos numéricos para aproximar la evolución temporal de las variables eléctricas y predecir el comportamiento del sistema bajo diferentes condiciones de operación.

De acuerdo con Chapra y Canale (2015), muchos problemas de ingeniería requieren algoritmos numéricos debido a la imposibilidad práctica de obtener soluciones exactas. De manera similar, Nieves y Domínguez (2014) muestran aplicaciones de métodos numéricos en diversas ramas de la ingeniería para resolver modelos matemáticos complejos.

**Citas APA 7 dentro del texto:** (Chapra & Canale, 2015; Nieves & Domínguez, 2014)

---

## 3. Herramientas utilizadas en métodos numéricos

El desarrollo y aplicación de métodos numéricos requiere herramientas computacionales que permitan implementar algoritmos de forma eficiente. Entre las principales familias de herramientas se encuentran:

### Lenguajes compilados

Los lenguajes compilados como **C**, **C++** y **Fortran** son ampliamente utilizados debido a su alta velocidad de ejecución y control sobre los recursos del sistema. Son especialmente útiles para simulaciones científicas y aplicaciones de alto desempeño.

### Lenguajes interpretados

Lenguajes como **Python** facilitan el desarrollo rápido de algoritmos gracias a su sintaxis sencilla y gran cantidad de bibliotecas disponibles para el cálculo científico.

### Entornos matriciales

**MATLAB** y **GNU Octave** ofrecen herramientas especializadas para trabajar con matrices, resolver sistemas de ecuaciones, realizar análisis de datos y visualizar resultados de manera eficiente.

### Python científico

Bibliotecas como **NumPy**, **SciPy** y **Matplotlib** permiten realizar cálculos numéricos avanzados, resolver problemas científicos y generar gráficos de alta calidad.

### Álgebra simbólica

Herramientas como **Mathematica**, **Maple** o el Symbolic Toolbox de MATLAB ayudan a manipular expresiones algebraicas de forma exacta antes de recurrir a aproximaciones numéricas.

### Bibliotecas de base

Bibliotecas como **BLAS** (Basic Linear Algebra Subprograms) y **LAPACK** (Linear Algebra Package) proporcionan rutinas optimizadas para operaciones matriciales y constituyen la base de muchas aplicaciones científicas modernas.

### Herramientas utilizadas por los libros consultados

- **Burden y Faires (2011):** presentan algoritmos generales que pueden implementarse en lenguajes como C, C++ o MATLAB.
- **Chapra y Canale (2015):** emplean ampliamente MATLAB para ilustrar procedimientos numéricos aplicados a la ingeniería.
- **Nieves y Domínguez (2014):** utilizan ejemplos computacionales aplicables a MATLAB y otros entornos de programación científica.
- **Quarteroni y Saleri (2009):** se enfocan específicamente en el uso de MATLAB y GNU Octave para el cálculo científico.

**Citas APA 7 dentro del texto:** (Burden & Faires, 2011; Chapra & Canale, 2015; Quarteroni & Saleri, 2009)

---

## 4. Herramientas utilizadas en el curso

### Docker

Docker es una plataforma que permite empaquetar aplicaciones junto con todas sus dependencias dentro de contenedores. Esto asegura que el software se ejecute de manera consistente en diferentes sistemas operativos y entornos de trabajo.

### Docker frente a una máquina virtual

Una máquina virtual emula un sistema operativo completo, incluyendo su propio kernel, mientras que Docker comparte el kernel del sistema anfitrión. Como resultado, los contenedores suelen consumir menos recursos y arrancar mucho más rápido que las máquinas virtuales.

### Dockerfile, compose.yaml y comandos básicos

El archivo `Dockerfile` contiene las instrucciones necesarias para construir una imagen de Docker. Por otro lado, el archivo `compose.yaml` permite definir y administrar múltiples servicios de manera simple.

Durante el curso se utilizaron los siguientes comandos:

- `docker compose up -d`: inicia los contenedores en segundo plano.
- `docker exec`: ejecuta comandos dentro de un contenedor activo.
- `docker stop`: detiene un contenedor.
- `docker compose down`: elimina contenedores creados por Compose.
- `docker ps`: muestra los contenedores en ejecución.
- `docker logs`: consulta los registros de un contenedor.

Detener un contenedor con `stop` no lo elimina; únicamente finaliza su ejecución. En cambio, `down` elimina los contenedores asociados al proyecto definido en Compose.

### GNU Octave

GNU Octave es un entorno de cálculo numérico de software libre compatible en gran medida con MATLAB. Permite realizar operaciones matriciales, gráficos y simulaciones científicas.


### Python

Python es un lenguaje de programación interpretado ampliamente utilizado en aplicaciones científicas y de ingeniería. Gracias a bibliotecas como NumPy, SciPy y Matplotlib, puede emplearse para resolver problemas numéricos complejos.


### C con GCC


El lenguaje C ofrece gran eficiencia en la ejecución de programas y es ampliamente utilizado para implementar algoritmos numéricos. GCC (GNU Compiler Collection) es uno de los compiladores más populares para este lenguaje.


-----

# Referencias

Burden, R. L., & Faires, J. D. (2011). *Análisis numérico* (9.ª ed.). Cengage Learning.

Chapra, S. C., & Canale, R. P. (2015). *Métodos numéricos para ingenieros* (7.ª ed.). McGraw-Hill Education.

Nieves, A., & Domínguez, F. C. (2014). *Métodos numéricos aplicados a la ingeniería*. Grupo Editorial Patria.

Quarteroni, A., & Saleri, F. (2009). *Cálculo científico con MATLAB y Octave*. Springer.