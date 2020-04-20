from enum import Enum


class tipo(Enum):
    Fisica = "Fisica"
    Juridica = "Jurídica"


class genero(Enum):
    Masculino = "M"
    Feminino = "F"
    Outro = "O"


class situacaoPessoa(Enum):
    Ativa = "Ativa"
    Inativa = "Inativa"


class situacaoUsuario(Enum):
    Ativo = "Ativo"
    Inativo = "Inativo"
    Bloqueado = "Bloqueado"


class tipoCanal(Enum):
    Telefone = "telefone"
    Email = "email"
    Chat = "chat-Online"
    Facebook = "facebook"
    Linkedin = "linkedin"
    Twitter = "twitter"
    Site = "site"
    WhatsApp = "whatsapp"
    SMS = "SMS"


class situacaoCanal(Enum):
    Ativo = "Ativo"
    Inativo = "Inativo"
