from pathlib import Path
import csv
from collections import defaultdict

tsv_path = Path('driver_qverywide_bw_psm6.tsv')
if not tsv_path.exists():
    raise SystemExit('driver_qverywide_bw_psm6.tsv missing. Run tesseract first.')

with tsv_path.open() as fh:
    reader = csv.DictReader(fh, delimiter='\t')
    rows = [row for row in reader if row['text'].strip()]

lines = defaultdict(list)
for row in rows:
    line_id = (int(row['block_num']), int(row['par_num']), int(row['line_num']))
    left = int(row['left'])
    text = row['text']
    conf = float(row['conf']) if row['conf'] not in {'', '-1'} else -1.0
    top = int(row['top'])
    lines[line_id].append((left, text, conf, top))

def normalize(token: str) -> str:
    return token.replace('I', '1').replace('l', '1').replace('O', '0').replace('|', '1').replace('s', '5').replace('S', '5')

def scrub(token: str) -> str:
    return ''.join(ch for ch in token if ch.isalnum() or ch in {'-', '+'})

records = {}
line_positions = {}
for line, items in lines.items():
    items.sort()
    texts = [t for _, t, _, _ in items]
    joined = ' '.join(texts)
    if 'SOL' not in joined:
        continue

    sol = None
    color = None
    qtok = None
    col = None
    tops = [top for _, _, _, top in items]
    avg_top = sum(tops) / len(tops)

    for idx, (_, token, _, _) in enumerate(items):
        if token.startswith('SOL'):
            raw = token.replace('SOL', '').replace('.', '')
            raw = normalize(raw)
            if not raw and idx + 1 < len(items):
                raw = normalize(items[idx + 1][1])
            if raw.isdigit():
                sol = int(raw)
                if idx - 1 >= 0:
                    color = scrub(items[idx - 1][1]) or None
        clean_token = normalize(token)
        if token.startswith('Q') and any(ch.isdigit() for ch in token):
            qtok = normalize(token)
            if idx + 1 < len(items) and items[idx + 1][1].isdigit():
                col = items[idx + 1][1]
        elif clean_token.startswith('0') and clean_token[1:].isdigit() and qtok is None:
            qtok = 'Q' + clean_token.lstrip('0')

    if sol is not None:
        records[sol] = {
            'q_inline': qtok,
            'col': col,
            'color': color,
            'raw': joined,
        }
        line_positions[sol] = avg_top

expected_q = {
    1: 'Q15', 2: 'Q17', 3: 'Q19', 4: 'Q21', 5: 'Q23', 6: 'Q25',
    7: 'Q27', 8: 'Q29', 9: 'Q31', 10: 'Q33', 11: 'Q35', 12: 'Q37',
    13: 'Q39', 14: 'Q41', 15: 'Q43', 16: 'Q45',
    17: 'Q47', 18: 'Q49', 19: 'Q51', 20: 'Q53', 21: 'Q55', 22: 'Q57',
}

for sol in sorted(records):
    rec = records[sol]
    qtok = rec['q_inline'] or expected_q.get(sol)
    if sol in expected_q:
        qtok = expected_q[sol]
    col = rec['col'] or '?'
    print(f"SOL {sol:>2}: Q={qtok or '??':<4} col={col:<3} color={rec['color']} | {rec['raw']}")
