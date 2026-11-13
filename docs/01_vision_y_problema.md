# 1. Visión y problema correcto
> Ejercicio 1 · Temas 1, 2 y 5 · 🎩 PO
> La visión va en el `README.md`. Aquí van los puntos 2 a 6.

## 1.2 ¿Por qué no cascada?

| Causa de falla de cascada | Cómo se vería en mi proyecto |
|---|---|
| **Los requisitos cambian / el cliente no sabe lo que quiere hasta ver algo funcionando** | Chuy no tiene claro si quiere rentar de noche ("la luz me sale cara") y tampoco sabe si cobrar anticipo. Si congeláramos los requisitos en un documento, en 6 meses tendríamos una app que no resuelve su duda real. |
| **La retroalimentación llega demasiado tarde** | Si construimos todo el sistema sin mostrarle R1 y R2 a Chuy, podríamos llegar con un cálculo de renta que no contempla el recargo de fin de semana, o con una política de cancelación distinta a la que él quiere. En cascada el error se descubre al final, cuando ya es caro corregirlo. |

**¿Usaría prototipos?** Sí. Un prototipo de baja fidelidad (bocetos en papel o wireframes) de la **pantalla de reserva** y de la **pantalla de entrada** para validar con Chuy antes de programar. Para R1 y R2 no hace falta prototipo: se validan con los escenarios BDD y con la tabla FIT.

## 1.3 El manifiesto en mi proyecto

| Valor o principio | Decisión concreta en mi proyecto |
|---|---|
| **Valor: Software funcionando sobre documentación exhaustiva** | Al final del Sprint 1 entrego R1 y R2 funcionando y probadas con `pytest`, no un documento de 30 páginas con la especificación de la app. |
| **Valor: Individuos e interacciones sobre procesos y herramientas** | Hablo directo con Chuy (o lo simulo) para validar los escenarios de cancelación en vez de escribir un manual de usuario que nadie va a leer. |
| **Principio: Entregar software funcionando con frecuencia** | Entrego valor al final de cada sprint (2 semanas), no al final del proyecto. Al cierre del Sprint 1 ya hay dos reglas de negocio operativas. |
| **Principio: La simplicidad — el arte de maximizar la cantidad de trabajo no realizado** | No construyo pasarela de pago, ni integración con WhatsApp, ni app móvil en este sprint. Solo las reglas de negocio en Python puro. |

## 1.4 Frameworks

| Framework | Lo que tomo de él |
|---|---|
| **Scrum** | Sprints de 2 semanas, Product Backlog priorizado con MoSCoW, planeación / daily / review / retrospectiva, y los tres sombreros (PO, SM, Dev). |
| **Kanban** | Tablero con columnas y límites WIP, políticas explícitas de transición, visualización del flujo y ciclos de retroalimentación. |
| **XP (Extreme Programming)** | TDD (rojo → verde → refactor), pruebas unitarias y de aceptación con `pytest`, diseño simple, integración continua (commits frecuentes). |

La combinación de Scrum y Kanban se llama: **Scrumban**.

## 1.5 Requisito o solución

| # | Lo que dijo mi cliente | ¿Requisito o solución? | Si es solución: el requisito que hay detrás |
|---|---|---|---|
| 1 | "Los equipos apartan por WhatsApp y luego no llegan; se me cruzan las reservas." | **Requisito** | (Ya es un requisito: centralizar la agenda y evitar reservas cruzadas.) |
| 2 | "Quiero que la app tenga los colores de mi equipo favorito." | **Solución** | La app debe tener identidad visual personalizable (branding del negocio). |
| 3 | "Que el capitán pueda dividir el pago entre sus jugadores." | **Solución** | El sistema debe permitir calcular y dividir el costo de la renta entre los jugadores de un equipo. |
| 4 | "Que se vea en una pantalla en la entrada quién juega a qué hora." | **Solución** | Debe existir una vista pública con la agenda del día visible desde la entrada del negocio. |
| 5 | "No sé si rentar de noche; la luz me sale cara." | **Requisito** | Hay que calcular el costo real de la renta nocturna (luz + tarifa) para que Chuy decida si la ofrece. |

## 1.6 Incertidumbre

- **Incertidumbre del *qué*:** **media**. El problema central (reservas cruzadas y cancelaciones) está claro, pero Chuy duda si ofrecer renta nocturna y no tiene definida su política de anticipo.
- **Incertidumbre del *cómo*:** **baja**. Sabemos que será Python + pytest, con reglas de negocio en funciones puras y sin frameworks web.
- **Zona del diagrama:** **Ejecución / Innovación (frontera)**. El cómo es conocido, el qué está mayormente claro pero con un hueco (renta nocturna).
- **Qué haré en este sprint para bajar la incertidumbre del *qué*:** validar con Chuy (o simularlo con los escenarios BDD y la tabla FIT) el cálculo de R1 en los límites exactos (17:59 vs 18:00, sábado vs domingo) y dejar como historia aparte el análisis de costo de la renta nocturna, para no meterla al Sprint 1.