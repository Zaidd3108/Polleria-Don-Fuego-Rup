# Modelo y Especificación de Casos de Uso (CU) - Pollería Don Fuego S.A.C.

**Curso:** Modelado y Desarrollo de Aplicaciones (CIIN1322P)  
**Estudiante:** Kenneth Zaidd Machacuay Maldonado  
**Organización:** Pollería Don Fuego S.A.C.  
**Propósito:** Documentar los Casos de Uso (CU-01 a CU-09), sus actores participantes, el flujo principal y el manejo explícito de excepciones y compensaciones.

---

## 1. Catálogo General de Casos de Uso

| ID | Nombre del Caso de Uso | Actor(es) | RF Asociado | Descripción Breve |
| :--- | :--- | :--- | :--- | :--- |
| **CU-01** | Registrar pedido | Cliente, Cajero | RF-01 | Captura los ítems, cantidades y modalidad de atención (local, teléfono o delivery). |
| **CU-02** | Consultar disponibilidad | Cajero | RF-02 | Verifica en tiempo real si los platos solicitados pertenecen a la carta vigente y tienen stock suficiente. |
| **CU-03** | Modificar o cancelar pedido | Cliente, Cajero | RF-03 | Permite editar ítems o anular la solicitud sin generar cobro antes de confirmar la transacción. |
| **CU-04** | Preparar pedido | Cocinero | RF-04 | Recepciona la comanda digital en cocina y gestiona la cocción de los platos solicitados. |
| **CU-05** | Gestionar faltante | Cocinero, Cajero | RF-05 | Notifica al área de caja sobre la falta repentina de algún insumo durante la preparación. |
| **CU-06** | Gestionar despacho | Cocinero, Repartidor | RF-06 | Coordina la salida del pedido preparado y confirma la entrega final al cliente. |
| **CU-07** | Registrar cobro | Cliente, Cajero | RF-07 | Procesa y valida el pago del pedido mediante el medio elegido por el cliente. |
| **CU-08** | Emitir comprobante | Cajero | RF-08 | Genera e imprime/envía la boleta o factura electrónica por el monto total cobrado. |
| **CU-09** | Anular o reembolsar | Cajero, Administrador | RF-09 | Ejecuta el reembolso parcial o total y la anulación del comprobante ante incidencias en cocina. |

---

## 2. Flujos de Excepción y Compensaciones Modeladas

Para evitar transacciones inconclusas o inconsistencias operativas, los casos de uso críticos contemplan tres flujos de excepción explícitos:

* **Excepción E1 — Producto sin stock o fuera de carta (Vinculado a CU-02 y CU-03):**
  * **Disparador:** El sistema detecta falta de disponibilidad al validar el pedido (`CU-02`).
  * **Compensación:** El Cajero ofrece una alternativa de la carta vigente al Cliente; si el Cliente acepta, se actualiza el pedido (`CU-01`); si rechaza, se cancela el pedido sin generar cobro (`CU-03`).

* **Excepción E2 — Pago rechazado o no válido (Vinculado a CU-07):**
  * **Disparador:** Falla en la validación del medio de pago durante el registro del cobro (`CU-07`).
  * **Compensación:** El sistema permite hasta un máximo de **2 reintentos** con otro medio de pago; si se agotan los intentos, se anula el pedido automáticamente y se libera el stock reservado.

* **Excepción E3 — Faltante de insumos en cocina (Vinculado a CU-05 y CU-09):**
  * **Disparador:** El Cocinero detecta insuficiencia de insumos durante la preparación (`CU-04`).
  * **Compensación:** Se notifica al Cajero (`CU-05`), se anula únicamente el ítem afectado y se aplica un reembolso parcial al Cliente (`CU-09`) antes de emitir el comprobante final (`CU-08`).