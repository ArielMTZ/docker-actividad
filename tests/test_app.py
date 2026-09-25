from app import app


def test_inicio():
    cliente = app.test_client()

    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert b"Aplicacion ejecutandose correctamente con Docker" in respuesta.data