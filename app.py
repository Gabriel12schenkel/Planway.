from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ================= Dados Temporários ===================
empresas_cadastradas = []

fornecedores = [
    {
        'id': 's001',
        'nome': 'Moda Essencial Atacado',
        'segmento': 'Roupas e Têxteis',
        'contato': 'contato@modaessencial.com.br',
        'telefone': '(11) 98765-4321',
        'localizacao': 'São Paulo, SP',
        'descricao': 'Fornecedor de roupas femininas e masculinas no atacado.',
        'avaliacao': 4.8,
        'avaliacoes': 125,
        'servicos': ['Roupas Femininas', 'Roupas Masculinas', 'Acessórios'],
        'produtos': [
            {'nome': 'Camiseta Básica Feminina', 'descricao': 'Pacote com 10 unidades', 'preco': 120.00},
            {'nome': 'Calça Jeans Masculina', 'descricao': 'Pacote com 5 unidades', 'preco': 250.00}
        ]
    },
    {
        'id': 's002',
        'nome': 'Orgânicos da Fazenda Feliz',
        'segmento': 'Alimentos e Bebidas',
        'contato': 'vendas@fazendafeliz.com.br',
        'telefone': '(21) 91234-5678',
        'localizacao': 'Rio de Janeiro, RJ',
        'descricao': 'Produtor e distribuidor de alimentos orgânicos frescos.',
        'avaliacao': 4.9,
        'avaliacoes': 98,
        'servicos': ['Frutas Orgânicas', 'Vegetais Orgânicos', 'Laticínios Naturais'],
        'produtos': [
            {'nome': 'Cesta de Verduras Orgânicas', 'descricao': 'Mix selecionado de verduras da estação', 'preco': 45.00},
            {'nome': 'Tomate Cereja Orgânico', 'descricao': 'Pacote de 1kg', 'preco': 18.50}
        ]
    },
    {
        'id': 's003',
        'nome': 'Eletrônicos & Cia',
        'segmento': 'Eletrônicos e Tecnologia',
        'contato': 'comercial@eletronicoscia.com',
        'telefone': '(31) 97654-3210',
        'localizacao': 'Belo Horizonte, MG',
        'descricao': 'Variedade de eletrônicos, gadgets e acessórios.',
        'avaliacao': 4.5,
        'avaliacoes': 210,
        'servicos': ['Smartphones', 'Acessórios Tech', 'Componentes PC'],
        'produtos': [
            {'nome': 'Carregador Portátil', 'descricao': '10000mAh, entrada USB-C', 'preco': 89.90},
            {'nome': 'Fone Bluetooth', 'descricao': 'Cancelamento de ruído', 'preco': 159.90}
        ]
    },
    {
        'id': 's004',
        'nome': 'Embalagens Sustentáveis BR',
        'segmento': 'Embalagens e Descartáveis',
        'contato': 'vendas@sustentaveisbr.com.br',
        'telefone': '(41) 98765-0000',
        'localizacao': 'Curitiba, PR',
        'descricao': 'Fornecedor de embalagens ecológicas e biodegradáveis.',
        'avaliacao': 4.6,
        'avaliacoes': 70,
        'servicos': ['Embalagens Biodegradáveis', 'Sacos Ecológicos', 'Descartáveis Sustentáveis'],
        'produtos': [
            {'nome': 'Embalagem para Alimentos', 'descricao': 'Pacote com 100 unidades', 'preco': 75.00},
            {'nome': 'Canudos de Papel', 'descricao': 'Pacote com 200 unidades', 'preco': 45.00}
        ]
    }
]

# ================= Rotas ===================

# Redirecionar / → /inicio
@app.route('/')
def home():
    return redirect(url_for('inicio'))

# 🏠 Página Inicial
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

# 🗂️ Planejamento
@app.route('/planejamento')
def planejamento():
    return render_template('planejamento.html')

# 📈 Financeiro
@app.route('/financeiro')
def financeiro():
    return render_template('financeiro.html')

# 🎯 Marketing
@app.route('/marketing')
def marketing():
    return render_template('marketing.html')

# 🤝 Seja Sócio
@app.route('/seja-socio', methods=['GET', 'POST'])
def seja_socio():
    global empresas_cadastradas

    if request.method == 'POST':
        nova_empresa = {
            'nome': request.form['company-name'],
            'segmento': request.form['segment'],
            'localizacao': request.form['location'],
            'investimento': request.form['investment'],
            'porcentagem': request.form['percentage'],
            'contato': request.form['contact'],
            'descricao': request.form['description']
        }
        empresas_cadastradas.append(nova_empresa)
        return redirect(url_for('seja_socio', cadastro_sucesso=True))

    cadastro_sucesso = request.args.get('cadastro_sucesso')
    return render_template('sejasocio.html',
                           empresas=empresas_cadastradas,
                           cadastro_sucesso=cadastro_sucesso)

# 🛍️ Fornecedor (marketplace)
@app.route('/fornecedor')
def fornecedor():
    return render_template('fornecedor.html', fornecedores=fornecedores)

# 🔍 Detalhes do Fornecedor
@app.route('/fornecedor/<string:supplier_id>')
def detalhes_fornecedor(supplier_id):
    fornecedor = next((f for f in fornecedores if f['id'] == supplier_id), None)
    
    if fornecedor is None:
        return redirect(url_for('fornecedor'))
    
    return render_template('detalhes_fornecedor.html', 
                           fornecedor=fornecedor,
                           fornecedores=fornecedores)

# ================= Run ===================
if __name__ == '__main__':
    app.run(debug=True)
