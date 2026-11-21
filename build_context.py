import json
from pathlib import Path
r=Path(__file__).parent
D=json.loads((r/'data/didatica.json').read_text())
# Explique os trechos-chave, na ordem em que o estudante os lê.
lines={
'model':['from django.db import models — importa os tipos que definem campos de banco.','class Quarto(models.Model) — declara a entidade que o Django reconhece como model.','numero, tipo e disponivel — definem os dados; unique exige número distinto e default define o valor inicial.','__str__ — produz uma identificação legível, útil inclusive no admin.'],
'path':['path(...) — vincula o caminho relativo a uma função da view, não ao arquivo físico.','<int:pk> — converte o segmento da URL em inteiro e o envia como pk.','name — permite gerar o caminho pelo nome sem escrever a URL inteira.'],
'view':['from django.shortcuts import render — importa a função que constrói uma resposta com template.','from .models import Quarto — importa a entidade do mesmo aplicativo.','def lista_quartos(request) — declara a função que recebe a requisição.','Quarto.objects.all() — prepara a consulta; a view pode adicionar filtros.','render(..., {"quartos": quartos}) — procura o template e passa a coleção com o nome quartos.'],
'detail':['A rota captura pk e o envia à função detalhe_quarto.','get_object_or_404(Quarto, pk=pk) procura o model e gera 404 se ele não existir.','render passa o objeto ao template sob a chave quarto.'],
'filter':['Quarto.objects — acessa o gerenciador do model.','filter(disponivel=True) — limita o QuerySet aos quartos disponíveis.','order_by("numero"), no exemplo prático — ordena o resultado; a view deve atribuí-lo e enviá-lo ao template.'],
'for':['{% for quarto in quartos %} percorre a coleção enviada pela view.','{{ quarto.numero }} e {{ quarto.tipo }} exibem atributos de cada objeto.','{% empty %} apresenta uma alternativa quando a coleção está vazia; {% endfor %} encerra a repetição.'],
'modelform':['forms.ModelForm fornece campos associados ao model.','Meta.model aponta para Quarto; fields limita os campos editáveis.','A view deve instanciar o form e verificar is_valid() antes de save().'],
'clean':['clean_numero deve ser um método indentado dentro de QuartoForm.','self.cleaned_data["numero"] contém o valor já convertido pelo campo.','ValidationError interrompe a aceitação do campo; return numero devolve o valor válido.'],
'serializer':['serializers.ModelSerializer define representação e validação de entrada para API.','Meta.model associa o model; fields determina os campos expostos.','O ViewSet utiliza esta classe; o JSON é gerado na resposta da API.'],
'viewset':['viewsets.ModelViewSet agrupa ações de lista, detalhe, criação, atualização e exclusão.','queryset determina os objetos tratados; serializer_class seleciona QuartoSerializer.','No exemplo real, QuartoSerializer está acima no mesmo arquivo api.py; o router o conecta às URLs.'],
'router':['DefaultRouter constrói o roteamento das ações do ViewSet.','router.register("quartos", QuartoViewSet) registra o prefixo do recurso.','path("api/", include(router.urls)) no projeto acrescenta o prefixo /api/.'],
'validar':['O form é vinculado aos dados enviados em request.POST.','is_valid() executa conversão e validações antes de decidir se os dados podem ser usados.','form.save() grava a instância válida; form.errors apresenta os erros em caso contrário.'],
'makemigrations':['python manage.py invoca os comandos do projeto configurado.','makemigrations detecta alterações e gera arquivos de migração; não muda as tabelas.','Execute migrate em seguida para aplicar os arquivos.'],
'migrate':['migrate lê as migrações pendentes e as aplica na ordem de dependência.','O comando usa o banco configurado em resort/settings.py; não altera um template.'],
'include':['include("quartos.urls") carrega padrões de URL do aplicativo.','path("", ...) não acrescenta prefixo; outros prefixos são possíveis.','quartos/urls.py precisa definir urlpatterns.'],
'template':['request fornece o contexto da requisição.','"quartos/lista.html" é o nome lógico do template, não uma URL.','{"quartos": quartos} disponibiliza a coleção para o loop no HTML.'],
'test-db':['pytest.mark.django_db habilita o acesso ao banco de testes.','objects.create cria o registro de teste; assert compara o resultado esperado.','Os dados usados no teste não são os cadastros normais do banco de desenvolvimento.'],
'config-test':['[pytest] inicia a seção de configuração.','DJANGO_SETTINGS_MODULE informa o módulo Python das configurações.','python_files informa como localizar os arquivos de teste.']}
practice={
'django':'Qual comando mostra a versão do Django instalada no ambiente ativo?',
'mvt':'Identifique, numa listagem de quartos, quem define dados, quem prepara a resposta e quem apresenta o HTML.',
'venv':'Indique o comando de ativação do ambiente para seu sistema e explique em qual terminal executá-lo.',
'instalar':'Escreva o comando que instala Django 5.2 no ambiente virtual ativo.',
'startproject':'Qual a diferença entre startproject resort e startproject resort . em relação à pasta criada?',
'startapp':'Crie um aplicativo chamado passeios e indique de qual pasta executar o comando.',
'runserver':'Em qual pasta você deve executar runserver? Qual URL abrir após configurar a lista?',
'settings':'Onde acrescentar passeios à lista de aplicativos sem remover os apps padrão?',
'admin':'Quais pré-requisitos e comando permitem entrar no painel administrativo?',
'model':'Acrescente um campo andar ao model. Em qual arquivo ele fica e quais dois comandos atualizam o banco?',
'fields':'Defina um campo de preço decimal com até 7 dígitos e 2 casas; em que classe ele deve ficar?',
'relationships':'Como uma Reserva poderia apontar para um Quarto usando ForeignKey? Qual arquivo receberia a classe?',
'register':'Indique o import e o registro necessários para que Quarto apareça no painel administrativo.',
'makemigrations':'Depois de acrescentar um campo, qual comando escreve a migração e onde você o executa?',
'migrate':'Qual comando aplica migrações pendentes ao banco? O que precisa existir antes?',
'showmigrations':'Como conferir no terminal quais migrações de quartos já foram aplicadas?',
'path':'Crie uma rota de detalhe para <int:pk> e indique onde ela deve ser incluída.',
'include':'Como o URLconf do projeto delega os caminhos ao arquivo quartos/urls.py?',
'reverse':'Escreva a chamada que obtém a URL da rota quartos:detalhe para o identificador 5.',
'view':'Na view de listagem, envie a coleção com a chave quartos. Qual arquivo receberá essa chave?',
'detail':'Escreva a busca por pk em uma view retornando 404 quando o quarto não existir.',
'request':'Como uma view obtém o valor de q na URL /quartos/?q=luxo?',
'redirect':'Após salvar, como retornar o navegador à rota nomeada quartos:lista?',
'cbv':'Como conectar uma ListView a uma rota usando as_view()?',
'crud':'Como vincular um ModelForm a um quarto já existente ao editar o cadastro?',
'all':'Como obter um QuerySet com todos os quartos em uma view?',
'filter':'Escreva uma consulta para quartos cujo numero seja maior que 100. Em qual função da view ela pode ser usada?',
'get':'O que acontece com get(pk=999) se o registro não existir? Qual alternativa é apropriada em uma view?',
'lookups':'Escreva uma busca de tipo contendo luxo sem diferenciar maiúsculas de minúsculas.',
'queryset':'Como verificar se existe algum quarto disponível sem contar todos os resultados?',
'save':'Explique por que uma regra definida apenas no Form não é executada por quarto.save().',
'for':'Escreva um loop que mostre apenas o tipo de cada quarto. Qual chave a view precisa enviar?',
'template':'Na chamada render, que dicionário permite ao template usar a variável quartos?',
 'tags':'Crie um bloco conteudo em um template filho e indique o arquivo base de que ele depende.',
'modelform':'Defina em Meta quais campos de Quarto ficarão visíveis no formulário e indique o arquivo.',
'validar':'Em qual condição a view deve chamar form.save(), depois de receber POST?',
'clean':'Altere clean_numero para exigir número maior que 100 e indique em qual classe o método deve ficar.',
'drf':'Diferencie a página HTML em /quartos/ da resposta de uma API em /api/quartos/.',
'serializer':'Quais campos do model Quarto seu serializer irá expor? Onde ele fica no exemplo?',
'viewset':'Quais duas propriedades conectam o ModelViewSet ao model e ao serializer?',
'router':'Identifique o arquivo físico que registra o router e o endpoint produzido para a lista.',
'http':'Qual método HTTP consulta a lista? Qual método cria um registro e qual status indica criação bem-sucedida?',
'pytest':'Como executar apenas quartos/tests/test_quartos.py com saída detalhada?',
'config-test':'Qual valor de DJANGO_SETTINGS_MODULE corresponde ao pacote de configuração resort?',
'test-db':'Crie um teste que salve o quarto 202 e verifique seu número. Qual marca autoriza acesso ao banco?',
 'test-client':'Escreva um assert que confirme status 200 depois de client.get("/quartos/").'
}
for k,v in lines.items():D[k]['lines']=v
for k,v in practice.items():D[k]['practice']=v
(r/'data/didatica.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
# Metadata is explicit for every P3 code-bearing section; labels correspond to prova-p3.json.
def L(f,p,a,res):return dict(file=f,folder=p,action=a,responsibility=res)
terminal=L('Não é arquivo: terminal','exemplo/','Execute no terminal, na pasta de manage.py; não cole no Python.','Invoca os comandos do projeto Django.')
m={
'1/O que desenvolver':(D['model']['location'],'O import fornece os tipos; a classe define os campos; __str__ produz texto legível. O banco só muda após as migrações.'),
'1/Comandos necessários':(terminal,'makemigrations gera o arquivo; migrate aplica a alteração no banco configurado.'),
'1/Admin opcional':(D['register']['location'],'O import acessa o model; admin.site.register conecta-o ao painel administrativo.'),
'2/URLs do aplicativo':(D['path']['location'],'app_name cria o namespace; path liga padrões às views; <int:pk> fornece pk para o detalhe.'),
'2/Conexão no projeto':(D['include']['location'],'include delega os caminhos ao app; admin.site.urls disponibiliza o painel. Esta versão ainda não contém o router da etapa 7.'),
'3/Como funciona':(D['view']['location'],'A lista consulta e envia quartos; o detalhe recebe pk, busca um objeto ou retorna 404 e envia quarto ao template.'),
'4/Consulta com filtro':(D['filter']['location'],'objects.filter(disponivel=True) restringe a consulta e order_by("numero") ordena. A atribuição deve ficar dentro da view de listagem.'),
'5/Listagem HTML':(D['for']['location'],'A view envia quartos; for percorre a coleção; empty trata lista vazia; url gera o caminho de detalhe pelo nome.'),
'5/Template de detalhe':(L('exemplo/quartos/templates/quartos/detalhe.html','exemplo/quartos/templates/quartos/','Crie o arquivo de detalhe dentro do app.','Renderiza o objeto enviado pela view de detalhe.'),'{{ quarto.numero }} e {{ quarto.tipo }} acessam a chave quarto do contexto; a tag url gera o link de volta.'),
'6/Formulário':(D['modelform']['location'],'ModelForm define os campos; clean_numero usa cleaned_data, lança ValidationError se necessário e retorna o valor válido.'),
'6/View completa de cadastro':(D['view']['location'],'As três funções estão juntas; criar_quarto vincula POST ao form, valida e salva, ou renderiza o form com erros.'),
'6/URL completa':(D['path']['location'],'O arquivo agora inclui a rota nomeada criar, usada pelo template e pelo namespace quartos.'),
'6/HTML e CSRF':(L('exemplo/quartos/templates/quartos/form.html','exemplo/quartos/templates/quartos/','Crie o arquivo do formulário dentro do app.','Exibe o ModelForm e envia seus dados por POST.'),'csrf_token insere a proteção CSRF; form.as_p apresenta campos e erros; o botão envia a requisição à view.'),
'7/Serializer e ViewSet':(D['serializer']['location'],'O serializer expõe os campos e valida a entrada; o ViewSet usa queryset e serializer_class para fornecer as ações.'),
'7/Router':(L('exemplo/resort/urls.py','exemplo/resort/','Substitua o URLconf inicial ou integre imports, router e padrões ao arquivo existente.','Conecta as URLs HTML, o admin e as rotas da API.'),'router.register vincula quartos ao ViewSet; include(router.urls) sob api/ produz /api/quartos/.'),
'7/Requisições de exemplo':(L('Não é arquivo: terminal / cliente HTTP','Qualquer pasta; com o servidor de exemplo ativo','Execute curl no terminal; o JSON é enviado no corpo da requisição, não salvo como arquivo.','O cliente faz requisições HTTP ao endpoint.'),'GET consulta a lista. POST envia JSON com Content-Type e deve retornar 201 se os dados forem válidos; o id é gerado e pode variar.'),
'8/Configuração':(D['config-test']['location'],'DJANGO_SETTINGS_MODULE aponta para resort.settings; python_files especifica a descoberta de testes.'),
'8/Testes integrados':(D['test-db']['location'],'django_db permite banco de teste; client simula GET/POST; asserts conferem representação, status e persistência.'),
'8/Executar e verificar':(terminal,'pytest -v descobre os testes e apresenta o resultado detalhado no terminal.')}
P={}
for step in json.loads((r/'data/prova-p3.json').read_text()):
 for section in step['sections']:
  if section['code']:
   key=f"{step['number']}/{section['label']}"
   assert key in m,key
   P[key]={'location':m[key][0],'breakdown':m[key][1]}
(r/'data/p3-context.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')
print('P3 metadata blocks:',len(P))
