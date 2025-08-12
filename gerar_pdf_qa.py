from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT_PATH = "font/DejaVuSans.ttf"

titulo = "Template de Abertura de Issue (QA) + Checklist de Validação Pós-Fix"

conteudo = """
📄 TEMPLATE DE ABERTURA DE ISSUE (QA) – JIRA

🔹 Tipo da Issue: Bug

Título (Resumo):
[Área do sistema] - Breve descrição do erro
Exemplo: Cadastro - Sistema permite salvar CPF inválido

Descrição:
Descrição do problema:
O sistema está permitindo salvar usuários com CPF inválido, sem apresentar mensagens de validação.

Ambiente:
- [ ] Local
- [ ] Homologação
- [ ] Produção

Comportamento atual:
O sistema salva um CPF inválido (ex: 000.000.000-00) sem apresentar erro.

Comportamento esperado:
O sistema deve validar o CPF e exibir uma mensagem de erro quando for inválido.

Impacto:
Dados inválidos podem ser inseridos na base, comprometendo integrações e relatórios.

Passos para reprodução:
1. Acessar o módulo de cadastro de usuários;
2. Preencher os campos obrigatórios;
3. Informar um CPF inválido (ex: 000.000.000-00);
4. Clicar em "Salvar".
Resultado atual: Usuário salvo com sucesso.
Resultado esperado: Mensagem de erro: "CPF inválido".

Evidências:
Anexe prints de tela, vídeos (ex: via Loom), logs ou traceback.

Informações adicionais:
Navegador: Chrome v123
Versão do sistema: 2.4.7
Data/Hora do teste: 05/08/2025 às 15:30

Severidade: Alta
Prioridade: Média

✅ CHECKLIST DE VALIDAÇÃO PÓS-FIX (QA)

🔄 Reteste da Issue:
- [ ] Validar se o erro descrito não ocorre mais com os dados informados
- [ ] Executar novamente os passos de reprodução originais
- [ ] Verificar se a mensagem ou comportamento esperado ocorre
- [ ] Testar com variações de dados similares ao cenário do bug

🔁 Teste de Regressão Focal:
- [ ] Validar se o comportamento original do sistema foi mantido para entradas válidas
- [ ] Testar se funcionalidades vizinhas ou dependentes continuam funcionando normalmente
- [ ] Verificar se outros campos/processos relacionados não foram afetados pelo fix

🧪 Ambiente e Deploy:
- [ ] Confirmar em qual ambiente o fix foi aplicado (QA, staging, produção)
  - [ ] "QA"
  - [ ] "UAT"
  - [ ] "PROD"
- [ ] Verificar se a versão do sistema está correta
- [ ] Validar se não existem erros no console ou logs

🗂️ Rastreamento:
- [ ] O PR/commit relacionado à issue foi vinculado corretamente (fixes #ID)
- [ ] O desenvolvedor adicionou testes automatizados (se aplicável)
- [ ] A issue foi atualizada com o status correto:
  - [ ] "Aguardando reteste"
  - [ ] "Validado"
  - [ ] "Reaberto"

✅ Conclusão:
- [ ] O bug foi corrigido com sucesso
- [ ] Nenhum impacto colateral foi identificado
- [ ] A issue pode ser encerrada ou movida para produção
"""

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "", 14)
        self.cell(0, 10, titulo, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)

    def chapter_body(self, text):
        self.set_font("DejaVu", "", 11)
        self.multi_cell(0, 8, text)

pdf = PDF()
pdf.add_font("DejaVu", "", FONT_PATH, uni=True)
pdf.add_page()
pdf.chapter_body(conteudo)
pdf.output("./report/Template_QA_Issue_Checklist.pdf")
