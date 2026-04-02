---
lang: en
slug: index
template: home
title: The AI Agents Book
summary: Understand how AI agents work, build your own local agent (open source, private), and extract practical conclusions from recent model leaks.
---

## 1) Understand how agents work

This book explains agent systems in technical language, but without assuming prior AI knowledge. You’ll build intuition for what’s happening inside: model outputs, iterative loops, tool calls, and memory/retrieval.

---

## 2) Build your own agent locally

You will follow a tutorial that produces a working agent on your own computer/VM using open-source components—no paid “agent APIs” required.

What you will learn how to wire together:

- a model (local or private)
- an agent loop (iteration)
- tools (actions in the real world)
- memory + retrieval (scaling beyond context)

Optional paid libraries and tools can be listed when they help, but the core path stays local and reproducible.

---

## 3) Conclusions from recent model leak fallout

We include an explicit “so what” section: what we can learn about agent reliability, system design trade-offs, and evaluation from leaked or real-world model information.

---

## Chapter roadmap (initial draft status)

- Chapter 0 — Introduction (not written)
- Chapter 1 — Foundations (not written)
- Chapter 2 — How Models Work (done — deep)
- Chapter 3 — System Architecture (not written)
- Chapter 4 — Environment & Setup (not written)
- Chapter 5 — The Agent Loop (done — deep)
- Chapter 6 — Tool Systems (partially deep — needs full rewrite)
- Chapter 7 — Memory & Retrieval (done — deep)
- Chapter 8 — Planning & Decomposition (done — deep, recently rewritten)
- Chapter 9 — Multi-Agent Systems (not written)
- Chapter 10 — Advanced Systems & Production (not written)

---

## Build track: `build-your-own-agent`

Before we add build steps into the book, we lock the **build track architecture** first. The parallel project below is the proposed roadmap: a real codebase you run, inspect, and extend—aligned with the book’s theory chapters.

**You can run this project:**

- **On your machine** with a local runtime such as **Ollama** (fully private, no cloud required), or  
- **With hosted models** (e.g. **ChatGPT**, **Claude**, or similar APIs) when you prefer speed or don’t have local GPU—same code shape, different model backend.

The default implementation path is **plain Python first**; frameworks appear later only as optional comparisons so learning stays honest and you don’t hide behind abstractions too early.

### How the project grows

The project grows in **stages**. Each stage gives you something real to run, inspect, and test. The system is **not** rebuilt from scratch each time—it **evolves** step by step, so you see how a simple model call becomes a real agent.

---

### Step 0 — A bare model call

**Goal:** Make the stack feel real immediately—and make the limitations visible.

**Result:** The smallest program that sends a prompt to a model and gets a response. No loop, tools, memory, or planning yet. Exciting because it works; underwhelming because it’s only a single exchange—that contrast is the baseline.

**Tools:** Python environment + a model interface. You may start with a remote API for simplicity, then swap in a local model later.

**Knowledge:** Not “how to build an agent” yet—but what a model **alone** can and cannot do. That insight is required before later steps.

**Ready to move on:** You can run a prompt, get a response, change the prompt, and see that the system still feels like a **one-shot** interaction, not a persistent process.

---

### Step 1 — A stable project skeleton

**Goal:** Stop treating the program as a script; treat it as a **system**.

**Result:** A small codebase (not one file): model access separated from app logic, room for configuration and future components—not “smarter” yet, but **cleaner**.

**Tools:** Folders, modules, environment variables, config files, a simple class or interface for the model.

**Knowledge:** Architecture matters for how easily the system can grow.

**Ready to move on:** You can swap prompts or model backends without rewriting the whole project; it feels like the start of a real app.

---

### Step 2 — The first agent loop

**Goal:** Turn a one-shot call into a **loop**: act, update state, continue.

**Result:** The first behavior over time—still primitive, but no longer static. Multiple steps in sequence.

**Tools:** Python control flow, a simple state object, prompt assembly. Still no real-world actions.

**Knowledge:** Intelligence here comes from **iteration and feedback**, not only from model quality.

**Ready to move on:** You can assign a task, watch more than one step, inspect history, and explain why the loop differs from a one-shot call.

---

### Step 3 — Structured outputs and action parsing

**Goal:** Move from vague prose to outputs the system can **interpret reliably**.

**Result:** Structured responses (e.g. JSON-like actions) and a parser that turns model output into behavior—less chatbot, more **process**.

**Tools:** Prompt design, lightweight schemas, parsing, validation, error handling.

**Knowledge:** Action needs **structure** at the boundary between language and execution.

**Ready to move on:** Valid structured outputs most of the time, recovery from formatting mistakes, consistent machine-readable intent.

---

### Step 4 — The first tools

**Goal:** Let the agent affect or inspect something **outside** the prompt.

**Result:** First real tools (e.g. read/list files, controlled writes). The agent doesn’t only talk about files—it can **use** them.

**Tools:** File I/O, a tool registry, a dispatcher from parsed actions to functions, light safety constraints.

**Knowledge:** Tools are the bridge from language to the world—and must be shaped carefully.

**Ready to move on:** The agent can choose a tool, run it, feed the result into the next loop step.

---

### Step 5 — Real feedback through command execution

**Goal:** Add **grounded** interaction: run tests, scripts, commands—inspect real behavior.

**Result:** A rough but real **coding-agent prototype**: inspect a project, run commands, respond to output.

**Tools:** Subprocess execution, safe wrappers, logging, stronger validation. The environment becomes part of the architecture.

**Knowledge:** Grounded feedback is what makes agents **practically** powerful.

**Ready to move on:** A simple coding task where the agent reads files, runs a command, and meaningfully feeds output back into the loop.

---

### Step 6 — Memory and retrieval

**Goal:** Address **context pressure** as steps and interactions accumulate.

**Result:** Memory outside the immediate prompt + retrieval that decides what to bring back—not full “long-term intelligence” yet, but no full reset every few turns.

**Tools:** Persistent state, history, a retrieval layer; start naive (e.g. simple store/search), then compare embeddings / vector DBs if useful.

**Knowledge:** Memory is a **selection** problem—what to retrieve, when—not just storage.

**Ready to move on:** The system uses information from earlier steps or files without stuffing everything into the live prompt.

---

### Step 7 — Planning and task decomposition

**Goal:** Move from pure reactivity to **direction**: explicit planning and decomposition.

**Result:** A visible sense of what the system is trying to complete—not only the next plausible step.

**Tools:** Plan prompts, plan state, revision logic, tighter integration between loop state and task structure.

**Knowledge:** Planning is direction over time; plans are **hypotheses** and must update when reality changes.

**Ready to move on:** You can see a plan, act on it, revise it, and distinguish reacting from working through a structure.

---

### Step 8 — A more capable coding agent

**Goal:** Unify loop, tools, memory, and planning around a **real codebase** use case.

**Result:** A single-agent coding assistant that inspects a repo, takes several steps, remembers prior results, and acts with some direction—not only reaction.

**Tools:** Everything built so far, integrated; optional safer patching or code search.

**Knowledge:** **Synthesis**—earlier ideas stop being separate lessons and become one system.

**Ready to move on:** A bounded real task in a sample project with a meaningful multi-step workflow.

---

### Step 9 — Multi-agent extension

**Goal:** Extend the system—don’t replace it—with **roles** (e.g. planner, executor, evaluator).

**Result:** Work can split across agents instead of one loop carrying every responsibility.

**Tools:** Orchestration, role prompts, shared or partitioned memory, inter-agent message formats.

**Knowledge:** Multi-agent design is about **structural** separation of responsibilities, not impressiveness.

**Ready to move on:** Two or more agents coordinate and you can contrast single- vs multi-agent behavior meaningfully.

---

### Step 10 — Production hardening

**Goal:** Shift from educational prototype toward something you can **operate**: reliability, observability, bounded behavior.

**Result:** A system you can monitor, debug, constrain, and trust more realistically—not only “capable.”

**Tools:** Logging, tracing, limits on loop depth, error handling, inspection hooks; optional framework comparisons **after** you understand what they abstract.

**Knowledge:** The last mile is often **stability** under imperfect conditions, not raw cleverness.

**Ready to move on:** Repeated runs, inspectability of execution, and treating success and failure as **system** behavior—not magic.

---

## How the reader experiences progress

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

## What you need before starting

The build track assumes you know **Python**, not AI engineering:

**You need:** a Python environment, comfort running scripts, basic functions/files, and willingness to debug your setup.

**You don’t need:** prior ML training, heavy math, or familiarity with AI frameworks—those arrive only when they earn their place.

---

## Why this structure works

The book teaches **understanding**. The build track teaches **embodiment**. You don’t only read about loops, tools, memory, and planning—you build the system in an order that makes each piece **necessary**. That coherence is what keeps theory and practice from feeling like two different books.

---

## Newsletter / email capture

Email capture comes later. For now, you can track progress through the SEO site fragments and chapter pages.

## Next step

Start with the companion fragments here:

- [howaiagentswork.com — English home](https://howaiagentswork.com/en/)

You can revisit this site later for a `donate` / `support` page when monetization decisions are finalized.

---

*Optional next editorial pass: tighten each step into a single blueprint block (Goal / Result / Tools / Knowledge / Ready-to-move-on) for Chapter 0 or the companion repo README.*
