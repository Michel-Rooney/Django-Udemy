## Urls.py
app_name = 'recipes': Namespace para urls Ex.: recipes:home

## {% for %}
{% empty %} : Se caso tiver vazio imprima isso

## Test
**Instalar:** pip install pytest pytest-django <br>
**pytest -rP:** Mostra as capturas na execução do test <br>
**pytest -k 'nome do test':** Executa um test especifico <br>
**self.fail():** Fazer seu teste falhar pra lembrar <br>
**from unittest import skip** <br>
- **@skip('WIP') - Work in progress**
**coverage:**
- pip install coverage
- .coveragerc
- coverage run -m pytest
- coverage html

## Outros
python manage.py shell : Shell interativo do django <br>
recipe._meta.get_fields() <br>
### Duplicar receita
1. recipe.id = None
2. recipe.save()
### Gerador de senhas
python -c "import string as s;from random import SystemRandom as sr;print(''.join(sr().choices(s.ascii_letters + s.punctuation, k=64)))"
### Session
request.session['algo'] : Trabalho com os cookies do navegador apartir da sessão dele