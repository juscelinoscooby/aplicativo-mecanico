import os

# Caminho da pasta onde estão os PDFs
pasta_doc = 'doc'
arquivos = [f for f in os.listdir(pasta_doc) if f.endswith('.pdf')]

# Gera os blocos HTML
blocos_html = ''
for arquivo in arquivos:
    nome_formatado = arquivo.replace('.pdf', '').replace('-', ' ').replace('_', ' ')
    bloco = f'''
    <div class="document">
      <span>{nome_formatado}</span>
      <a href="{pasta_doc}/{arquivo}" target="_blank"><button>Acessar</button></a>
    </div>
    '''
    blocos_html += bloco

# Salva em um arquivo parcial
with open('documentos.html', 'w', encoding='utf-8') as f:
    f.write(blocos_html)

print('✅ Blocos HTML gerados com sucesso!')