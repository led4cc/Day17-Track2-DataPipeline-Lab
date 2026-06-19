# Reflection — Day 17 (≤ 200 words)

Answer briefly, in your own words. This is graded on reasoning, not length.

1. **The flywheel.** Day 13 emitted agent traces; today you turned them into an
   eval set and DPO pairs that Day 22 will train on. Which step in
   `traces → Bronze → datasets` would break most silently in production if you
   got it wrong — and how would you detect it?

2. **Decontamination.** Your run dropped 2 of 3 preference pairs because their
   prompts were in the eval set. What concretely goes wrong if you *skip* this
   step and train on those pairs? How would the lie show up in your metrics?

3. **Point-in-time.** The naive join leaked a future `lifetime_spend` into the
   training row. Describe one feature in a system you know that would be
   dangerous to join without an `ASOF`/point-in-time guard.

4. **Graph vs vector.** From `kg_demo.py`, name one question the knowledge graph
   answers well that flat chunk retrieval (`embed.py`) would struggle with, and
   one where the graph is overkill.

_Write your answers below._

The quietest failure would be flattening traces incorrectly. If parent/child spans
lose `trace_id`, `split`, or root status, the Bronze table still looks populated,
but eval rows, costs, and preference pairs become wrong. I would detect it with
span-count checks, one-row-per-root trace summaries, and alerts when eval/pair
counts suddenly drift.

Skipping decontamination means the model trains on the same prompts used for
grading. Offline eval would look better because the model memorized benchmark
answers, not because it generalized. The lie would show up as high eval scores
but weak performance on new production prompts or a fresh holdout set.

A dangerous feature is a user's "total spend" or "risk score" in an e-commerce
or finance system. If I join the latest value instead of the value known at the
event time, the model sees purchases, refunds, or fraud decisions that happened
after the prediction moment.

The knowledge graph answers the multi-hop question "where does a widget ship
from?" because it can traverse widget -> accessory -> Hanoi fulfillment center.
Flat chunk retrieval struggles because the facts live in separate chunks. The
graph is overkill for a single-hop lookup like "what is the widget return window?"
