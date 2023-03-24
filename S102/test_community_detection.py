def test_create_network():
    assert create_network(amis) == {'Alice': ['Bob', 'Dominique'],
                                    'Bob': ['Alice', 'Charlie', 'Dominique'],
                                    'Charlie': ['Bob'],
                                    'Dominique': ['Alice', 'Bob']}
    assert not create_network(list_of_friends) == ['Léo','Thierry','Léo','Valentin','Léo','Axel']
    assert create_network(list_of_friends) != ['Thomas','Daria','Thomas','Carole','Thierry','Axel','Valentin','Andrea']
    print("La fonction create_network est ok")

test_create_network()
    
def test_get_people():
    assert get_people(create_network(amis)) == ['Alice', 'Bob', 'Charlie', 'Dominique']
    assert not get_people(create_network(list_of_friends)) == ['Léo', 'Thierry', 'Valentin', 'Axel', 'Muriel', 'Yasmine']
    assert get_people(create_network(list_of_friends)) != ['Joël', 'Thomas', 'Nassim', 'Andrea', 'Ali', 'Daria', 'Carole']
    print("La fonction get_people est ok")

test_get_people()
    
def test_are_friends():
    assert are_friends(create_network(amis), "Alice", "Bob") == True
    assert not are_friends(create_network(list_of_friends), "Léo", "Andréa") == True
    assert are_friends(create_network(list_of_friends), "Léo", "Thierry") != False
    print("La fonction are_friends est ok")
    
test_are_friends()

def test_all_his_friends():
    assert all_his_friends(create_network(amis), "Alice", ["Bob", "Dominique"]) == True
    assert not all_his_friends(create_network(list_of_friends), "Joêl", ["Thomas", "Axel"]) == True
    assert all_his_friends(create_network(list_of_friends), "Thomas", ["Daria", "Carole"]) != False
    print("La fonction all_his_friends est ok")
    
test_all_his_friends()

def test_is_a_community():
    assert is_a_community(create_network(amis), ["Alice", "Bob", "Dominique"]) == True
    assert not is_a_community(create_network(list_of_friends),["Léo", "Thierry"]) == False
    assert is_a_community(create_network(list_of_friends),["Léo", "Thierry", "Valentin", "Axel"]) != True
    print("La fonction is_a_community est ok")
    
test_is_a_community()

def test_find_community():
    assert find_community(create_network(amis),["Charlie", "Alice", "Dominique"]) == ['Charlie']
    assert not find_community(create_network(list_of_friends), ["Thierry","Léo","Axel"]) == ['Thierry', 'Léo']
    assert find_community(create_network(list_of_friends), ['Léo', 'Axel']) != ['Andréa', 'Léo', 'Axel']
    print("La fonction find_community est ok")
    
test_find_community()

def test_pre_order_by_decreasing_popularity():
    assert pre_order_by_decreasing_popularity(create_network(amis),["Alice", "Bob", "Charlie"],1) == ['Charlie']
    assert not pre_order_by_decreasing_popularity(create_network(list_of_friends),["Léo", "Thierry", "Axel"],3) == ["Axel"]
    assert pre_order_by_decreasing_popularity(create_network(list_of_friends),["Léo", "Thierry", "Axel"],2) != ['Thierry']
    print("La fonction pre_order_by_decreasing_popularity est ok")
    
test_pre_order_by_decreasing_popularity()

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(create_network(amis), ["Alice", "Bob", "Charlie"]) == ['Bob', 'Alice', 'Charlie']
    assert not order_by_decreasing_popularity(create_network(list_of_friends), ["Léo", "Thierry", "Axel"]) == ['Axel', 'Léo', 'Thierry']
    assert order_by_decreasing_popularity(create_network(list_of_friends), ["Léo", "Muriel", "Axel", "Yasmine"]) != ['Muriel', 'Léo', 'Axel', 'Yasmine']
    print("La fonction order_by_decreasing_popularity est ok")
    
test_order_by_decreasing_popularity()

def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity(create_network(amis)) == ['Bob', 'Dominique', 'Alice']
    assert not find_community_by_decreasing_popularity(create_network(list_of_friends)) == ['Joël', 'Andrea', 'Ali']
    assert find_community_by_decreasing_popularity(create_network(list_of_friends)) != [ 'Andrea', 'Nassim']
    print("La fonction find_community_by_decreasing_popularity est ok")
    
test_find_community_by_decreasing_popularity()

def test_find_community_from_person():
    assert find_community_from_person(create_network(amis),"Alice") == ['Alice', 'Bob', 'Dominique']
    assert not find_community_from_person(create_network(list_of_friends),"Ali") == ['Ali', 'Joël', 'Andrea']
    assert find_community_from_person(create_network(list_of_friends),"Muriel") != ['Muriel', 'Yasmine', 'Joël', 'Ali']
    print("La fonction find_community_from_person est ok")
    
test_find_community_from_person()

def test_find_max_community():
    assert find_max_community(create_network(amis)) == ['Alice', 'Bob', 'Dominique']
    assert not find_max_community(create_network(list_of_friends)) == ['Nassim', 'Ali']
    assert find_max_community(create_network(list_of_friends)) != ['Muriel', 'Yasmine', 'Joël', 'Ali']
    print("La fonction find_max_community est ok")
    
test_find_max_community()
