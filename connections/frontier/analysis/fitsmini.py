#!/usr/bin/env python3
"""Minimal FITS binary-table reader (numpy only) for Fermi-LAT FT1/FT2 files: header cards and fixed-width BINTABLE columns."""
from __future__ import annotations

from pathlib import Path

import numpy as np

TFORM = {"L": ("u1", 1), "B": ("u1", 1), "I": (">i2", 2), "J": (">i4", 4), "K": (">i8", 8), "E": (">f4", 4), "D": (">f8", 8), "A": ("S1", 1)}


def headers(raw: bytes) -> list[tuple[int, dict, int]]:
    """Return (header_start, cards, data_start) for each HDU."""
    out, pos = [], 0
    while pos < len(raw):
        cards, start = {}, pos
        while True:
            block = raw[pos:pos + 2880]
            if len(block) < 2880:
                return out
            pos += 2880
            done = False
            for i in range(0, 2880, 80):
                card = block[i:i + 80].decode("ascii", errors="replace")
                key = card[:8].strip()
                if key == "END":
                    done = True
                    break
                if card[8:10] == "= ":
                    val = card[10:].split("/")[0].strip() if not card[10:].strip().startswith("'") else card[10:].split("'")[1]
                    cards.setdefault(key, val)
            if done:
                break
        data_start = pos
        nbytes = int(cards.get("NAXIS1", 0)) * int(cards.get("NAXIS2", 0)) if int(cards.get("NAXIS", 0)) >= 2 else 0
        nbytes += int(cards.get("PCOUNT", 0) or 0)
        out.append((start, cards, data_start))
        pos = data_start + ((nbytes + 2879) // 2880) * 2880
    return out


def read_table(path: Path, extname: str, columns: list[str]) -> dict[str, np.ndarray]:
    raw = Path(path).read_bytes()
    for _, cards, data_start in headers(raw):
        if cards.get("EXTNAME", "").strip() != extname:
            continue
        nrow, width, nf = int(cards["NAXIS2"]), int(cards["NAXIS1"]), int(cards["TFIELDS"])
        names, fields, offset = [], [], 0
        for k in range(1, nf + 1):
            form = cards[f"TFORM{k}"].strip()
            rep = int("".join(c for c in form if c.isdigit()) or 1)
            code = next(c for c in form if c.isalpha())
            names.append(cards[f"TTYPE{k}"].strip())
            if code == "X":  # bit array: ceil(rep/8) bytes
                nb = (rep + 7) // 8
                fields.append((names[-1], ("u1", (nb,)), offset))
                offset += nb
                continue
            dt, size = TFORM[code]
            fields.append((names[-1], (dt, (rep,)) if rep > 1 and code != "A" else (f"S{rep}" if code == "A" else dt), offset))
            offset += size * rep
        assert offset == width, (offset, width)
        dtype = np.dtype({"names": [f[0] for f in fields], "formats": [f[1] for f in fields], "offsets": [f[2] for f in fields], "itemsize": width})
        rec = np.frombuffer(raw, dtype=dtype, count=nrow, offset=data_start)
        return {c: rec[c].astype(rec[c].dtype.newbyteorder("=")) if rec[c].dtype.kind != "S" else rec[c] for c in columns}
    raise KeyError(extname)


def keyword(path: Path, extname: str, key: str) -> str:
    raw = Path(path).read_bytes()
    for _, cards, _ in headers(raw):
        if cards.get("EXTNAME", "").strip() == extname:
            return cards.get(key)
    raise KeyError(extname)
