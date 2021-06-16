# termux-builder
Build simple .deb packages for termux

## Que es termux-builder? 

Termux builder es un conjunto de simples scripts 
para la creación de paquetes .deb para termux.

## Instalación :

```
# instalamos las dependencias necesarias 
pkg install git python
# Clonamos este repositorio 
git clone https://github.com/Yisus7u7/termux-builder
```

## Como usarlo? 

Su uso es simple ingresa a la carpeta termux-builder, usa el comando :

```
./gen.sh  #para crear un nuevo proyecto
```

Y use 

```
./build.py example.deb 
# cambie example.deb por el nombre del paquete que desea construir
```

### Como funciona?
Termux-builder genera un boostrap minimo
Solo debe editar la información de su paquete en
`./termux_pkg/DEBIAN/control`, ahí debe definir la
información de su paquete.

```
Package: hello-example  #nombre se su paquete, solo minúsculas y números, no use espacios. 
Version: 1.0.0  #versión de su paquete 
Priority: optional  #prioridad (es mejor no cambiar eso) 
Architecture: all  #arquitectura compatibles con su paquete, all es compatible con todas
Depends: python, php, openssh  #dependencias que su paquete necesita para funcionar 
Installed-Size: 2300  #peso de su paquete, el valor debe ser equivalente a Kb
Maintainer: @Yisus7u7 <jesuspixel5@gmail.com>  #su nombre, correo electrónico opcional
Homepage: https://github.com/Yisus7u7/termux-builder  #link al código fuente o el lugar de origen del paquete 
Description: This is an example of hello world   #descripción de su paquete 

```

Con eso definimos la información del paquete, 
Ahora ingrese sus archivos en la carpeta `./termux_pkg/data/data/com.termux/files/usr/`
En esa ubicación se encuentran las carpetas, sea creativo, 
guarde los ejecutables en bin y los datos de su programa en share, 
le recomiendo borrar las carpetas vacias que no use. 

Luego de eso use :

```
./build.py hello-example_1.0.0_all.deb
# Nota : cambie "hello-example" por el nombre de su paquete, 
# cambie "1.0.0" por la versión y cambie "all" por la arquitectura 
# que usted haya especificado. 
```

Luego podrá instalar el paquete con :

`pkg install ./package_name.deb`

También puede hacer cosas geniales como crear un 
repositorio de paquetes .deb similar a los de termux, 
donde el usuario debe solo ejecutar `pkg install app_name`
para instalar sus paquetes, un ejemplo de repositorio 
apt es [este repositorio.](https://pkgs-yisus.github.io/pkgs.yisus.org/)

### Enlaces de referencia 🔗

- [termux-apt-repo](https://github.com/termux/termux-apt-repo)
- [termux-create-package](https://github.com/termux/termux-create-package)
- [mi repositorio comunitario de paquetes](https://pkgs-yisus.github.io/pkgs.yisus.org/)
- [wiki de debían](https://wiki.debian.org/Packaging/Intro)


## Contribuir

- Puede hacer solicitudes de extracción sobre errores
o mejoras útiles.

- Si quiere reportar un error, hacer una pregunta
o solicitar una función, [cree el problema aquí](https://github.com/Yisus7u7/termux-builder/issues) 


Comparte esto con tus amigos y deja tu 🌟, 
Espero que te guste este proyecto. 
