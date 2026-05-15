# Positioning: Notariat as Code, NoC and Enterprise Control Plane

Status: binding project positioning

Last content update: 2026-05-15

## Purpose

This document is not an old concept note. It is the binding terminology for the
current NoC state. It separates the target model, operating principle, product
name and implemented repository surfaces.

The current development state is maintained in [roadmap/BUILD_NOW.md](../../roadmap/BUILD_NOW.md).

## Terminology

| Term | Meaning in this repository |
| --- | --- |
| `Notariat as Code` | Target model: notarial case types, roles, approvals, evidence, plugins and workflows are described declaratively, versioned and verifiably. |
| `NoC` | Concrete reference implementation of that target model in this repository. |
| `Enterprise Control Plane` | Platform name for the operating, control and execution layer of NoC. |
| `Enterprise GitOps` | Operating principle: changes move through branch, pull request, review, approval, checks and merge. |

`Organization as Code` remains the broader category. This repository is the
notary-specific form: `Notariat as Code`.

## What Is Concrete Today

NoC is no longer only documentation. On `main` as of 2026-05-15, it has a first
executable notary-specific runtime surface:

- case-local static knowledge graphs under [usecases/](../../usecases), each as
  `knowledge-graph.graph.json` and `knowledge-graph.md`,
- KG validation through [scripts/validate_knowledge_graph.py](../../scripts/validate_knowledge_graph.py),
- a notarial KG runtime under [src/notary_kg/](../../src/notary_kg),
- a CLI under [scripts/notary_kg.py](../../scripts/notary_kg.py),
- a no-code KG editor view for subject-matter staff with its contract in
  [workflows/contracts/kg-editor.contract.json](../../workflows/contracts/kg-editor.contract.json),
- a strict quality gate through [scripts/quality_gate.py](../../scripts/quality_gate.py).

The product structure is binding:

- [plugins/](../../plugins): installable plugin artifacts,
- [workflows/](../../workflows): skills, workflow contracts and deterministic
  Python workflows,
- [usecases/](../../usecases): concrete notarial case types with their own
  static KG/DB.

## What Is Not Claimed

NoC does not replace a required professional system or notarial professional
review. The repository also does not currently claim:

- production-ready end-to-end automation for notarial matters,
- uncontrolled SaaS processing of mandate data,
- replacement of XNP, card-reader, morris or register-portal obligations,
- subject-matter truth through an LLM without versioned change, review and
  approval.

The LLM is an input interface. A state becomes binding only through versioned
change, validation, review, merge and evidence.

## Architecture Mapping

| Layer | Job | Current repository surfaces |
| --- | --- | --- |
| Intent Layer | business intent, policies, roles, usecases | [policies/](../../policies), [usecases/](../../usecases), [prompts/en/](../../prompts/en) |
| Control Layer | branch, pull request, review, approval, rulesets | [AGENTS.md](../../AGENTS.md), [.github/copilot-instructions.md](../../.github/copilot-instructions.md), [.cursor/rules/](../../.cursor/rules) |
| Execution Layer | deterministic runtime and workflow execution | [src/](../../src), [scripts/](../../scripts), [workflows/](../../workflows) |
| Evidence Layer | evidence, SBOM, eventstream, Gantt progress | [sbom/](../../sbom), [docs/en/eventstream/](eventstream), [roadmap/GANTT.md](../../roadmap/GANTT.md) |

## Product Promise

Notarial case types, plugins, workflows, roles, approvals and evidence run
declaratively, auditable and automated through Git, without letting subject
matter or operations bypass the compliance chain of branch, review, check and
merge.

## One-Sentence Pitch

Notariat as Code is an operating model in which notarial case types, plugins,
workflows, policies and operational changes are described declaratively in Git
and moved into verifiable execution through an Enterprise Control Plane.
