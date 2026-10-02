## Coding: least code that's correct
- Read the task and trace the real flow first. Then stop at the first rung that holds: not needed → already in codebase → stdlib/platform → installed dependency → one line → minimum new code.
- Bug fix = root cause: grep every caller and fix the shared function once.
- No unrequested abstractions or new dependencies. Prefer deletion and the shortest working diff. Match existing conventions.
- Mark deliberate shortcuts: `ponytail: <ceiling>; upgrade to <path>`.
- Never skimp on validation at trust boundaries, security, data-loss handling. Non-trivial logic gets one runnable check.
