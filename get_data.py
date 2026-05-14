from datasets import load_dataset
from pathlib import Path

ds = load_dataset("bentrevett/multi30k")
out = Path(".data/multi30k")
out.mkdir(parents=True, exist_ok=True)
for split in ("train", "validation", "test"):
    with open(out / f"{split}.de", "w", encoding="utf-8") as f_de, open(out / f"{split}.en", "w", encoding="utf-8") as f_en:
        for ex in ds[split]:
            f_de.write(ex["de"].strip() + "\n")
            f_en.write(ex["en"].strip() + "\n")
print("wrote files to", out)
print(sorted(p.name for p in out.iterdir()))