import requests

# Base url
base_url = "http://localhost:8000"

#  /banks endpoint test  
def test_banks_endpoint():
    response = requests.get(f"{base_url}/banks")
    assert response.status_code == 200
    assert len(response.json()) > 0



#  /branches/:ifsc endpoint test
def test_branch_by_ifsc_endpoint():
    response = requests.get(f"{base_url}/branches/RATN0000190")
    assert response.status_code == 200
    



# function to test the /banks/search endpoint
def test_search_banks_endpoint():
    response = requests.get(f"{base_url}/banks/search?name=SBI")
    assert response.status_code == 200
    

# function to test the /banks/:bank_name/branches endpoint
def test_bank_branches_endpoint():
    response = requests.get(f"{base_url}/banks/axis/branches_view")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Calling the test functions
test_banks_endpoint()
test_branch_by_ifsc_endpoint()
test_search_banks_endpoint()
test_bank_branches_endpoint()