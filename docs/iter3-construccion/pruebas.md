# Plan de Pruebas y Validación - Pollería Don Fuego S.A.C.

**Curso:** Modelado y Desarrollo de Aplicaciones (CIIN1322P)  
**Estudiante:** Kenneth Zaidd Machacuay Maldonado  
**Organización:** Pollería Don Fuego S.A.C.  
**Propósito:** Definir la estrategia de pruebas, casos de prueba funcionales e integración para validar la correcta implementación de las épicas (E1, E2, E3) y el manejo robusto de excepciones durante las fases de Construcción (C1, C2) y Transición (T1)[cite: 16].

---

## 1. Estrategia General de Pruebas
El plan de pruebas se estructura de manera incremental alineado al roadmap del proyecto[cite: 16]:
* **Pruebas Unitarias:** Verificación de componentes individuales y reglas de negocio asociadas a los Requisitos Funcionales (RF-01 al RF-09).
* **Pruebas de Integración:** Validación de la comunicación entre el registro de pedidos, el control de stock, la caja y el envío de comandas a cocina (Épicas E1 y E2)[cite: 16].
* **Pruebas de Excepciones:** Comprobación rigurosa de los flujos alternos y de compensación (E1: Sin stock[cite: 18], E2: Pagos rechazados[cite: 18], E3: Faltante de insumos[cite: 18]).
* **Pruebas de Aceptación:** Validación operativa con el usuario final durante la fase de Transición (T1)[cite: 16].

---

## 2. Casos de Prueba Principales (Matriz de Validación)

| ID Prueba | Módulo / Épica | Descripción de la Prueba | Resultado Esperado | Trazabilidad |
| :--- | :--- | :--- | :--- | :--- |
| **CP-01** | Épica E1 | Registrar un pedido completo seleccionando ítems de la carta vigente[cite: 16]. | El pedido se almacena correctamente con estado inicial y asigna ID de seguimiento. | RF-01, CU-01[cite: 21] |
| **CP-02** | Épica E1 | Validar la disponibilidad de un producto sin stock al momento de registrar el pedido[cite: 18]. | Se activa la excepción E1, ofreciendo alternativa o cancelando sin cobro[cite: 18]. | RF-02, CU-02, E1[cite: 18, 21] |
| **CP-03** | Épica E3 | Simular el rechazo del medio de pago en el registro de cobro[cite: 18]. | Permite hasta 2 reintentos; si se agotan, anula el pedido y libera el stock reservado[cite: 18]. | RF-07, CU-07, E2[cite: 18, 21] |
| **CP-04** | Épica E2 | Enviar comanda digital hacia el área de cocina tras validar el pago[cite: 18, 21]. | La orden aparece en la interfaz del cocinero de manera inmediata. | RF-04, CU-04[cite: 21] |
| **CP-05** | Épica E2 | Detectar faltante de insumos durante la preparación en cocina[cite: 18]. | Se activa la excepción E3, notificando a caja, anulando el ítem y generando reembolso parcial[cite: 18]. | RF-05, RF-09, CU-05, E3[cite: 18, 21] |
| **CP-06** | Épica E3 | Emitir el comprobante de pago (boleta/factura) por el monto final cobrado[cite: 21]. | Generación y visualización correcta del documento tributario para el cliente. | RF-08, CU-08[cite: 21] |

---

## 3. Criterios de Aprobación (Definition of Done)
* 100% de los casos de prueba críticos (CP-01 a CP-06) ejecutados sin errores bloqueantes.
* Cobertura total de los flujos de excepción (E1, E2, E3) con sus respectivas compensaciones validadas en ambiente de pruebas[cite: 18].
* Aprobación formal de la capacidad operativa inicial (IOC) al finalizar la construcción de las épicas[cite: 16].