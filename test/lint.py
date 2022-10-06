"""modulo de teste lint"""
import sys
from pylint import lint

THRESHOLD = 9

run = lint.Run(['/home/dagoberto/Documentos/TESTE_CRUD/crud_post_video/model/model.py'],
               do_exit=False)
score = run.linter.stats['global_note']
if score < THRESHOLD:
    print('Linter failed')
    sys.exit(1)

sys.exit(0)
