import graphviz

# Função para criar o mapa mental
def criar_mapa_mental():
    # Cria um novo gráfico
    mapa = graphviz.Digraph('Mapa Mental', filename='mapamental2', engine='dot', format='png')
    
    # Ajusta o tamanho do mapa mental
    mapa.attr(size='10,10')

    # Definições de cores
    cor_html = 'orange'
    cor_css = 'blue'
    cor_js = 'yellow'

    # Seção HTML
    mapa.node('HTML', 'HTML', color=cor_html, style='filled', fillcolor=cor_html)
    mapa.node('Estrutura', 'Estrutura', color=cor_html, style='filled', fillcolor=cor_html)
    mapa.node('Tags Comuns', 'Tags Comuns', color=cor_html, style='filled', fillcolor=cor_html)
    mapa.edge('HTML', 'Estrutura')
    mapa.edge('HTML', 'Tags Comuns')
    
    tags_html = ['<!DOCTYPE>', '<html>', '<head>', '<title>', '<body>', '<h1> to <h6>', '<p>', '<a>', '<img>', '<div>', '<span>', '<ul>', '<ol>', '<li>', '<table>', '<form>', '<input>', '<button>', '<link>', '<meta>']
    for tag in tags_html:
        mapa.node(tag, tag, color=cor_html, style='filled', fillcolor=cor_html)
        mapa.edge('Tags Comuns', tag)
    
    # Seção CSS
    mapa.node('CSS', 'CSS', color=cor_css, style='filled', fillcolor=cor_css)
    mapa.node('Seletores', 'Seletores', color=cor_css, style='filled', fillcolor=cor_css)
    mapa.node('Propriedades Comuns', 'Propriedades Comuns', color=cor_css, style='filled', fillcolor=cor_css)
    mapa.edge('CSS', 'Seletores')
    mapa.edge('CSS', 'Propriedades Comuns')
    
    seletores_css = ['.class', '#id', 'elemento', 'elemento1,elemento2', 'elemento1 elemento2']
    for seletor in seletores_css:
        mapa.node(seletor, seletor, color=cor_css, style='filled', fillcolor=cor_css)
        mapa.edge('Seletores', seletor)
    
    propriedades_css = ['color', 'background-color', 'font-size', 'margin', 'padding', 'border', 'width', 'height', 'display', 'flex', 'grid']
    for prop in propriedades_css:
        mapa.node(prop, prop, color=cor_css, style='filled', fillcolor=cor_css)
        mapa.edge('Propriedades Comuns', prop)
    
    # Seção JavaScript
    mapa.node('JavaScript', 'JavaScript', color=cor_js, style='filled', fillcolor=cor_js)
    mapa.node('Tipos de Dados', 'Tipos de Dados', color=cor_js, style='filled', fillcolor=cor_js)
    mapa.node('Estruturas de Controle', 'Estruturas de Controle', color=cor_js, style='filled', fillcolor=cor_js)
    mapa.node('Funções', 'Funções', color=cor_js, style='filled', fillcolor=cor_js)
    mapa.edge('JavaScript', 'Tipos de Dados')
    mapa.edge('JavaScript', 'Estruturas de Controle')
    mapa.edge('JavaScript', 'Funções')
    
    tipos_js = ['Number', 'String', 'Boolean', 'Array', 'Object', 'Null', 'Undefined']
    for tipo in tipos_js:
        mapa.node(tipo, tipo, color=cor_js, style='filled', fillcolor=cor_js)
        mapa.edge('Tipos de Dados', tipo)
    
    estruturas_js = ['if', 'else', 'switch', 'for', 'while', 'do while']
    for estrutura in estruturas_js:
        mapa.node(estrutura, estrutura, color=cor_js, style='filled', fillcolor=cor_js)
        mapa.edge('Estruturas de Controle', estrutura)
    
    funcoes_js = ['function', 'return', '=> (arrow function)', 'callback', 'async/await']
    for funcao in funcoes_js:
        mapa.node(funcao, funcao, color=cor_js, style='filled', fillcolor=cor_js)
        mapa.edge('Funções', funcao)
    
    # Renderiza o mapa mental
    mapa.render(view=True)

# Chama a função para criar o mapa mental
criar_mapa_mental()

