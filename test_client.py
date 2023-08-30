import pytest
from ..Class.client import Client # per far funzionare pytest




@pytest.fixture
def person():
    return Client("Nome", "Cognome")

def test_copy(person):
    copied_value = Client(person.name, person.surname)
    assert copied_value.name == person.name and copied_value.surname == person.surname

# wrap up person test
def is_person_correct(person):
    assert isinstance(person.name, str)
    assert isinstance(person.surname, str)





# lista corretti
@pytest.mark.parametrize("list_right", [
    Client("Monica", "Franco"),
    Client("Franco", "Orlando"),
    Client("Mammt", "Ricchio")
])

def test_list_right(list_right):
    is_person_correct(list_right)









# fatta senza parametrize perché non si può creare l'exception handling
@pytest.fixture
def list_wrong():
    people = []

    with pytest.raises(TypeError):
        people = [
        Client("", ""),
        Client(),
        Client(10, 10),
        Client(20),
        Client(None, None),
        Client("10", "Mammt")
        ]


    return people

# vuol dire = sapendo che mi darà errore, controlla se il test da esito negativo, se si è corretto
def test_list_wrong(list_wrong):
    for p in list_wrong:
        not is_person_correct(p)


