# Procesos de Negocio - Pollería Don Fuego S.A.C.

## 1. Introducción
El presente documento describe los procesos de negocio fundamentales del sistema de gestión para **Pollería Don Fuego S.A.C.** bajo el marco de la metodología RUP (Rational Unified Process). Define los flujos operativos desde la toma de pedidos hasta la entrega final al cliente, integrando las actualizaciones de la línea base **v1.1** (como el cálculo de delivery por zonas y la entrega en local).

---

## 2. Actores del Negocio
* **Cliente:** Usuario final que realiza pedidos de forma presencial o a través del canal digital (delivery/recojo).
* **Cajero:** Responsable de registrar pedidos, procesar pagos, emitir comprobantes electrónicos y realizar el cuadre de caja.
* **Cocinero / Operario de Cocina:** Encargado de verificar insumos, preparar los platos solicitados y controlar los tiempos y calidad de salida.
* **Motorizado (Repartidor):** Encargado de la distribución y entrega de pedidos a domicilio según las zonas de cobertura.
* **Administrador:** Supervisor encargado de gestionar tarifas, reportes de ventas, trazabilidad y control general del sistema.

---

## 3. Procesos Principales del Negocio

### Proceso 1: Gestión de Pedidos y Ventas (`E-01`)
* **Descripción:** Abarca la interacción inicial del cliente con el sistema para registrar sus requerimientos.
* **Flujo Operativo:**
  1. El cliente selecciona los productos del menú (pollos a la brasa, complementos, bebidas).
  2. El sistema valida la disponibilidad de stock en tiempo real (`HU-02`).
  3. Si es un pedido por delivery, se registran los datos de entrega y se calcula de forma automatizada la tarifa de envío según la zona geográfica (`HU-03` / `HU-15` / `CR-001`).
  4. Se calcula el subtotal y se confirma la orden (`HU-04`).

### Proceso 2: Preparación y Control de Cocina (`E-02`)
* **Descripción:** Gestión de la producción culinaria tras la confirmación de la venta.
* **Flujo Operativo:**
  1. El sistema genera el ticket de venta y envía la orden electrónica al terminal de cocina (`HU-05`).
  2. El cocinero verifica la existencia de insumos necesarios en el inventario (`HU-06`).
  3. Se ejecuta la preparación del pollo a la brasa y platos asociados bajo estrictos estándares de control de calidad (`HU-07`).

### Proceso 3: Despacho y Entrega (`E-02`)
* **Descripción:** Manejo de la entrega del producto final al cliente, ya sea en local o en domicilio.
* **Flujo Operativo:**
  * **Opción A (Recojo en Local):** El cliente recibe su pedido directamente en el mostrador del establecimiento (`HU-08` / `CU-10` / `CR-002`).
  * **Opción B (Delivery):** Se asigna el pedido al motorizado, gestionando la ruta y el despacho a domicilio (`HU-09`).
  * En caso de incidencias (cliente ausente o dirección errónea), se procesa la gestión de pedidos no entregados (`HU-10`).

### Proceso 4: Facturación, Cobro y Cuadre de Caja (`E-03`)
* **Descripción:** Cierre financiero de las transacciones diarias.
* **Flujo Operativo:**
  1. El cajero procesa el cobro del pedido mediante pasarelas de pago o efectivo (`HU-11`).
  2. Se emite el comprobante electrónico correspondiente (boleta o factura) (`HU-12`).
  3. El sistema registra automáticamente el ingreso en el libro de caja diario (`HU-13`).
  4. Al finalizar la jornada, se efectúa el cuadre y arqueo de caja general (`HU-14`).

---

## 4. Alineación y Trazabilidad (Versión v1.1)
Los procesos descritos en este documento se encuentran plenamente trazados en la **Matriz de Trazabilidad v1.1** (`trazabilidad/matriz_v1.1.csv`), garantizando que cada historia de usuario y caso de uso mantenga un vínculo directo con las clases de diseño y los casos de prueba ejecutados.