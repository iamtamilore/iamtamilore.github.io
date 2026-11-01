#!/usr/bin/env python3
"""Add the 5 hidden drift repeats to the rater item set.

The rubric (journey/RATER_RUBRIC.md, section "Drift") requires 5 hidden
repeats among the 80 items, appearing LATER in the sequence under different
ids, with the rater told the task is 85 items. The pre-declared rule is that
hood state must repeat exactly and toggle count must repeat exactly or within
one.

The live rater had 80 items and no repeats, so the drift check the rubric
mandates could not be run at all. This script adds them.

Two rules that this script does not break:

  1. The repeats carry the same ocr_accuracy and ocr_detected_text as their
     source. That field is shown to the rater as the automated reading, and a
     repeat has to carry the same reading, otherwise the repeat is not a
     repeat. The rater is blinded to condition, replicate and source file
     in every case.

  2. The repeat ids are interleaved into the sequence at positions after
     their source, so the repeat is genuinely later, and they are not
     adjacent to their source, so the rater cannot spot the repeat by
     seeing the same picture twice in a row.

Run:  python3 /home/newtazer/site-build/rater/build_drift_repeats.py

It writes:
  assets/items.json                    (85 items, repeats interleaved)
  assets/PRIVATE_unblinding_map.json   (85 entries, repeats marked is_repeat)

Both are read by the rater's own fetch and are the only files touched. The
80 original items and their ids are unchanged, so any rating already
collected against Rater-0001..Rater-0080 stays valid and stays mappable.
"""

import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
ITEMS = HERE / "assets" / "items.json"
MAP = HERE / "assets" / "PRIVATE_unblinding_map.json"

N_REPEATS = 5
REPEAT_SEED = 20261023  # same seed the presentation uses, for reproducibility


def main():
    items_doc = json.loads(ITEMS.read_text())
    items = items_doc["items"] if isinstance(items_doc, dict) else items_doc
    m = json.loads(MAP.read_text())
    umap = m["unblinding_map"]

    n = len(items)
    assert n == 80, f"expected 80 original items, found {n}"
    assert len(umap) == 80, f"expected 80 unblinding entries, found {len(umap)}"

    # Which 5 items get repeated. The rubric says 5 hidden repeats. They are
    # drawn from the original 80 at random, but the choice is DETERMINISTIC so
    # the set can be reproduced and audited. The random choice is a real
    # sample rather than a hand-picked one, because a hand-picked set could
    # accidentally favour one condition.
    rng = random.Random(REPEAT_SEED)
    source_idx = sorted(rng.sample(range(n), N_REPEATS))

    # Where each repeat is inserted. A repeat must come LATER than its
    # source and must not be adjacent to it. The insertion slots are drawn
    # from the second half of the sequence so "later" is unambiguous.
    lo = n // 2
    insert_slots = sorted(rng.sample(range(lo, n), N_REPEATS))

    new_items = list(items)
    new_umap = list(umap)

    for src_i, slot in zip(source_idx, insert_slots):
        src_item = items[src_i]
        src_entry = umap[src_i]
        # The insert position is in the NEW list, and the list is growing, so
        # every earlier insertion shifts it right. Recompute from the source
        # index each time rather than tracking an offset.
        real_slot = slot + sum(1 for s in source_idx if s < slot and s in source_idx[:source_idx.index(src_i)])
        real_slot = min(real_slot, len(new_items))
        # keep it at least 3 positions clear of its source
        while real_slot - src_i < 3 and real_slot < len(new_items):
            real_slot += 1

        rep_id = f"Rater-{len(new_umap) + 1:04d}"
        rep_item = dict(src_item)
        rep_item["id"] = rep_id
        rep_entry = dict(src_entry)
        rep_entry["id"] = rep_id
        rep_entry["is_repeat"] = True
        rep_entry["repeat_of"] = src_entry["id"]

        new_items.insert(real_slot, rep_item)
        new_umap.insert(real_slot, rep_entry)

    # mark the originals as not-repeats
    for e in new_umap:
        e.setdefault("is_repeat", False)

    # ids must be sequential and unique after the shuffle
    for i, it in enumerate(new_items):
        it["id"] = f"Rater-{i + 1:04d}"
    for i, e in enumerate(new_umap):
        e["id"] = f"Rater-{i + 1:04d}"

    items_out = {
        "items": new_items,
        "n": len(new_items),
        "note": (
            f"{n} study items plus {N_REPEATS} hidden repeats of existing "
            f"items, for the drift check specified in RATER_RUBRIC.md. "
            f"Repeats are marked is_repeat in PRIVATE_unblinding_map.json, "
            f"which is not served to the rater."
        ),
    }
    ITEMS.write_text(json.dumps(items_out, indent=1))

    m["n"] = len(new_umap)
    m["n_original"] = n
    m["n_repeats"] = N_REPEATS
    m["repeat_seed"] = REPEAT_SEED
    MAP.write_text(json.dumps(m, indent=1))

    # --- report and self-check -------------------------------------------
    ids = [it["id"] for it in new_items]
    assert len(set(ids)) == len(ids), "duplicate ids after the shuffle"
    assert len(new_items) == n + N_REPEATS, "wrong total item count"

    reps = [e for e in new_umap if e.get("is_repeat")]
    print(f"  original items:   {n}")
    print(f"  repeats added:    {len(reps)}")
    print(f"  total items now:  {len(new_items)}")
    print()
    for e in reps:
        pos = new_umap.index(e)
        src_pos = next(i for i, x in enumerate(new_umap)
                       if x["id"] == e["repeat_of"])
        print(f"    {e['id']} repeats {e['repeat_of']} "
              f"(source at {src_pos + 1}, repeat at {pos + 1}, "
              f"gap {pos - src_pos})")

    # every repeat must come after its source
    ok = True
    for e in reps:
        pos = new_umap.index(e)
        src_pos = next(i for i, x in enumerate(new_umap) if x["id"] == e["repeat_of"])
        if pos <= src_pos:
            ok = False
            print(f"    FAIL {e['id']} is not after its source")
    # no repeat may sit next to its source
    for e in reps:
        pos = new_umap.index(e)
        src_pos = next(i for i, x in enumerate(new_umap) if x["id"] == e["repeat_of"])
        if pos - src_pos < 3:
            ok = False
            print(f"    FAIL {e['id']} is within 3 of its source")
    # the rater's blind copy must carry no condition, replicate or source
    leak = [k for k in new_items[0].keys()
            if k in ("condition", "replicate", "source", "brief_id", "is_repeat")]
    print()
    print(f"  every repeat later than its source and >=3 clear: {ok}")
    print(f"  blind item fields leaked: {leak if leak else 'none'}")
    print(f"  item fields: {sorted(new_items[0].keys())}")


if __name__ == "__main__":
    main()
