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
