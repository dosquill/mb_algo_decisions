import pytest
from offer import Offer


@pytest.fixture
def offer():
    name = "test"
    profit = 100
    budget_needed = 1000
    time_needed = 1
    data = Offer(name=name, profit=profit, budget_needed=budget_needed, time_needed=time_needed)
    return data



def test_right_constructor():
    assert Offer(name= 'test1', profit=100, budget_needed=1000, time_needed=1)
    assert Offer(name= 'test2', profit=100.0, budget_needed=1000.0, time_needed=2)
    



def test_wrong_names():
    with pytest.raises(Exception):
        Offer(name=10, profit=100, budget_needed=1000, time_needed=1)

    with pytest.raises(Exception):
        Offer(name='', profit=100, budget_needed=1000, time_needed=1)

    with pytest.raises(Exception):
        Offer(name= None, profit=100, budget_needed=1000, time_needed=1)

    with pytest.raises(Exception):
        Offer(name= True, profit=100, budget_needed=1000, time_needed=1)

def test_right_names():
    assert Offer(name='Bet365', profit=100, budget_needed=1000, time_needed=1)
    assert Offer(name='Bwin', profit=100, budget_needed=1000, time_needed=1)








def test_wrong_profits():
    with pytest.raises(Exception):
        Offer(name='Test', profit='100', budget_needed=1000, time_needed=1)

    with pytest.raises(Exception):
        Offer(name='Test', profit=None, budget_needed=1000, time_needed=1)

    with pytest.raises(Exception):
        Offer(name= 'Test', profit=-100, budget_needed=1000, time_needed=1)

    with pytest.raises(Exception):
        Offer(name= 'Test', profit='', budget_needed=1000, time_needed=1)

    with pytest.raises(Exception):
        Offer(name= 'Test', profit=True, budget_needed=1000, time_needed=1)

def test_right_profits():
    assert Offer(name= 'Test', profit=100, budget_needed=1000, time_needed=1)
    assert Offer(name= 'Test', profit=100.0, budget_needed=1000, time_needed=1)








def test_wrong_budget_needed():
    with pytest.raises(Exception):
        Offer(name='Test', profit=100, budget_needed='1000', time_needed=1)

    with pytest.raises(Exception):
        Offer(name='Test', profit=100, budget_needed='', time_needed=1)

    with pytest.raises(Exception):
        Offer(name= 'Test', profit=100, budget_needed=None, time_needed=1)

    with pytest.raises(Exception):
        Offer(name= 'Test', profit=100, budget_needed=-1000, time_needed=1)

    with pytest.raises(Exception):
        Offer(name= 'Test', profit=100, budget_needed=True, time_needed=1)


def test_right_budget_needed():
    assert Offer(name= 'Test', profit=100, budget_needed=1000, time_needed=1)
    assert Offer(name= 'Test', profit=100, budget_needed=1000.0, time_needed=1)





def test_wrong_time_needed():
    with pytest.raises(Exception):
        Offer(name='Test', profit=100, budget_needed=1000, time_needed=1.0)

    with pytest.raises(Exception):
        Offer(name='Test', profit=100, budget_needed=1000, time_needed='')

    with pytest.raises(Exception):
        Offer(name= 'Test', profit=100, budget_needed=1000, time_needed='1')

    with pytest.raises(Exception):
        Offer(name= 'Test', profit=100, budget_needed=1000, time_needed=-1)

    with pytest.raises(Exception):
        Offer(name= 'Test', profit=100, budget_needed=1000, time_needed=True)

    with pytest.raises(Exception):
        Offer(name= 'Test', profit=100, budget_needed=1000, time_needed=None)


def test_right_time_needed():
    assert Offer(name= 'Test', profit=100, budget_needed=1000, time_needed=1)






# @pytest.fixture
# def list_right():
#     return [
#         {
#             'bookmaker': 'Betfair', 
#             'earning': 10, 
#             'budget_needed': 100, 
#             'roi': 0.1, 
#             'time_needed': 10
#         },
#     ]
# 
# 
# 
# """ 
# @pytest.fixture
# def list_wrong():
#     return [
#         {
#             'bookmaker': 'Betfair',
#             'earning': 10,
#             'budget_needed': 100,
#             'roi': 0.1,
#             'time_needed': 10
#         },
#         {
#             'bookmaker': '',
#             
#         },
#         {
#             'bookmaker': None,
#             'earning': 10,
#             
#         }
#     ]
# 
#  """
# 
# 
# 
# def test_list_right(list_right):
#     for data in list_right:
#         Offer(
#             bookmaker=data['bookmaker'],
#             earning=data['earning'],
#             budget_needed=data['budget_needed'],
#             roi=data['roi'],
#             time_needed=data['time_needed']
#             )
# 
# 
# """ 
# def test_list_wrong(list_wrong):
#     for data in list_wrong:
#         assert not Offer(
#             bookmaker=data['bookmaker'],
#             earning=data['earning'],
#             budget_needed=data['budget_needed'],
#             roi=data['roi'],
#             time_needed=data['time_needed']
#             )
# 
#  """