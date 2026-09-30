
def parece_imagen(url_o_nombre: str) -> bool:
    if not url_o_nombre:
        return False
    extensiones = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg')
    return url_o_nombre.lower().endswith(extensiones)

