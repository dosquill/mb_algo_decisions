import pytest
from Class.client import Client


real_file_name = 'db/all_offers.json'

@pytest.fixture
def person():
    name = "Nome"
    surname = "Cognome"
    id = 1
    return Client(name = name, surname=surname, id=id, file_path=real_file_name)




def test_right_constructor():
    assert person
    




def test_wrong_names():
    with pytest.raises(Exception):
        Client(name='', surname='Rossi', id=1, file_path=real_file_name)

    with pytest.raises(Exception):
        Client(name=True, surname='Rossi', id=1, file_path=real_file_name)

    with pytest.raises(Exception):
        Client(name=100, surname='Rossi', id=1, file_path=real_file_name)

    with pytest.raises(Exception):
        Client(name=100.0, surname='Rossi', id=1, file_path=real_file_name)
    
    with pytest.raises(Exception):
        Client(name=None, surname='Rossi', id=1, file_path=real_file_name)

def test_right_names():
    assert Client(name='Giovanni', surname='Rossi', id=1, file_path=real_file_name)






def test_wrong_surnames():
    with pytest.raises(Exception):
        Client(name='Marco', surname='',  id=1, file_path=real_file_name)

    with pytest.raises(Exception):
        Client(name='Marco', surname=True, id=1, file_path=real_file_name)

    with pytest.raises(Exception):
        Client(name='Marco', surname=100, id=1, file_path=real_file_name)

    with pytest.raises(Exception):
        Client(name='Marco', surname=100.0, id=1, file_path=real_file_name)
    
    with pytest.raises(Exception):
        Client(name='Marco', surname=None, id=1, file_path=real_file_name)

def test_right_surnames():
    assert Client(name='Giovanni', surname='Rossi', id=1, file_path=real_file_name)








def test_wrong_id():
    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi',  id=1.0, file_path=real_file_name)
    
    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi',  id=-1, file_path=real_file_name)

    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi', id='1', file_path=real_file_name)

    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi', id='', file_path=real_file_name)

    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi', id=True, file_path=real_file_name)
    
    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi', id=None, file_path=real_file_name)

def test_right_id():
    assert Client(name='Giovanni', surname='Rossi', id=1, file_path=real_file_name)









def test_wrong_file_path():
    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi',  id=1, file_path=10)

    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi', id=1, file_path=10.0)

    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi', id=1, file_path='')

    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi', id=1, file_path=None)
    
    with pytest.raises(Exception):
        Client(name='Marco', surname='Rossi', id=1, file_path=True)

def test_right_file_path():
    assert Client(name='Giovanni', surname='Rossi', id=1, file_path=real_file_name)

















##### NON CANCELLARE #####
#  def test_copy(person):
#      copied_value = Client(person.name, person.surname)
#      assert copied_value.name == person.name and copied_value.surname == person.surname
#  
#  # wrap up person test
#  def is_person_correct(person):
#      assert isinstance(person.name, str)
#      assert isinstance(person.surname, str)
#  
#  
#  
#  
#  
#  # lista corretti
#  @pytest.mark.parametrize("list_right", [
#      Client("Monica", "Franco"),
#      Client("Franco", "Orlando"),
#      Client("Mammt", "Ricchio")
#  ])
#  
#  def test_list_right(list_right):
#      is_person_correct(list_right)
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  # fatta senza parametrize perché non si può creare l'exception handling
#  @pytest.fixture
#  def list_wrong():
#      people = []
#  
#      with pytest.raises(TypeError):
#          people = [
#          Client("", ""),
#          Client(),
#          Client(10, 10),
#          Client(20),
#          Client(None, None),
#          Client("10", "Mammt")
#          ]
#  
#  
#      return people
#  
#  # vuol dire = sapendo che mi darà errore, controlla se il test da esito negativo, se si è corretto
#  def test_list_wrong(list_wrong):
#      for p in list_wrong:
#          not is_person_correct(p)
#  
#  
#  