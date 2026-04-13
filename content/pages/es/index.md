---
lang: es
slug: index
template: home
url: es/
save_as: es/index.html
title: El libro de los agentes de IA
summary: Entiende cómo funcionan los agentes de IA. Construye el tuyo. Elige entre local o nube, código abierto o SaaS. Aprende de las últimas filtraciones de modelos de IA.
---

> **Qué es esto:** un camino coherente desde *leer* cómo funcionan los agentes hasta *construir* uno propio — sin esconderse detrás de APIs caja negra. El sitio complementario [Cómo funcionan los agentes de IA](https://howaiagentswork.com/es/) publica fragmentos más largos y notas al estilo de capítulos; **esta página es el contrato**: qué vas a entender, cómo encajan las fases de la hoja de construcción y dónde seguir leyendo.

---

## En este sitio frente al sitio complementario {#on-this-site}

| Aquí (este sitio del libro) | En [howaiagentswork.com](https://howaiagentswork.com/es/) |
|-----------------------------|-----------------------------------------------------------|
| El **mapa**: promesas, hoja de ruta y la **hoja de construcción** en orden | **Profundidad**: modelos, bucles, herramientas, memoria, planificación — redactado para valer por sí solo en búsqueda y releído |
| **Pasos 0–10** como una sola narrativa que implementarás | **Fragmentos** a los que puedes entrar desde Google sin leer todo lo demás primero |
| Lo bastante breve para hojearlo de una sentada | Nos permite ir largos donde el matiz importa |

Usa esta página para decidir *si* te comprometes; usa el sitio complementario cuando quieras *densidad explicativa* en un solo tema.

---

## Tres motivos para leer {#three-reasons}

### 1) Entender cómo funcionan los agentes

Los agentes no son «un chatbot con más actitud». Son **bucles** que acoplan un modelo a **estado**, **herramientas** y, cuando hace falta, **memoria** y **planificación**. Este libro construye ese modelo mental en lenguaje técnico llano — **sin asumir cursos previos de ML** — para que puedas razonar sobre modos de fallo, costes y compromisos de diseño.

---

### 2) Construir tu propio agente en local

Seguirás un tutorial que produce un **agente funcional en tu máquina o VM** con piezas de código abierto. No hace falta una «API de agente» de pago para el núcleo del recorrido.

Aprenderás a conectar:

- un **modelo** (local, privado o alojado — la misma forma de código)
- un **bucle de agente** (iteración y retroalimentación)
- **herramientas** (acciones que tocan el mundo real)
- **memoria + recuperación** (escalar más allá de una sola ventana de contexto)

Las APIs alojadas (ChatGPT, Claude, …) son aceleradores opcionales; la postura por defecto es **Python reproducible e inspeccionable**.

---

### 3) Conclusiones tras las filtraciones recientes de modelos

Incluimos un **«y qué»** explícito: qué sugieren las filtraciones y los lanzamientos reales sobre **fiabilidad**, **evaluación** y **diseño de sistemas** — sin convertir el libro en cotilleo. El objetivo es **criterio de ingeniería**, no titulares.

---

## Hoja de ruta de capítulos (borrador) {#chapter-roadmap}

- Capítulo 0 — Introducción
- Capítulo 1 — Fundamentos
- Capítulo 2 — Cómo funcionan los modelos
- Capítulo 3 — Arquitectura del sistema
- Capítulo 4 — Entorno y configuración
- Capítulo 5 — El bucle del agente
- Capítulo 6 — Sistemas de herramientas
- Capítulo 7 — Memoria y recuperación
- Capítulo 8 — Planificación y descomposición
- Capítulo 9 — Sistemas multiagente
- Capítulo 10 — Sistemas avanzados y producción

Lectura complementaria para varios de estos temas (mismo proyecto, otra superficie):

- **Modelos y tokens** — intuición de qué puede y no puede ver el modelo en un solo paso  
- **El bucle** — por qué «de un tiro» frente a «multipaso» lo cambia todo  
- **Herramientas** — análisis, seguridad y el límite entre lenguaje y ejecución  
- **Memoria y recuperación** — selección, no solo almacenamiento  
- **Planificación** — planes como hipótesis que deben sobrevivir al contacto con la realidad  

Explora esos hilos en el sitio complementario cuando quieras detalle más allá de esta visión general.

---

## Hoja de construcción (`build-your-own-agent`) {#build-track-summary}

La **pista de ejercicios** práctica (pasos 0–10) tiene ahora su propia página para que el inicio siga siendo un contrato y una hoja de ruta ligeros.

**[Abrir la pista de ejercicios →](/es/exercise/)** — enlaces rápidos y el texto completo.

---

## Dónde seguir leyendo {#read-next}

Empieza por los fragmentos complementarios cuando quieras profundidad al estilo capítulo:

- [English — How AI agents work](https://howaiagentswork.com/en/) — fragmentos y notas largas  
- [Español](https://howaiagentswork.com/es/) — mismo proyecto, entrada en castellano  

La captura de correos y las donaciones pueden añadirse después; por ahora, el progreso se ve en el sitio complementario y en esta hoja de ruta.

---

*Pase editorial opcional: condensar cada paso en un solo bloque tipo blueprint (Objetivo / Resultado / Herramientas / Conocimiento / Listo para seguir) para el Capítulo 0 o el README del repositorio complementario.*
