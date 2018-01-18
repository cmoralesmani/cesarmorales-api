"""
Excepciones personalizadas para errores que ocurran durante el
envío de correo.
"""


class Error(Exception):
    """ Clase base para las excepciones del envío de email  """
    pass


class SendError(Error):
    """
    Se activa cuando hay un error dentro del módulo de
    envío de email
    """

    def __init__(self, message):
        self.message = message
