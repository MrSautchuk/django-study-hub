# Django Study Hub

Aplicação de consulta **estática**, em português, para a disciplina Desenvolvimento Web III. A busca e as preferências são locais; não há backend, login, LLM, API paga ou build. A versão da aplicação é uma base inicial curada, **não é uma documentação completa do Django**.

## Materiais analisados

- `Diagrama_Prova_P3_WebIII.pdf`, página 1: oito entregáveis, código no Forms e capturas de HTML, JSON e testes; prova individual, documentação oficial e sem IA.
- `IMPRIMIR_44_Caderno_de_Revisao_WebIII.pdf`, páginas 1–3: foco em ORM e templates; `filter` versus `get`; `clean_campo`; contexto de template; cenário Passeio.
- `[FATEC]-[WEBIII]-Aula14e15-2026.pdf`, páginas 1–26: revisão dos seis conceitos, API e simulado. Os slides agrupam os mesmos assuntos em cinco/seis blocos; o diagrama detalha **oito entregáveis**, ordem adotada aqui. O diagrama pede um ou mais testes passando; o hub oferece três camadas para praticar. A aula informa 120 minutos.
- O caderno simplifica dizendo que validação é do Form. Tecnicamente o Django também oferece validação de model via `full_clean()`, mas `save()` não a chama automaticamente; uma validação implementada somente no Form não protege gravações pelo ORM ou pela API. O problema de contexto divergente é **uma possível causa** de lista vazia, não a única.

Os materiais são usados para identificar exigências da disciplina, não como autoridade técnica. A documentação oficial do Django é a referência técnica para Django (série **5.2 LTS**); os materiais não especificam versão. Os links de cada entrada apontam ao assunto da documentação. Python, DRF e pytest-django são projetos separados e **não são especificados pela documentação Django**. Para não atribuir indevidamente seus comportamentos ao Django, o hub identifica esses trechos e oferece como referência complementar as documentações oficiais próprias. A versão ilustrativa do DRF é 3.16. Verifique a compatibilidade dos pacotes com sua versão de Python. A documentação de Django não valida por si só os exemplos de DRF ou pytest.

**Atenção:** o material recebido estabelece consulta apenas à documentação oficial durante a prova e proíbe IA. Este hub destina-se ao estudo prévio: não se deve presumir que seja permitido usá-lo na avaliação.

## Como executar e publicar

Abra a pasta do projeto com um servidor HTTP estático, por exemplo `npx serve .` ou a extensão Live Server do VS Code; abra o endereço indicado. Não é necessário Python para usar o hub. Apenas abrir `index.html` com `file://` pode bloquear a leitura dos arquivos JSON. É necessária rede para acessar os links externos e para carregar o site inicialmente; não há service worker nem garantia de funcionamento offline após carregamento.

Para publicar no GitHub Pages:

1. Envie o **conteúdo desta pasta** para a raiz de um repositório GitHub (inclusive `index.html`, `src/` e `data/`).
2. Em **Settings → Pages**, selecione **Deploy from a branch**, a branch desejada e a pasta `/ (root)`; salve.
3. Acesse a URL publicada informada pelo GitHub. Os recursos usam caminhos relativos; a navegação usa hash (`#/doc/filter`, por exemplo), permitindo links diretos mesmo em repositórios cujo site tem prefixo no caminho, sem configuração de rewrite do servidor.
4. Depois de modificar JSON ou código, faça commit e push. Não é necessário compilar o site.

Alternativamente, sirva esta pasta em qualquer hospedagem estática. Favoritos, pesquisas, histórico e tema ficam no `localStorage` do navegador, isolados por origem; limpar os dados do navegador os remove. As respostas do simulado não são persistidas nem corrigidas automaticamente.

## Base de conhecimento

`data/categories.json` lista os módulos e `data/<id-do-módulo>.json` guarda as entradas. Para adicionar conteúdo, inclua um objeto com `id` único, `category`, `title`, `description`, `explanation`, `keywords`, `synonyms`, `code`, `syntax`, `when`, `example`, `error`, `source`, `version`, `kind` e `related` (lista de IDs existentes). A busca pondera título, palavras-chave/sinônimos, código e descrição, e tolera erros curtos de digitação. Para uma **nova categoria**, adicione-a em `categories.json`, crie seu JSON e inclua o nome do arquivo na lista de carregamento em `src/app.js`. Use referências pontuais e revise versão e exemplos.

`data/prova-p3.json` contém as oito etapas. Os scripts `build_data.py` e `build_p3.py` foram usados para gerar as bases iniciais e servem como origem alternativa: se executados novamente, **sobrescrevem** os JSON correspondentes. Por isso, em manutenção escolha editar os scripts geradores e regenerar, ou editar os JSON e não executar os geradores sem reconciliar as mudanças. Os trechos da P3 são gerados a partir da pasta `exemplo/`.

## Exemplo completo (opcional, requer Python)

O aplicativo web de consulta **não depende** desse exemplo. Para executar o projeto didático Django/DRF localmente:

```bash
cd exemplo
python -m venv .venv
# Ative o ambiente: Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# em outro terminal, com o ambiente ativo:
pytest -v
```

Visite `/quartos/`, `/quartos/novo/` e `/api/quartos/`. O projeto de exemplo inclui migração inicial. Para testar o admin, execute `python manage.py createsuperuser` e acesse `/admin/`. `settings.py` usa chave e `DEBUG` para ambiente local: **não é configuração de produção**. A regra customizada do `QuartoForm` só se aplica a esse form; proteja igualmente as demais entradas antes de uma aplicação real. A API de exemplo também não configura autenticação/autorização de produção.

## Verificação

Foram validados o parsing dos JSON, a sintaxe JavaScript e o exemplo Django com migrações e três testes (`pytest` para model, view e API). A busca local foi testada com as 23 frases de intenção do enunciado. O layout possui breakpoints para desktop e celular; o funcionamento pode variar conforme navegador e permissões de clipboard/localStorage.
