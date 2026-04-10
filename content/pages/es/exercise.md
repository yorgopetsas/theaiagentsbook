---
lang: es
slug: exercise
title: Pista de ejercicios
summary: Recorrido paso a paso build-your-own-agent (fases 0–10): arquitectura, objetivos y qué deberías poder hacer antes de seguir.
template: exercise
url: es/exercise/
save_as: es/exercise/index.html
---

## Hoja de construcción: `build-your-own-agent` {#build-track}

Antes de integrar los pasos en los capítulos del libro, fijamos la **arquitectura** del código paralelo: algo que puedas **ejecutar, inspeccionar y ampliar** — alineado con la teoría anterior.

**Puedes ejecutar este proyecto:**

- **En tu máquina** con un runtime local como **Ollama** (privado, sin nube obligatoria), o  
- **Con modelos alojados** cuando quieras velocidad o no tengas GPU local — **la forma del código se mantiene**; solo cambia el backend del modelo.

El camino por defecto es **Python plano primero**. Los frameworks aparecen después como *comparaciones opcionales* para que aprendas qué abstraen **después** de haber sentido el bucle en crudo.

### Cómo crece el proyecto {#how-the-project-grows}

El proyecto crece por **fases**. Cada fase produce algo que puedes ejecutar y probar. El sistema **no** se reescribe desde cero cada vez — **evoluciona**, así que ves cómo una simple llamada al modelo se convierte en algo que merece la palabra *agente*.

---

### Paso 0 — Una llamada mínima al modelo {#step-0}

**Objetivo:** Que la pila se sienta real de inmediato — y que las limitaciones se vean.


**Resultado:** El programa más pequeño que envía un prompt a un modelo y obtiene una respuesta. Aún sin bucle, herramientas, memoria ni planificación. Emocionante porque funciona; decepcionante porque es solo un intercambio — ese contraste es la línea base.

**Herramientas:** Entorno Python + interfaz al modelo. Puedes empezar con una API remota por simplicidad y luego cambiar a un modelo local.

**Conocimiento:** Aún no es «cómo construir un agente» — sino qué puede y no puede hacer un modelo **solo**. Esa idea es necesaria antes de los pasos siguientes.

**Listo para seguir:** Puedes ejecutar un prompt, obtener respuesta, cambiar el prompt y ver que el sistema sigue pareciendo una interacción **de un tiro**, no un proceso persistente.

---

### Paso 1 — Esqueleto de proyecto estable {#step-1}

**Objetivo:** Dejar de tratar el programa como un script; tratarlo como un **sistema**.

**Resultado:** Una base de código pequeña (no un solo archivo): acceso al modelo separado de la lógica de la app, hueco para configuración y componentes futuros — aún no «más listo», pero **más limpio**.

**Herramientas:** Carpetas, módulos, variables de entorno, archivos de configuración, una clase o interfaz sencilla para el modelo.

**Conocimiento:** La arquitectura importa para que el sistema pueda crecer con facilidad.

**Listo para seguir:** Puedes cambiar prompts o backends de modelo sin reescribir todo el proyecto; se siente como el inicio de una app real.

---

### Paso 2 — El primer bucle de agente {#step-2}

**Objetivo:** Convertir una llamada única en un **bucle**: actuar, actualizar estado, continuar.

**Resultado:** El primer comportamiento en el tiempo — aún primitivo, pero ya no estático. Varios pasos en secuencia.

**Herramientas:** Flujo de control en Python, un objeto de estado sencillo, ensamblaje del prompt. Aún sin acciones en el mundo real.

**Conocimiento:** La inteligencia aquí viene de **iteración y retroalimentación**, no solo de la calidad del modelo.

**Listo para seguir:** Puedes asignar una tarea, ver más de un paso, inspeccionar el historial y explicar en qué se diferencia el bucle de una llamada única.

---

### Paso 3 — Salidas estructuradas y análisis de acciones {#step-3}

**Objetivo:** Pasar de prosa vaga a salidas que el sistema pueda **interpretar con fiabilidad**.

**Resultado:** Respuestas estructuradas (p. ej. acciones tipo JSON) y un analizador que convierte la salida del modelo en comportamiento — menos chatbot, más **proceso**.

**Herramientas:** Diseño de prompts, esquemas ligeros, análisis, validación, manejo de errores.

**Conocimiento:** La acción necesita **estructura** en el límite entre lenguaje y ejecución.

**Listo para seguir:** Salidas estructuradas válidas la mayor parte del tiempo, recuperación ante errores de formato, intención legible por máquina de forma coherente.

---

### Paso 4 — Las primeras herramientas {#step-4}

**Objetivo:** Permitir que el agente afecte o inspeccione algo **fuera** del prompt.

**Resultado:** Primeras herramientas reales (p. ej. leer/listar archivos, escrituras controladas). El agente no solo habla de archivos — puede **usarlos**.

**Herramientas:** E/S de archivos, registro de herramientas, despacho desde acciones analizadas a funciones, restricciones de seguridad ligeras.

**Conocimiento:** Las herramientas son el puente del lenguaje al mundo — y deben diseñarse con cuidado.

**Listo para seguir:** El agente puede elegir una herramienta, ejecutarla e incorporar el resultado al siguiente paso del bucle.

---

### Paso 5 — Retroalimentación real mediante ejecución de comandos {#step-5}

**Objetivo:** Añadir interacción **fundamentada**: ejecutar pruebas, scripts, comandos — inspeccionar comportamiento real.

**Resultado:** Un **prototipo de agente de código** tosco pero real: inspeccionar un proyecto, ejecutar comandos, responder a la salida.

**Herramientas:** Ejecución de subprocesos, envoltorios seguros, registro, validación más fuerte. El entorno pasa a formar parte de la arquitectura.

**Conocimiento:** La retroalimentación fundamentada es lo que hace a los agentes **prácticamente** potentes.

**Listo para seguir:** Una tarea de código sencilla donde el agente lee archivos, ejecuta un comando e incorpora la salida al bucle de forma significativa.

---

### Paso 6 — Memoria y recuperación {#step-6}

**Objetivo:** Abordar la **presión de contexto** a medida que se acumulan pasos e interacciones.

**Resultado:** Memoria fuera del prompt inmediato + recuperación que decide qué traer de vuelta — aún no «inteligencia a largo plazo» completa, pero sin reinicio total cada pocos turnos.

**Herramientas:** Estado persistente, historial, capa de recuperación; empezar de forma ingenua (p. ej. almacén/búsqueda simple) y comparar embeddings / bases vectoriales si aporta.

**Conocimiento:** La memoria es un problema de **selección** — qué recuperar y cuándo — no solo de almacenamiento.

**Listo para seguir:** El sistema usa información de pasos o archivos anteriores sin meterlo todo en el prompt activo.

---

### Paso 7 — Planificación y descomposición de tareas {#step-7}

**Objetivo:** Pasar de la pura reactividad a la **dirección**: planificación y descomposición explícitas.

**Resultado:** Una idea visible de lo que el sistema intenta completar — no solo el siguiente paso plausible.

**Herramientas:** Prompts de plan, estado del plan, lógica de revisión, integración más estrecha entre el estado del bucle y la estructura de la tarea.

**Conocimiento:** La planificación es dirección en el tiempo; los planes son **hipótesis** y deben actualizarse cuando cambia la realidad.

**Listo para seguir:** Puedes ver un plan, actuar sobre él, revisarlo y distinguir reaccionar de avanzar por una estructura.

---

### Paso 8 — Un agente de código más capaz {#step-8}

**Objetivo:** Unificar bucle, herramientas, memoria y planificación en un caso de uso **real de código**.

**Resultado:** Un asistente de código de un solo agente que inspecciona un repositorio, da varios pasos, recuerda resultados previos y actúa con cierta dirección — no solo reacción.

**Herramientas:** Todo lo construido hasta ahora, integrado; parches más seguros o búsqueda de código opcionales.

**Conocimiento:** **Síntesis** — las ideas dejan de ser lecciones separadas y se convierten en un sistema.

**Listo para seguir:** Una tarea real acotada en un proyecto de ejemplo con un flujo multipaso significativo.

---

### Paso 9 — Extensión multiagente {#step-9}

**Objetivo:** Extender el sistema — sin sustituirlo — con **roles** (p. ej. planificador, ejecutor, evaluador).

**Resultado:** El trabajo puede repartirse entre agentes en lugar de un solo bucle con toda la responsabilidad.

**Herramientas:** Orquestación, prompts de rol, memoria compartida o particionada, formatos de mensaje entre agentes.

**Conocimiento:** El diseño multiagente trata de **separación estructural** de responsabilidades, no de impresionar.

**Listo para seguir:** Dos o más agentes coordinan y puedes contrastar con sentido el comportamiento mono- frente a multiagente.

---

### Paso 10 — Endurecimiento para producción {#step-10}

**Objetivo:** Pasar del prototipo educativo a algo que puedas **operar**: fiabilidad, observabilidad, comportamiento acotado.

**Resultado:** Un sistema que puedes monitorizar, depurar, limitar y en el que confiar con más realismo — no solo «capaz».

**Herramientas:** Registro, trazas, límites de profundidad del bucle, manejo de errores, ganchos de inspección; comparaciones con frameworks **después** de entender qué abstraen.

**Conocimiento:** El último tramo suele ser **estabilidad** bajo condiciones imperfectas, no solo ingenio bruto.

**Listo para seguir:** Ejecuciones repetidas, inspeccionabilidad del comportamiento y tratar éxito y fracaso como comportamiento de **sistema** — no magia.

---

## Cómo vive el lector el progreso {#progress-lens}

Cada fase responde a una pregunta concreta:

| Paso | Pregunta |
|------|----------|
| 0 | ¿Puedo hacer que un modelo responda siquiera? |
| 2 | ¿Puedo hacer que continúe en el tiempo? |
| 4 | ¿Puedo hacer que toque el mundo? |
| 6 | ¿Puedo hacer que deje de olvidar? |
| 7 | ¿Puedo hacer que actúe con estructura? |
| 9 | ¿Puedo repartir el trabajo entre roles? |
| 10 | ¿Puedo confiar en lo construido lo bastante para seguir mejorándolo? |

Esa progresión mantiene motivada la hoja de construcción: resultados visibles en cada fase.

---

## Qué necesitas antes de empezar {#prerequisites}

La hoja de construcción asume que conoces **Python**, no ingeniería de IA:

**Necesitas:** un entorno Python, comodidad ejecutando scripts, funciones/archivos básicos y ganas de depurar tu configuración.

**No necesitas:** formación previa en ML, matemáticas pesadas ni familiaridad con frameworks de IA — llegan solo cuando lo merecen.

---

## Por qué funciona esta estructura {#why-it-works}

El libro enseña **comprensión**. La hoja de construcción enseña **encarnación**. No solo lees sobre bucles, herramientas, memoria y planificación — los ensamblas en un orden donde cada pieza se vuelve **necesaria**. Esa coherencia es lo que evita que teoría y práctica parezcan dos libros distintos.

---

*Pase editorial opcional: condensar cada paso en un solo bloque tipo blueprint (Objetivo / Resultado / Herramientas / Conocimiento / Listo para seguir) para el Capítulo 0 o el README del repositorio complementario.*
