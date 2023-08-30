import pytest
from ..Class.offer import Offer



@pytest.fixture
def example_list():
    data = OfferList(Offer("bookmaker1", 1.1, 100, 1.1, 1))
    return data


def test_offer_list(example_list):
    print(example_list)







# TODO devo fare un dizionario con i valori corretti e quelli sbagliati e fare un ciclo for per testare tutti i valori
@pytest.fixture
def list_right():
    return [
        {
            'bookmaker': 'Betfair', 
            'earning': 10, 
            'budget_needed': 100, 
            'roi': 0.1, 
            'time_needed': 10
        },
    ]



""" 
@pytest.fixture
def list_wrong():
    return [
        {
            'bookmaker': 'Betfair',
            'earning': 10,
            'budget_needed': 100,
            'roi': 0.1,
            'time_needed': 10
        },
        {
            'bookmaker': '',
            
        },
        {
            'bookmaker': None,
            'earning': 10,
            
        }
    ]

 """



def test_list_right(list_right):
    for data in list_right:
        Offer(
            bookmaker=data['bookmaker'],
            earning=data['earning'],
            budget_needed=data['budget_needed'],
            roi=data['roi'],
            time_needed=data['time_needed']
            )


""" 
def test_list_wrong(list_wrong):
    for data in list_wrong:
        assert not Offer(
            bookmaker=data['bookmaker'],
            earning=data['earning'],
            budget_needed=data['budget_needed'],
            roi=data['roi'],
            time_needed=data['time_needed']
            )

 """