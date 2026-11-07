# Especificación de Requisitos de Software (SRS Breve) - Pollería Don Fuego S.A.C.

**Curso:** Modelado y Desarrollo de Aplicaciones (CIIN1322P)  
**Estudiante:** Kenneth Zaidd Machacuay Maldonado  
**Organización:** Pollería Don Fuego S.A.C.  
**Propósito:** Definir los Requisitos Funcionales (RF), Historias de Usuario (HU) y su correspondencia con los Casos de Uso (CU) bajo el estándar de la fase de elaboración[cite: 19, 21].

---

## 1. Matriz de Requisitos Funcionales y Trazabilidad

| Objetivo (OBJ) | Requisito Funcional (RF - SRS Breve) | Historias de Usuario (HU) | Caso de Uso Asociado (CU) | Evidencia en Modelos / Diagramas |
| :--- | :--- | :--- | :--- | :--- |
| **OBJ-1** | **RF-01:** Registrar pedido[cite: 21] | HU-01, HU-02[cite: 21] | CU-01 Registrar pedido[cite: 21] | Diagrama de actividad: Nodo inicial y registro[cite: 21] |
| **OBJ-1** | **RF-02:** Validar disponibilidad de carta y stock[cite: 21] | HU-03[cite: 21] | CU-02 Consultar disponibilidad[cite: 21] | Diagrama de actividad: Decisión de stock y Excepción E1[cite: 21] |
| **OBJ-1** | **RF-03:** Modificar o cancelar pedido[cite: 21] | HU-04, HU-05[cite: 21] | CU-03 Modificar o cancelar pedido[cite: 21] | Diagrama de actividad: Fin por cancelación sin cobro[cite: 21] |
| **OBJ-2** | **RF-04:** Preparar pedido y gestionar estados[cite: 21] | HU-06, HU-07[cite: 21] | CU-04 Preparar pedido[cite: 21] | Diagrama de actividad: Envío de comanda a cocina[cite: 21] |
| **OBJ-2** | **RF-05:** Gestionar faltante de insumos[cite: 21] | HU-08[cite: 21] | CU-05 Gestionar faltante[cite: 21] | Diagrama de actividad: Excepción E3[cite: 21] |
| **OBJ-2** | **RF-06:** Despachar y confirmar entrega[cite: 21] | HU-09, HU-10[cite: 21] | CU-06 Gestionar despacho[cite: 21] | Diagrama de actividad: Despacho y entrega final[cite: 21] |
| **OBJ-3** | **RF-07:** Registrar y validar cobro[cite: 21] | HU-11, HU-12[cite: 21] | CU-07 Registrar cobro[cite: 21] | Diagrama de actividad: Registro de cobro y Excepción E2[cite: 21] |
| **OBJ-3** | **RF-08:** Emitir comprobante de pago[cite: 21] | HU-13[cite: 21] | CU-08 Emitir comprobante[cite: 21] | Diagrama de actividad: Emisión de boleta/factura[cite: 21] |
| **OBJ-3** | **RF-09:** Anular comprobante o procesar reembolso[cite: 21] | HU-14[cite: 21] | CU-09 Anular o reembolsar[cite: 21] | Diagrama de actividad: Reembolso parcial por Excepción E3[cite: 21] |

---

## 2. Detalle de Épicas y Alcance Funcional
* **Épica E1 (Registro y Atención de Pedidos):** Agrupa los RF-01, RF-02 y RF-03 (cubriendo las HU-01 a la HU-05), abarcando desde la captura inicial de la solicitud del cliente hasta la validación de stock y posibles cancelaciones anticipadas[cite: 19, 21].
* **Épica E2 (Preparación y Despacho):** Agrupa los RF-04, RF-05 y RF-06 (cubriendo las HU-06 a la HU-10), controlando el flujo de comanda en cocina, la gestión de insumos faltantes y la entrega final al cliente[cite: 19, 21].
* **Épica E3 (Cobro y Comprobante):** Agrupa los RF-07, RF-08 y RF-09 (cubriendo las HU-11 a la HU-14), gestionando los medios de pago, reintentos por rechazo, emisión obligatoria de comprobantes y reembolsos parciales ante incidencias operativas[cite: 19, 21].