from ex5 import monthly_users
from ex5 import annual_user_count
from ex5 import annual_user_download_average
import ex5

def test_monthly_users():
    ex5.access_log = ["19.69.248.2 mmc2 [12/12/2018] `GET /m/' 200 4263",
    "19.69.248.2 mmc2 [12/12/2018] `GET /m/index.php' 200 4494",
    "46.72.177.4 gr4 [12/12/2018] `GET /video/v.php' 200 4263"]
    assert (monthly_users(2018) == [0,0,0,0,0,0,0,0,0,0,0,2]) or \
        (monthly_users(2018) == [0,0,0,0,0,0,0,0,0,0,0,3])

def test_annual_user_count():
    ex5.access_log = ["19.69.248.2 mmc2 [12/12/2018] `GET /m/' 200 4263",
    "19.69.248.2 mmc2 [12/12/2018] `GET /m/index.php' 200 4494",
    "46.72.177.4 gr4 [12/12/2018] `GET /video/v.php' 200 4263"]
    assert (annual_user_count(2018) == 2) or (annual_user_count(2018) == 3)

def test_annual_user_download_average():
    ex5.access_log = ["19.69.248.2 mmc2 [12/12/2018] `GET /m/' 200 4263",
    "19.69.248.2 mmc2 [12/12/2018] `GET /m/index.php' 200 4494",
    "46.72.177.4 gr4 [12/12/2018] `GET /video/v.php' 200 4263"]
    assert (annual_user_download_average(2018) == 4340) or \
        (annual_user_download_average(2018) == 6510)

test_annual_user_download_average()
