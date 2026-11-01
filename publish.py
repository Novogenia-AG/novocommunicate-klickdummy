"""Kopiert den NovoCommunicate-Prototyp (v2) nach index.html und prüft, dass nur Demo-Kontaktdaten enthalten sind.
Aufruf: python publish.py  (danach commit + push)"""
import re
SRC = r"C:\Users\DanielWallerstorfer\Novogenia GmbH\DANIEL FILES - Dokumente\DANIEL FILES\AI CHAT BOT GENE-IUS\APP DESIGN\NOVOCOMMUNICATE\novocommunicate-v2.html"
s = open(SRC, encoding='utf-8').read()
s = s.replace(' (Prototyp v2)</title>', ' (Klickdummy)</title>', 1)
left = set(re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}', s)) - {'service@novogenia.com'}
assert all(re.search(r'@example(-[a-z]+)?\.(com|at)$', e) for e in left), left
assert not re.search(r'Djukanovic|Wassermann|Mladen|@novogenia\.com(?<!service@novogenia\.com)', s.replace('service@novogenia.com', ''), re.I)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok', len(s))
