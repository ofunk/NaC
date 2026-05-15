# NoC KG Editor

Installable local Codex plugin for notaries and notary-office staff. It opens
usecase-local knowledge graphs as safe forms and checklists instead of requiring
raw JSON edits.

## Status

Installable local MVP. The plugin wraps the existing NoC KG editor runtime and
keeps the source of truth in the repository:

- `usecases/<slug>/knowledge-graph.graph.json`
- `usecases/<slug>/knowledge-graph.md`

The editor is proposal-only. It does not store mandate values, personal data,
health data, estate data, secrets or portal credentials in Git.

## Open A Usecase

From the repository root:

```powershell
python plugins\noc-kg-editor\scripts\open_editor.py adoption-familienrechtliche-erklaerungen
```

For JSON, suitable for a ChatGPT App, GPT Action or local UI bridge:

```powershell
python plugins\noc-kg-editor\scripts\open_editor.py adoption-familienrechtliche-erklaerungen --format json
```

For a Markdown session sheet that can be linked from a usecase README:

```powershell
python plugins\noc-kg-editor\scripts\open_editor.py adoption-familienrechtliche-erklaerungen --format markdown --output out\kg-editor\adoption-familienrechtliche-erklaerungen.md
```

## Editor Model

The editor view exposes four notary-facing tabs:

- open information,
- documents,
- decisions,
- gates and evidence.

The plugin exposes the same action names as the workflow contract:

- `get_graph`
- `propose_patch`
- `validate_graph_patch`
- `create_pull_request`

Only the local CLI and session-sheet surface are implemented in this MVP. Public
ChatGPT/App integration remains a later channel and must keep OAuth, AVV/DPA,
TLS, consequential-action confirmation and local-workstation boundaries separate
from real mandate data.

## Boundary

- Runs locally from this repository.
- Uses the existing `notary_kg.editor` runtime.
- Produces safe views and Markdown/JSON session sheets.
- Requires human confirmation before any patch or pull request.
- Keeps real client, mandate, health, family, property, estate and secret values
  out of Git and out of LLM-visible files.

