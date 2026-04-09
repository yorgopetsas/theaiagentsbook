---
lang: en
slug: index
template: home
title: The AI Agents Book
summary: Understand how AI agents work, build your own local agent (open source, private), and extract practical conclusions from recent model leaks.
---

> **What this is:** one coherent path from *reading* how agents work to *building* one yourself—without hiding behind black-box APIs. The companion site [How AI agents work](https://howaiagentswork.com/en/) publishes longer fragments and chapter-style notes; **this page is the contract**: what you will understand, how the build track stages fit together, and where to read next.

---

## On this site vs. the companion site {#on-this-site}

| Here (this book site) | On [howaiagentswork.com](https://howaiagentswork.com/en/) |
|------------------------|-----------------------------------------------------------|
| The **map**: promises, roadmap, and the **build track** in order | **Deeper dives**: models, loops, tools, memory, planning—written to stand alone for search and rereading |
| **Steps 0–10** as a single narrative you will implement | **Fragments** you can enter from Google without reading everything else first |
| Stays short enough to skim in one sitting | Lets us go long where nuance matters |

Use this page to decide *whether* to commit; use the companion site when you want *explanation density* on a single topic.

---

## Three reasons to read {#three-reasons}

### 1) Understand how agents work

Agents are not “a chatbot with extra vibes.” They are **loops** that couple a model to **state**, **tools**, and (when needed) **memory** and **planning**. This book builds that mental model in plain technical language—**no prior ML coursework assumed**—so you can reason about failure modes, costs, and design trade-offs.

---

### 2) Build your own agent locally

You will follow a tutorial that produces a **working agent on your machine or VM** using open-source pieces. No paid “agent API” is required for the core path.

What you will learn to wire together:

- a **model** (local, private, or hosted—same code shape)
- an **agent loop** (iteration and feedback)
- **tools** (actions that touch the real world)
- **memory + retrieval** (scaling beyond a single context window)

Hosted APIs (ChatGPT, Claude, …) are optional accelerators; the default stance is **reproducible, inspectable Python**.

---

### 3) Conclusions from recent model leak fallout

We include an explicit **“so what”**: what leaks and real-world releases suggest about **reliability**, **evaluation**, and **system design**—without turning the book into gossip. The point is **engineering judgment**, not headlines.

---

## Chapter roadmap (draft status) {#chapter-roadmap}

- Chapter 0 — Introduction
- Chapter 1 — Foundations
- Chapter 2 — How Models Work
- Chapter 3 — System Architecture
- Chapter 4 — Environment & Setup
- Chapter 5 — The Agent Loop
- Chapter 6 — Tool Systems
- Chapter 7 — Memory & Retrieval
- Chapter 8 — Planning & Decomposition
- Chapter 9 — Multi-Agent Systems
- Chapter 10 — Advanced Systems & Production

Companion reading for several of these themes (same project, different surface):

- **Models & tokens** — intuition for what the model can and cannot see in one pass  
- **The loop** — why “one-shot” vs “multi-step” changes everything  
- **Tools** — parsing, safety, and the boundary between language and execution  
- **Memory & retrieval** — selection, not storage  
- **Planning** — plans as hypotheses that must survive contact with reality  

Explore those threads on the companion site when you want detail beyond this overview.

---

## Build track: `build-your-own-agent` {#build-track}

Before we fold steps into the book chapters, we lock the **architecture** of the parallel codebase: something you can **run, inspect, and extend**—aligned with the theory above.

**You can run this project:**

- **On your machine** with a local runtime such as **Ollama** (private, no cloud required), or  
- **With hosted models** when you want speed or lack local GPU—the **shape of the code stays the same**; only the model backend changes.

The default path is **plain Python first**. Frameworks appear later as *optional comparisons* so you learn what they abstract **after** you have felt the raw loop.

### How the project grows {#how-the-project-grows}

The project grows in **stages**. Each stage produces something you can run and test. The system is **not** rewritten from scratch each time—it **evolves**, so you watch a single model call turn into something that deserves the word *agent*.

---

### Step 0 — A bare model call {#step-0}

**Goal:** Make the stack feel real immediately—and make the limitations visible.


**Result:** The smallest program that sends a prompt to a model and gets a response. No loop, tools, memory, or planning yet. Exciting because it works; underwhelming because it’s only a single exchange—that contrast is the baseline.

**Tools:** Python environment + a model interface. You may start with a remote API for simplicity, then swap in a local model later.

**Knowledge:** Not “how to build an agent” yet—but what a model **alone** can and cannot do. That insight is required before later steps.

**Ready to move on:** You can run a prompt, get a response, change the prompt, and see that the system still feels like a **one-shot** interaction, not a persistent process.

---

### Step 1 — A stable project skeleton {#step-1}

**Goal:** Stop treating the program as a script; treat it as a **system**.

**Result:** A small codebase (not one file): model access separated from app logic, room for configuration and future components—not “smarter” yet, but **cleaner**.

**Tools:** Folders, modules, environment variables, config files, a simple class or interface for the model.

**Knowledge:** Architecture matters for how easily the system can grow.

**Ready to move on:** You can swap prompts or model backends without rewriting the whole project; it feels like the start of a real app.

---

### Step 2 — The first agent loop {#step-2}

**Goal:** Turn a one-shot call into a **loop**: act, update state, continue.

**Result:** The first behavior over time—still primitive, but no longer static. Multiple steps in sequence.

**Tools:** Python control flow, a simple state object, prompt assembly. Still no real-world actions.

**Knowledge:** Intelligence here comes from **iteration and feedback**, not only from model quality.

**Ready to move on:** You can assign a task, watch more than one step, inspect history, and explain why the loop differs from a one-shot call.

---

### Step 3 — Structured outputs and action parsing {#step-3}

**Goal:** Move from vague prose to outputs the system can **interpret reliably**.

**Result:** Structured responses (e.g. JSON-like actions) and a parser that turns model output into behavior—less chatbot, more **process**.

**Tools:** Prompt design, lightweight schemas, parsing, validation, error handling.

**Knowledge:** Action needs **structure** at the boundary between language and execution.

**Ready to move on:** Valid structured outputs most of the time, recovery from formatting mistakes, consistent machine-readable intent.

---

### Step 4 — The first tools {#step-4}

**Goal:** Let the agent affect or inspect something **outside** the prompt.

**Result:** First real tools (e.g. read/list files, controlled writes). The agent doesn’t only talk about files—it can **use** them.

**Tools:** File I/O, a tool registry, a dispatcher from parsed actions to functions, light safety constraints.

**Knowledge:** Tools are the bridge from language to the world—and must be shaped carefully.

**Ready to move on:** The agent can choose a tool, run it, feed the result into the next loop step.

---

### Step 5 — Real feedback through command execution {#step-5}

**Goal:** Add **grounded** interaction: run tests, scripts, commands—inspect real behavior.

**Result:** A rough but real **coding-agent prototype**: inspect a project, run commands, respond to output.

**Tools:** Subprocess execution, safe wrappers, logging, stronger validation. The environment becomes part of the architecture.

**Knowledge:** Grounded feedback is what makes agents **practically** powerful.

**Ready to move on:** A simple coding task where the agent reads files, runs a command, and meaningfully feeds output back into the loop.

---

### Step 6 — Memory and retrieval {#step-6}

**Goal:** Address **context pressure** as steps and interactions accumulate.

**Result:** Memory outside the immediate prompt + retrieval that decides what to bring back—not full “long-term intelligence” yet, but no full reset every few turns.

**Tools:** Persistent state, history, a retrieval layer; start naive (e.g. simple store/search), then compare embeddings / vector DBs if useful.

**Knowledge:** Memory is a **selection** problem—what to retrieve, when—not just storage.

**Ready to move on:** The system uses information from earlier steps or files without stuffing everything into the live prompt.

---

### Step 7 — Planning and task decomposition {#step-7}

**Goal:** Move from pure reactivity to **direction**: explicit planning and decomposition.

**Result:** A visible sense of what the system is trying to complete—not only the next plausible step.

**Tools:** Plan prompts, plan state, revision logic, tighter integration between loop state and task structure.

**Knowledge:** Planning is direction over time; plans are **hypotheses** and must update when reality changes.

**Ready to move on:** You can see a plan, act on it, revise it, and distinguish reacting from working through a structure.

---

### Step 8 — A more capable coding agent {#step-8}

**Goal:** Unify loop, tools, memory, and planning around a **real codebase** use case.

**Result:** A single-agent coding assistant that inspects a repo, takes several steps, remembers prior results, and acts with some direction—not only reaction.

**Tools:** Everything built so far, integrated; optional safer patching or code search.

**Knowledge:** **Synthesis**—earlier ideas stop being separate lessons and become one system.

**Ready to move on:** A bounded real task in a sample project with a meaningful multi-step workflow.

---

### Step 9 — Multi-agent extension {#step-9}

**Goal:** Extend the system—don’t replace it—with **roles** (e.g. planner, executor, evaluator).

**Result:** Work can split across agents instead of one loop carrying every responsibility.

**Tools:** Orchestration, role prompts, shared or partitioned memory, inter-agent message formats.

**Knowledge:** Multi-agent design is about **structural** separation of responsibilities, not impressiveness.

**Ready to move on:** Two or more agents coordinate and you can contrast single- vs multi-agent behavior meaningfully.

---

### Step 10 — Production hardening {#step-10}

**Goal:** Shift from educational prototype toward something you can **operate**: reliability, observability, bounded behavior.

**Result:** A system you can monitor, debug, constrain, and trust more realistically—not only “capable.”

**Tools:** Logging, tracing, limits on loop depth, error handling, inspection hooks; optional framework comparisons **after** you understand what they abstract.

**Knowledge:** The last mile is often **stability** under imperfect conditions, not raw cleverness.

**Ready to move on:** Repeated runs, inspectability of execution, and treating success and failure as **system** behavior—not magic.

---

## How the reader experiences progress {#progress-lens}

Each stage answers one concrete question:

| Step | Question |
|------|----------|
| 0 | Can I make a model respond at all? |
| 2 | Can I make it continue over time? |
| 4 | Can I make it touch the world? |
| 6 | Can I make it stop forgetting? |
| 7 | Can I make it act with structure? |
| 9 | Can I make the work split across roles? |
| 10 | Can I trust what I built enough to keep improving it? |

That progression keeps the build track motivating: visible results at every stage.

---

## What you need before starting {#prerequisites}

The build track assumes you know **Python**, not AI engineering:

**You need:** a Python environment, comfort running scripts, basic functions/files, and willingness to debug your setup.

**You don’t need:** prior ML training, heavy math, or familiarity with AI frameworks—those arrive only when they earn their place.

---

## Why this structure works {#why-it-works}

The book teaches **understanding**. The build track teaches **embodiment**. You don’t only read about loops, tools, memory, and planning—you assemble them in an order where each piece becomes **necessary**. That coherence is what keeps theory and practice from feeling like two different books.

---

## Where to read next {#read-next}

Start with the companion fragments when you want chapter-length depth:

- [English — How AI agents work](https://howaiagentswork.com/en/) — fragments and long-form notes  
- [Español](https://howaiagentswork.com/es/) — same project, Spanish entry point  

Email capture and donations can layer on later; for now, progress is visible through the companion site and this roadmap.

---

*Optional editorial pass: tighten each step into a single blueprint block (Goal / Result / Tools / Knowledge / Ready-to-move-on) for Chapter 0 or the companion repo README.*
