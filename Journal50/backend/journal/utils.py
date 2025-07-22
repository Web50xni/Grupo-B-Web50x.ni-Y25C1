from datetime import datetime
import re


def parse_links(raw_links):
    """
    Convierte un campo de enlaces (lista o string multilínea) en una lista limpia de URLs.
    
    Args:
        raw_links (str | list): Texto con enlaces por línea o lista de enlaces.
    
    Returns:
        list[str]: Lista de enlaces limpios.
    """
    
    if isinstance(raw_links, list):
        # Ya es una lista (posiblemente desde cleaned_data del form)
        return [link.strip() for link in raw_links if link.strip()]
    
    elif isinstance(raw_links, str):
        # Normalizar saltos de línea a \n
        normalized = raw_links.replace('\r\n', '\n').replace('\r', '\n')
        
        # Separar por líneas vacías (dos saltos de línea) — para enlaces que ocupan varias líneas
        blocks = re.split(r'\n\s*\n', normalized.strip())
        
        # Quitar saltos internos y espacios, y quedarnos solo con los enlaces no vacíos
        return [block.replace('\n', '').strip() for block in blocks if block.strip()]
    
    return []


def build_note_dict(cleaned_data, studyspace):
    """
    Construye una entrada de nota estructurada desde form.cleaned_data.

    Args:
        cleaned_data (dict): Datos validados del formulario.

    Returns:
        dict: Diccionario con la clave igual al título y valor estructurado.
    """
    title = cleaned_data.get("title", "Sin título")
    
    return {
        title: {
            "title": title,
            "studyspace": studyspace,
            "content": cleaned_data.get("content", ""),
            "links": parse_links(cleaned_data.get("links", [])),
            "code": {
                "language": cleaned_data.get("language", ""),
                "source": cleaned_data.get("source", "")
            },
            "created_at": datetime.today().strftime('%d/%m/%y')
        }
    }