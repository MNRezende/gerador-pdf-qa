# gerador-pdf-qa

📄 README – Script gerar_pdf_qa.py

📌 Descrição
Este script gera um PDF padronizado com:

 - Template de abertura de issue (QA) para o Jira. 
 - Checklist de validação pós-fix para garantir qualidade após correções.

O objetivo é fornecer uma documentação visual e prática para equipes de Qualidade (QA), ajudando a padronizar a comunicação de bugs e testes de validação.

🛠 Tecnologias Utilizadas

 - Python 3.x 
 - fpdf2 – biblioteca para geração de PDFs.
 
📂 Estrutura do Script

 - Título: "Template de Abertura de Issue (QA) + Checklist de Validação Pós-Fix"
 - Conteúdo: texto estruturado com:
	 - Campos obrigatórios para registro de bugs.
	 - Passos para reprodução do problema.
	 - Espaços para anexar evidências.
	 - Checklist de testes após a correção.
	 
📦 Pré-requisitos

Antes de executar, instale as dependências:

    pip install fpdf2

Certifique-se também de ter a fonte DejaVuSans.ttf no diretório:

    font/DejaVuSans.ttf

▶️ Como Executar

    python gerar_pdf_qa.py

ou

    python3 gerar_pdf_qa.py

Ao executar, o script irá gerar um arquivo PDF contendo o template e checklist prontos para uso.

📑 Exemplo de Saída

O PDF gerado conterá:

 - Cabeçalho com o título do documento.
 - Seções bem definidas para preenchimento rápido.
 - Checklist com caixas para marcação manual ou digital.
 
🧩 Possíveis Melhorias

 - Parametrizar título e conteúdo para permitir geração de diferentes templates.
 - Adicionar suporte a múltiplos idiomas.
 - Permitir configuração de estilos (cores, fontes e logos).

📜 Licença

Este script pode ser usado e adaptado livremente para fins internos da sua equipe.