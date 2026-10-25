# WTFactory — Workshops and Trainings Factory: the public catalog


The public landing page at https://uipath-practice.github.io/ . Lists every course and exercise with audience, level, products and prerequisites, the workshop compositions, and a product-coverage grid.

`catalog.yaml` and `workshops.yaml` are **generated** by `tools/build-catalog.py` from each course cookbook's `exercise.yaml` files and from `catalog/catalog.manual.yaml` (courses whose cookbook is elsewhere). To add or change a course you do not own a cookbook for, open a PR against `catalog/catalog.manual.yaml`; the next catalog build lands here. Pages are plain Markdown with Jinja loops (`mkdocs-macros`), so a catalog change needs no page edit.

```bash
uv venv .venv && uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/mkdocs serve
```
