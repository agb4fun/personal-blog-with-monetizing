from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    id: int  # Identificador único del blog
    title: str
    content: str
    image_url: str  # URL de la imagen asociada al blog (opcional)
    author: str  # Nombre del autor del blog
    published: bool  # Indica si el blog está publicado o no
    # Otros campos que desees incluir, como fecha de creación, fecha de modificación, etc.

class User(BaseModel):
    username: str  # Nombre de usuario único
    email: str  # Dirección de correo electrónico
    full_name: str  # Nombre completo del usuario
    hashed_password: str  # Contraseña hasheada del usuario
    blogs: List[Blog] = []  # Lista de blogs escritos por el usuario

class Payment(BaseModel):
    id: int  # Identificador único del pago
    user_id: int  # Identificador del usuario que hizo el pago
    amount: float  # Cantidad del pago
    # Otros campos que desees incluir, como fecha del pago, estado, etc.
