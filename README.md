# ClioAgent

ClioAgent is a focused fork of Microsoft GraphRAG for IB History. It connects
historical evidence from textbooks and academic papers with explicitly attributed
historiographical interpretations.

> No identifiable historian or author, no source context, no named
> historiographical claim. Page numbers are shown only when present in the input.

## What this fork changes

- Adds `HISTORIAN`, `HISTORICAL_EVENT`, `HISTORICAL_EVIDENCE`, and
  `INTERPRETATION` graph entities.
- Restricts graph relations to `ARGUES`, `SUPPORTED_BY`, `CHALLENGES`,
  `QUALIFIES`, and `RELATES_TO` labels.
- Adds source-strict IB History extraction and answer prompts.
- Adds the `clioagent` command while retaining the GraphRAG engine internally.
- Removes the upstream documentation site, unified-search demo, release tooling,
  CI configuration, notebooks, and large upstream test suite.
- Keeps all GraphRAG engine packages required for indexing and retrieval.

## Requirements

- Python 3.11, 3.12, or 3.13
- [uv](https://docs.astral.sh/uv/) for the bundled workspace
- an OpenAI API key
- legally obtained source material

GraphRAG 3.3.0 does not support Python 3.14.

## Install

From the repository root:

```bash
uv sync --all-packages
cp .env.example .env
```

Add your API key to `.env`, then activate the environment:

```bash
source .venv/bin/activate
```

## Add data

The `data/` directory is intentionally empty. Put processed `.txt` or `.md`
documents directly inside it. It is ignored by Git to prevent accidental upload
of textbooks and subscription papers.

Each document should preserve metadata and page markers:

```text
TITLE: Example Book
AUTHOR: Jane Smith
YEAR: 2022
DOCUMENT_TYPE: textbook

[PAGE 42]
Document text begins here...
```

Do not upload copyrighted source documents, generated indexes, API keys, or
GraphRAG caches to GitHub.

## Run

```bash
uv run clioagent index
uv run clioagent query "To what extent did economic conditions cause the regime's fall?"
uv run clioagent query --method global "What are the major debates across this corpus?"
```

Use local search for focused evidence or an individual interpretation. Use global
search for themes and debates across the complete corpus. Begin with a small
corpus because standard GraphRAG indexing can use substantial model tokens.

## Repository layout

```text
clioagent/
├── data/                    # private corpus; ignored by Git
├── prompts/                 # IB History prompts
├── packages/clioagent/      # ClioAgent command
├── packages/graphrag*/      # retained GraphRAG engine packages
├── settings.yaml            # ready-to-edit project configuration
└── tests/                    # ClioAgent-specific smoke tests
```

## Attribution

ClioAgent contains modified and redistributed portions of Microsoft GraphRAG
3.3.0, originally released under the MIT License. The original Microsoft
copyright and license are retained in `LICENSE` and source files.

Upstream: <https://github.com/microsoft/graphrag>

