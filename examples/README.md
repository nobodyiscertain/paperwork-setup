# Examples

Materialized output of what `PAPERWORK.md` Step 9 generates.

## `sample-system/`

A complete sample with everything enabled (`has_dashboard=true`, `has_library=true`, `has_daily_bookends=true`) so you can see what the lightweight dashboard actually looks like.

To regenerate the dashboard:

```bash
cd examples/sample-system
python3 dashboard/render.py
open dashboard/index.html       # or xdg-open / start
```

To run the markdown doctests:

```bash
cd examples/sample-system
python3 -m doctest dashboard/_markdown.py -v
```

The fixtures (`journal/`, `library/`) are hand-written stand-ins for what slash commands would produce in a real installation. The same `render.py` and `_assets/` files in this example are the ones embedded as TEMPLATE blocks in `PAPERWORK.md` Step 9.

Not meant to be run as a real management system — just reference output for design review and regression-checking.
