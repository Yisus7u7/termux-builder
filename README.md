# termux-builder
Build simple .deb packages for termux

![image](https://opengraph.githubassets.com/91871daab983cd69e18846c4f5c40a547e91638b3fe6064d81d9bb4574d95e73/Yisus7u7/termux-builder) 

## Que es termux-builder? 

Termux builder es un conjunto de simples scripts 
para la creación de paquetes .deb para termux.

## Instalación :

```bash
# instalamos las dependencias necesarias 
pkg install git python
# Clonamos este repositorio 
git clone https://github.com/Yisus7u7/termux-builder
```

## Como usarlo? 

Su uso es simple ingresa a la carpeta termux-builder, usa el comando :

```bash
./gen.sh  #para crear un nuevo proyecto
```

Y use 

```bash
./build.py 
# para construir el paquete 
```

### Como funciona?
Termux-builder genera un boostrap minimo
Solo debe editar la información de su paquete en
`pkg_info.py`, ahí debe definir la
información de su paquete.

edite pkg_info.py:

`nano pkg_info.py` 

puede usar su editor de texto de preferencia 

```python
#insert your termux pkg info
# nombre de tu paquete, ej:

TERMUX_PKG_NAME="my_hello_app"

# versión de tu paquete, ej:

TERMUX_PKG_VERSION="1.0.0"

# enlace a página o fuente de tu paquete, ej:

TERMUX_PKG_HOMEPAGE="https://pkgs-yisus.github.io/pkgs.yisus.org/"

# descripción de tu paquete ej:
#nota : la descripción debe ocupar sólo una línea. 

TERMUX_PKG_DESCRIPTION="esto es un ejemplo de hello world"

# dueño/mantendor del paquete, ej:

TERMUX_PKG_MAINTAINER="@Yisus7u7 <jesuspixel5@gmail.com>"

# dependencias de tu paquete, ej:

TERMUX_PKG_DEPENDS="python, openssh, php"

# el tamaño de tu paquete 
# Nota: el valor debe equivaler a KB
#ej: 1000 = 1MB | 1000 es igual a 1000 kB y 1000kb es igual a 1MB

TERMUX_PKG_SIZE="2100"

# la arquitectura que donde solo tu paquete puede ejecutarse
# nota : usa all para que sea comptible con todos los dispositivos 
# si tu paquete usa clang o c++ o lenguajes
# que requieren compilación, debe usar los valores
# (arm, aarch64, x86_64)

TERMUX_PKG_ARCH="all"

# end

```

Con eso definimos la información del paquete, 
Ahora ingrese sus archivos en la carpeta 

`./termux_pkg/data/data/com.termux/files/usr/`

En esa ubicación se encuentran las carpetas, sea creativo, 
guarde los ejecutables en bin y los datos de su programa en share, 
le recomiendo borrar las carpetas vacias que no use. 

Luego de eso use :

```bash
./build.py 

# se generará su paquete .deb
```

Luego podrá instalar el paquete con :

`pkg install ./package_name.deb`

También puede hacer cosas geniales como crear un 
repositorio de paquetes .deb similar a los de termux, 
donde el usuario debe solo ejecutar `pkg install app_name`
para instalar sus paquetes, un ejemplo de repositorio 
apt es [este repositorio.](https://pkgs-termux.github.io/pkgs.org)

### Enlaces de referencia 🔗

- [termux-apt-repo](https://github.com/termux/termux-apt-repo)
- [termux-create-package](https://github.com/termux/termux-create-package)
- [mi repositorio comunitario de paquetes](https://pkgs-termux.github.io/pkgs.org)
- [wiki de debían](https://wiki.debian.org/Packaging/Intro)


## Contribuir

- Puede hacer solicitudes de extracción sobre errores
o mejoras útiles.

- Mejorar esta página (aspecto, información) 

- Si quiere reportar un error, hacer una pregunta
o solicitar una función, [cree el problema aquí](https://github.com/Yisus7u7/termux-builder/issues) 


Comparte esto con tus amigos y deja tu 🌟, 
Espero que te guste este proyecto. 
