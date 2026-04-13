---
lang: en
slug: index
template: home
url: en/
save_as: en/index.html
title: The AI Agents Book
summary: Understand how AI Agents work. Build your own AI Agent. Choose between a local or cloud, open source or SaaS. Learn from latest model AI leaks.
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

## Build track (`build-your-own-agent`) {#build-track-summary}

The hands-on **exercise track** (steps 0–10) lives on its own page so this home stays a light contract and roadmap.

**[Open the exercise track →](/en/exercise/)** — jump links and the full write-up.

---

## Where to read next {#read-next}

Start with the companion fragments when you want chapter-length depth:

- [English — How AI agents work](https://howaiagentswork.com/en/) — fragments and long-form notes  
- [Español](https://howaiagentswork.com/es/) — same project, Spanish entry point  

Email capture and donations can layer on later; for now, progress is visible through the companion site and this roadmap.

---

*Optional editorial pass: tighten each step into a single blueprint block (Goal / Result / Tools / Knowledge / Ready-to-move-on) for Chapter 0 or the companion repo README.*
