# Using AI After the Course

AI assistants (ChatGPT, Claude, Cursor, Copilot, etc.) can speed up learning — or short-circuit it.
This course gave you Python fundamentals; these notes help you use AI **without** replacing your own judgment.

---

## Default stance

- **You** run the code, read the error, and decide if the answer makes sense.
- **AI** explains concepts, compares options, and helps you debug — not replaces practice.

The templates in [learning_prompts.md](learning_prompts.md) are written for that balance. Start there.

---

## Good uses

| Task | Example prompt style |
|------|----------------------|
| Understand a concept | learning_prompts Prompt 1 |
| Compare libraries | Prompt 2 |
| Explain an error | Prompt 6 |
| Plan a feature | Prompt 7 |
| Review your code (no rewrite) | Prompt 5 |
| Match an existing codebase | Prompt 3 |

Paste **minimal** code and the **full traceback**. Say “do not fix it for me” when you are learning.

---

## Risky uses

| Avoid | Why |
|-------|-----|
| “Write my whole lab / script” | You miss the muscle memory the course built |
| Pasting confidential data | Internal parameters, credentials, unpublished results |
| Accepting code you cannot explain | Hard to maintain and debug in production |
| Skipping tests | AI code often misses edge cases — use pytest (Lab 11) |

At CERN and similar environments: treat prompts like email — **no secrets, no export-controlled or sensitive payloads** unless your organisation explicitly allows it in that tool.

---

## Workflow when stuck

1. Read the traceback ([python_quick_reference.md](python_quick_reference.md)).
2. Check official docs for the module involved.
3. Try a one-line experiment in the REPL.
4. Use a learning prompt (explain / debug / scope — not “solve”).
5. Apply the **smallest** change yourself and re-run.

---

## AI + concurrency + data

AI often suggests `threading` for speed. For Python:

- CPU-bound pure Python → processes ([threads_vs_processes.md](threads_vs_processes.md))
- NumPy/pandas → vectorise first
- Ask AI *why* it chose threads vs processes; wrong advice is common

---

## Related resources

- [learning_prompts.md](learning_prompts.md) — copy-paste prompts
- [python_quick_reference.md](python_quick_reference.md) — docs and tracebacks
- [POST_COURSE.md](POST_COURSE.md) — full index of post-course material
