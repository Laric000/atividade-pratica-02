from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, String

from database import Base


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30), unique=True)
    pais: Mapped[str] = mapped_column(String(30), unique=True)
    livros: Mapped[List['Livro']] = relationship(back_populates= 'autor')
    # TODO: relacione Autor com Livro usando relationship e back_populates.


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(30), unique=True)
    ano: Mapped[int] = mapped_column
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    disponivel: Mapped[bool] = mapped_column(defaul= True)
    autor:Mapped['Autor'] = relationship(back_populates = 'livro')

    # TODO: adicione o campo disponivel, com valor padrão True.
    # TODO: relacione Livro com Autor usando relationship e back_populates.
    livros = [ 
        
    ]

