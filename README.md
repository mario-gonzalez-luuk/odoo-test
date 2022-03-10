# odoo-test
## Test tecnico odoo developer 

Modulo para extender la funcionalidad del modelo Sale Order donde automaticamente se asigna una orden al empleado siguiendo la siguiente lista de condiciones:

1. Se asignara la orden al empleado disponible (Available) con menor numero de ordenes asignadas
2. Si no encuentra a nadie en el paso 1, se asignara la orden al empleado ocupado (Busy) con menor numero de ordenes asignadas
3. Si no encuentra a nadie en el paso 2, se asignara la orden al cualquier empledo (Offline) con menor numero de ordenes asignadas 
4. En dado caso no haya empleados con estado asignado (Available, Busy o Offline) se levanta un error de validacion indicando que no hay empleados que manejen la orden. 

## Referencias

El menu donde se podra ingresar a las vistas personalizadas del Sale Order:

(Perspectiva del usuario)

![image](https://user-images.githubusercontent.com/99834889/157718011-45e637b3-a458-4e25-be22-0ba9f8a97f62.png)

(Perspectiva del admin)

![image](https://user-images.githubusercontent.com/99834889/157719336-b2691715-ec0e-4501-a8ad-a77a8f2e11ba.png)

El lugar donde se puede seleccionar el estado en el formulario del empleado: Formulario Empleado -> Sales -> Employee Status

Ademas puede observar la cantidad de ordenes asignadas al respectivo empleado

![image](https://user-images.githubusercontent.com/99834889/157718750-b859be08-1a3d-4439-8f29-6ddb634ca090.png)
