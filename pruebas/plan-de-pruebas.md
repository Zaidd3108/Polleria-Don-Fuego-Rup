# Plan de Pruebas - Versión 1.1

## Proyecto: Pollería Don Fuego S.A.C.

---

## 1. Información General
* **Proyecto:** Pollería Don Fuego S.A.C.
* **Autor / Responsable:** Kenneth Zaidd Machacuay Maldonado (N00478549)
* **Versión del Sistema:** v1.1 (Línea Base Actualizada)
* **Fecha:** Noviembre de 2026

---

## 2. Alcance del Plan de Pruebas
El presente documento describe la estrategia, el entorno y los casos de prueba ejecutados para validar el correcto funcionamiento del sistema web y de gestión de Pollería Don Fuego S.A.C., abarcando tanto los flujos base (`v1.0`) como las incorporaciones y correcciones de la versión `v1.1`:
* **CR-001:** Cálculo automatizado del costo de envío por zona geográfica en el total del delivery (`HU-15`, `CU-09`).
* **CR-002:** Formalización del Caso de Uso de entrega de pedidos en local (`CU-10`, `HU-08`).

---

## 3. Estrategia de Pruebas
* **Pruebas Funcionales:** Validación de historias de usuario, casos de uso y cálculo de tarifas de envío.
* **Pruebas de Integración:** Verificación de la comunicación entre la pasarela de pedidos, el módulo de delivery y la base de datos de zonas de cobertura.
* **Pruebas de Trazabilidad:** Auditoría automatizada de cobertura mediante el script `reporte_trazabilidad.py` (alcanzando el **100% de cobertura** en requisitos, casos de uso, clases y pruebas).

---

## 4. Casos de Prueba (Resumen de Ejecución v1.1)

| Código | Descripción de la Prueba | Requisito Asociado | Resultado Esperado | Estado |
| :--- | :--- | :--- | :--- | :--- |
| **PR-01 / PR-02** | Registro correcto de pedidos y detalles | HU-01 | Almacenamiento exitoso del pedido | **Aprobado** |
| **PR-03 / PR-04** | Validación de stock disponible | HU-02 | Restricción si no hay stock | **Aprobado** |
| **PR-05 / PR-06** | Registro de datos de delivery | HU-03 | Captura correcta de dirección y zona | **Aprobado** |
| **PR-07 / PR-08** | Cálculo del subtotal y confirmación | HU-04 | Suma exacta de productos | **Aprobado** |
| **PR-09** | Generación de ticket y orden a cocina | HU-05 | Envío simultáneo a terminal de cocina | **Aprobado** |
| **PR-10** | Verificación de insumos en inventario | HU-06 | Validación de stock de insumos | **Aprobado** |
| **PR-11** | Control de calidad del pedido en preparación | HU-07 | Cambio de estado en cocina | **Aprobado** |
| **PR-12** | Entrega de pedido en el local (Mostrador) | HU-08 / CU-10 | Cierre de orden por recojo en tienda | **Aprobado** |
| **PR-13** | Despacho de pedido por delivery | HU-09 | Asignación de motorizado y ruta | **Aprobado** |
| **PR-14** | Gestión de incidencias de pedidos no entregados | HU-10 | Registro de devolución o reprogramación | **Aprobado** |
| **PR-15 / PR-16** | Cobro del pedido y pasarela de pago | HU-11 | Procesamiento de pago exitoso | **Aprobado** |
| **PR-17 / PR-18** | Emisión de comprobante electrónico | HU-12 | Generación de boleta/factura | **Aprobado** |
| **PR-19** | Registro de ingresos en libro de caja | HU-13 | Asiento contable automático | **Aprobado** |
| **PR-20** | Cuadre diario de caja | HU-14 | Balance general de turnos | **Aprobado** |
| **PR-21** | Validación de zona de cobertura (CR-001) | HU-15 | Identificación correcta de distrito/paradero | **Aprobado** |
| **PR-22** | Cálculo dinámico de tarifa de envío (CR-001) | HU-15 | Suma correcta del recargo al total del pedido | **Aprobado** |
| **PR-23** | Integración de reglas de envío y facturación | HU-04 / HU-12 | Coherencia en comprobante con tarifa de zona | **Aprobado** |
| **PR-24** | Control de flujos presenciales en mostrador | HU-08 / CU-10 | Trazabilidad del `CU-10` sin brechas | **Aprobado** |

---

## 5. Criterios de Aceptación y Conclusión
* El sistema cumple con todas las especificaciones de la metodología RUP.
* Se valida una **cobertura del 100%** en la matriz de trazabilidad (`matriz_v1.1.csv`).
* El plan de pruebas se declara **Aprobado** para la liberación oficial de la etiqueta **v1.1** en el repositorio.