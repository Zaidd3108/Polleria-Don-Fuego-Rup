# Matriz de Trazabilidad Integral - Pollería Don Fuego S.A.C.

**Curso:** Modelado y Desarrollo de Aplicaciones (CIIN1322P)  
**Estudiante:** Kenneth Zaidd Machacuay Maldonado  
**Organización:** Pollería Don Fuego S.A.C.  
**Propósito:** Mapear la coherencia bidireccional entre los objetivos del negocio, los requisitos funcionales (SRS breve), las historias de usuario, los casos de uso y las evidencias gráficas en los modelos UML/BPMN (Diagrama de Actividad y Excepciones E1-E3)[cite: 18].

---

## 1. Tabla de Trazabilidad Cruzada (Visión - SRS - HU - CU - Modelos)

| Objetivo (OBJ) | Requisito Funcional (RF - SRS Breve) | Historias de Usuario (HU) | Caso de Uso (CU) | Evidencia en Modelos (Diagrama de Actividad - Fig. 2) |
| :--- | :--- | :--- | :--- | :--- |
| **OBJ-1** | **RF-01:** Registrar pedido[cite: 18] | HU-01, HU-02[cite: 18] | CU-01 Registrar pedido[cite: 18] | Nodo inicial y registro de pedido[cite: 18] |
| **OBJ-1** | **RF-02:** Validar disponibilidad[cite: 18] | HU-03[cite: 18] | CU-02 Consultar disponibilidad[cite: 18] | Decisión de stock y Excepción E1[cite: 18] |
| **OBJ-1** | **RF-03:** Modificar o cancelar pedido[cite: 18] | HU-04, HU-05[cite: 18] | CU-03 Modificar o cancelar pedido[cite: 18] | Fin por cancelación sin cobro[cite: 18] |
| **OBJ-2** | **RF-04:** Preparar pedido y estados[cite: 18] | HU-06, HU-07[cite: 18] | CU-04 Preparar pedido[cite: 18] | Envío de comanda y área de cocina[cite: 18] |
| **OBJ-2** | **RF-05:** Gestionar faltante de insumos[cite: 18] | HU-08[cite: 18] | CU-05 Gestionar faltante[cite: 18] | Excepción E3 (insumos incompletos)[cite: 18] |
| **OBJ-2** | **RF-06:** Despachar y confirmar entrega[cite: 18] | HU-09, HU-10[cite: 18] | CU-06 Gestionar despacho[cite: 18] | Despacho y entrega final al cliente[cite: 18] |
| **OBJ-3** | **RF-07:** Registrar y validar cobro[cite: 18] | HU-11, HU-12[cite: 18] | CU-07 Registrar cobro[cite: 18] | Registro de cobro y Excepción E2[cite: 18] |
| **OBJ-3** | **RF-08:** Emitir comprobante[cite: 18] | HU-13[cite: 18] | CU-08 Emitir comprobante[cite: 18] | Emisión de boleta o factura[cite: 18] |
| **OBJ-3** | **RF-09:** Anular comprobante o reembolsar[cite: 18] | HU-14[cite: 18] | CU-09 Anular o reembolsar[cite: 18] | Reembolso parcial vinculado a Excepción E3[cite: 18] |

---

## 2. Reglas de Validación y Consistencia
* **Cobertura Completa:** El 100% de los requisitos funcionales (9 de 9) cuentan con su respectivo Caso de Uso y asignación de Historias de Usuario[cite: 19].
* **Representación Gráfica:** Todos los Casos de Uso modelados se encuentran explícitamente representados dentro del flujo principal o en las rutas de excepción del Diagrama de Actividad (Figura 2)[cite: 18, 19].
* **Control de Brechas:** Cualquier cambio o ajuste en los requerimientos del SRS exige la actualización síncrona de esta matriz para evitar desalineaciones en las fases de construcción y pruebas.