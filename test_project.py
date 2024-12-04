from mypackage.shortest_path import find_shortest_path
from mypackage.config_data import relatives, transportation_mode
from mypackage.path_transport import transport_minimal_time

def test_find_shortest_path():
    result = find_shortest_path()
    assert isinstance(result, list), "result is a list"
    assert len(result) == 2, "result should include a path and a total distance"
    print("test_find_shortest_path: success")

def test_organize_data():
    assert isinstance(relatives, dict), "Relatives should be a dictionary"
    assert 'R1' in relatives, "R1 should be in data"
    print("test_organize_data: success")

def test_transport_minimal_time():
    try:
        transport_minimal_time()
        print("test_transport_minimal_time: success")
    except Exception as e:
        print(f"test_transport_minimal_time: fail - {e}")

# 테스트 실행
if __name__ == "__main__":
    test_find_shortest_path()
    test_organize_data()
    test_transport_minimal_time()
