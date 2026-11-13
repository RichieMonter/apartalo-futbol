# Apártalo — Canchas de fútbol 7 La Cancha

Repositorio de la Evidencia 1 de Proyecto de ingeniería de software (Tecmilenio, CRN 13241).

## Datos del Estudiante
- **Estudiante:** Ricardo Fuentes Monter
- **Matrícula:** AL02938286
- **Variante:** Variante 8 — Canchas de fútbol 7 La Cancha
- **Project (tablero):** https://github.com/users/RichieMonter/projects/2

## Visión del producto
🎩 PO · Ejercicio 1, punto 1.
Apártalo es una aplicación web de reservas y gestión automatizada de canchas de fútbol 7 para el negocio "La Cancha", orientada a capitanes de equipos y administradores. Su propósito es centralizar la agenda de horarios y cálculos de tarifas en una sola plataforma, resolviendo el problema de las reservas cruzadas por WhatsApp y las cancelaciones sin previo aviso mediante reglas de negocio claras y pagos transparentes.

## Mi equipo Scrum (los tres sombreros)
| Sombrero | Lo que hago con él en este proyecto |
| :--- | :--- |
| 🎩 PO | Definición de la visión, creación y priorización del Product Backlog (MoSCoW), redacción de historias de usuario y validación de criterios de aceptación con el cliente (Chuy Rangel). |
| 🎩 SM | Configuración y facilitación del tablero Kanban, establecimiento de límites WIP, políticas explícitas y seguimiento de la bitácora del Sprint 1. |
| 🎩 Desarrollador | Implementación de las reglas de negocio (R1 y R2) en Python aplicando TDD, desarrollo de pruebas unitarias, de aceptación y no funcionales con pytest. |

## Cómo está organizado este repositorio
| Carpeta o archivo | Qué contiene | Ejercicio |
| :--- | :--- | :--- |
| `docs/01_vision_y_problema.md` | Paradigmas, manifiesto, requisito vs. solución, incertidumbre | 1 |
| Issues (historia y épica) + `docs/02_backlog.md` | Product backlog, plantilla invertida, glosario, iceberg | 2 |
| `docs/03_tablero.md` | Columnas, límites WIP, políticas y prácticas de kanban | 3 |
| `docs/04_refinamiento.md` + `features/` | Grooming, carga máxima, división, escenarios BDD, tabla FIT | 4 |
| `docs/05_sprint1.md` | Planeación, bitácora, revisión y retrospectiva | 5 |
| `src/apartalo/` + `tests/` + `docs/06_tdd.md` | Código, pruebas y ciclos de TDD | 6 |
| Issues rnf + `docs/07_rnf.md` | Requisitos no funcionales | 7 |
| `metricas/` + `docs/08_metricas.md` | Fotografía del tablero y consultas SQL | 8 |
| `ENTREGA.md` | Enlaces a cada evidencia | Entrega |

## Cómo correr las pruebas
```powershell
python -m venv .venv
.venv\Scripts\activate        # En Windows
pip install -r requirements.txt
pytest                           # todas las pruebas
pytest -m aceptacion             # solo la suite de aceptación
pytest -m unitaria               # solo las unitarias
pytest -m rnf                    # solo las de requisitos no funcionales