# Matriz de Trazabilidad de Construcción - Pollería Don Fuego S.A.C.

**Curso:** Modelado y Desarrollo de Aplicaciones (CIIN1322P)  
**Estudiante:** Kenneth Zaidd Machacuay Maldonado  
**Organización:** Pollería Don Fuego S.A.C.  
**Propósito:** Actualizar y verificar la trazabilidad entre los Requisitos Funcionales (RF), las Historias de Usuario (HU), las Épicas implementadas (E1, E2, E3), los componentes de código y los casos de prueba durante las fases de Construcción (C1, C2)[cite: 16].

---

## 1. Tabla de Trazabilidad de Construcción e Implementación

| Requisito Funcional (RF) | Épica Asociada | Historias de Usuario (HU) | Componente / Módulo Implementado | Casos de Prueba Relacionados | Estado de Construcción |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RF-01** | Épica E1[cite: 16] | HU-01, HU-02[cite: 18] | Módulo de Registro de Pedidos (UI / API) | CP-01[cite: 21] | Implementado y Verificado |
| **RF-02** | Épica E1[cite: 16] | HU-03[cite: 18] | Validador de Carta Vigente y Stock | CP-02, Excepción E1[cite: 18, 21] | Implementado y Verificado |
| **RF-03** | Épica E1[cite: 16] | HU-04, HU-05[cite: 18] | Gestor de Modificación y Cancelación | CP-02[cite: 21] | Implementado y Verificado |
| **RF-04** | Épica E2[cite: 16] | HU-06, HU-07[cite: 18] | Módulo de Comandas y Cocina | CP-04[cite: 21] | Implementado y Verificado |
| **RF-05** | Épica E2[cite: 16] | HU-08[cite: 18] | Alerta de Faltantes de Insumos | CP-05, Excepción E3[cite: 18, 21] | Implementado y Verificado |
| **RF-06** | Épica E2[cite: 16] | HU-09, HU-10[cite: 18] | Módulo de Despacho y Reparto | CP-05[cite: 21] | Implementado y Verificado |
| **RF-07** | Épica E3[cite: 16] | HU-11, HU-12[cite: 18] | Pasarela de Cobro y Validación | CP-03, Excepción E2[cite: 18, 21] | Implementado y Verificado |
| **RF-08** | Épica E3[cite: 16] | HU-13[cite: 18] | Generador de Comprobantes (Boleta/Factura) | CP-06[cite: 21] | Implementado y Verificado |
| **RF-09** | Épica E3[cite: 16] | HU-14[cite: 18] | Gestor de Reembolsos y Anulaciones | CP-05[cite: 21] | Implementado y Verificado |

---

## 2. Control de Cambios y Verificación de Excepciones
* **Validación de Excepciones (E1, E2, E3):** Cada excepción modelada en la fase de elaboración cuenta con su respectiva aserción en el código y prueba unitaria de integración asociada, garantizando que no existan flujos colgados ni estados indeterminados en el sistema[cite: 18].
* **Sincronización con el Repositorio:** Las modificaciones en el código fuente de los componentes reflejan de manera directa el alcance definido en las iteraciones de construcción (C1 y C2)[cite: 16].