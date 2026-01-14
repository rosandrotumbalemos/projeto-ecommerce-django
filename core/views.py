from django.shortcuts import render
from core.models import Produto  # <--- 1. Importamos a tabela

def pagina_inicial(request):
    # 2. Buscamos TODOS os produtos do banco (SELECT * FROM Produto)
    produtos = Produto.objects.all()

    # 3. Criamos um "dicionário de contexto"
    # É como uma caixa de entregas. O nome 'lista_produtos' é como vamos chamar lá no HTML
    contexto = {
        'lista_produtos': produtos
    }

    # 4. Entregamos a caixa junto com o HTML
    return render(request, 'index.html', contexto)

def pagina_sobre(request):
    return render(request, 'sobre.html')

def detalhe_produto(request, id):
    # Buscamos o produto onde o id no banco é igual ao id da URL
    produto = Produto.objects.get(id=id)

    contexto = {
        'produto': produto
    }
    return render(request, 'detalhe.html', contexto)