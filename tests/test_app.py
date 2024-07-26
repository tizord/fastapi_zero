from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá, mundo'}  # Assert


def test_create_user(client):
    # Arrange

    response = client.post(
        '/user/',
        json={
            'username': 'teste_username',
            'password': 'password',
            'email': 'teste@teste.com',
        },
    )  # Act
    # Asset 1 - Voltou o status code correto?

    assert response.status_code == HTTPStatus.CREATED

    # Assert 2 - Validar o UserPublic

    assert response.json() == {
        'username': 'teste_username',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'teste_username',
                'email': 'teste@teste.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'teste_username2',
            'email': 'teste2@teste.com',
            'password': '123',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'teste_username2',
        'email': 'teste2@teste.com',
        'id': 1,
    }

def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}