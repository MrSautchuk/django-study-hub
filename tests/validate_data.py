"""Valida dados estáticos. Ferramenta de manutenção, não é necessária para usar o site."""
import json
from pathlib import Path
r = Path(__file__).resolve().parents[1] / 'data'
def load(name):
    return json.loads((r / (name + '.json')).read_text(encoding='utf8'))
categories = load('categories')
entries = [entry for cat in categories for entry in load(cat['id'])]
didatica, p3, p3ctx, guide = map(load, ('didatica', 'prova-p3', 'p3-context', 'guia'))
ids = [entry['id'] for entry in entries]
assert len(ids) == len(set(ids)), 'IDs duplicados'
assert set(ids) == set(didatica), 'Falta contexto didático para alguma entrada'
for e in entries:
    d = didatica[e['id']]
    assert all(d.get(k) for k in ('scenario', 'prerequisites', 'breakdown', 'connection', 'expected', 'practice'))
    assert all(d['location'].get(k) for k in ('file', 'folder', 'action', 'responsibility'))
    assert all(ref in ids for ref in e.get('related', [])), f"Referência inválida: {e['id']}"
for step in p3:
    for section in step['sections']:
        if section['code']:
            c = p3ctx[f"{step['number']}/{section['label']}"]
            assert all(c['location'].get(k) for k in ('file', 'folder', 'action', 'responsibility'))
            assert c['breakdown']
for step in guide:
    for part in step['parts']:
        assert all(part['location'].get(k) for k in ('file', 'folder', 'action', 'responsibility'))
        assert part['code'] and part['explain']
print(f'OK: {len(entries)} tópicos, {len(p3)} etapas P3, {len(guide)} passos guiados.')
