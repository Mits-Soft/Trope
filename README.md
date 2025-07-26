
---

# Trope DSL

Trope is a semantic description language designed to represent complex, modular structures through symbolic and expressive syntax. It supports modeling abstract systems such as logic frameworks, narrative architectures, and interactive environments.

## ✨ Highlights

- Domain-Specific Language (DSL) focused on structure, relationships, and attributes  
- Syntax defined via `trope.dsl.ebnf`, with support for live interpretation or compilation  
- Extensible schema system (`specs/schemas/`) enabling custom behaviors and validation  
- Ideal for prototyping narrative engines, structural generators, or logic graphs  

## 📁 Repository Structure

- `examples/`: Usage scenarios written in `.dscr`, with Python-powered demos  
- `specs/`: Grammar definition, schemas, syntax highlighting (`.tmLanguage.json`)  
- `docs/`: Conceptual notes and abstract descriptions  
- `vscode-extension/`: Extension for VSCode with language config, snippets, and support for `.dscr`  

## 🚀 Getting Started

Clone the repository and explore the `examples/` folder to understand the syntax and potential applications.

> git clone https://github.com/Mits-Soft/Trope.git  
> cd trope-dsl/examples

Use `ex.py` inside `notifier/` as a minimal interpreter.

## 🔌 VSCode Extension

Install the `.vsix` file in `vscode-extension/` to get DSL support in your editor.

> In VS Code:  
> Ctrl+Shift+P → Extensions: Install from VSIX → Select `trope-dsl-0.0.2.vsix`

Includes syntax highlighting, snippets, and schema integration.

## 📚 Documentation

Detailed guides and abstract notes are available in `docs/`.  
The DSL grammar can be found in `specs/trope.dsl.ebnf`.

## 🧪 Schemas

All supported structure types and semantic properties are defined in JSON Schema format under `specs/schemas/`.

## ⚖️ License

This project is licensed under the MIT License. See `LICENSE` for details.

---
