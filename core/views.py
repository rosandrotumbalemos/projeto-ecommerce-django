from django.shortcuts import render, get_object_or_404
from .models import Produto

# 1. A página principal (que o urls.py chama de pagina_inicial)
def pagina_inicial(request):
    produtos = Produto.objects.all()
    
    # --- O ESPIÃO ESTÁ AQUI ---
    print("--------------------------------------------------")
    print("ESPIÃO: ESTOU DENTRO DA PAGINA_INICIAL!") 
    print(f"ESPIÃO: Encontrei {produtos.count()} produtos no banco.")
    print("--------------------------------------------------")
    # --------------------------

    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)

# 2. A página Sobre (para não dar erro de importação)
def pagina_sobre(request):
    return render(request, 'sobre.html')

# 3. A página de Detalhes (para não dar erro de importação)
def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    context = {
        'produto': produto
    }
    return render(request, 'detalhe_produto.html', context)