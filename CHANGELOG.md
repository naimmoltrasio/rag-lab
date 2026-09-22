# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [2026-09-22]

### Added
- Connected vector retriever to the LLM chain, formatting retrieved
  documents as plain text before passing them as context

### Fixed
- Corrected CSV column name typo causing a KeyError in vector.py
- Fixed .gitignore pattern that didn't match the actual chroma db folder name

### Learned
- The difference between an application bug (fix) and repo tooling
  cleanup (chore) when naming commits

## [2026-09-21]

### Added
- Initial setup: downloaded ollama(llama3.2) and mxbai-embed-large embeddeding model.
- Configured a basic prompt call to the llm to check if works ok.

### Learned
- How does the indexation works (chunking, embedding, vector store) on a surface level.
- What is Ollama and how to install an LLM and a embedding model and configure a basic prompt.
