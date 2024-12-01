from ..repository.categoria_repository import select_all_categoria

def select_all_categoria_service():
    categorias=select_all_categoria()
    print(categorias)
    return categorias