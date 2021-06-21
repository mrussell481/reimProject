from daos.manager_dao import ManagerDao
from daos.manager_dao_impl import ManagerDaoImpl
from entities.manager import Manager


manager_dao: ManagerDao = ManagerDaoImpl()


def test_statistics():
    stats_list = manager_dao.statistics()
    counter = 0
    for x in stats_list:
        counter += 1
    assert counter == 9


def test_judge_request():
    response = manager_dao.judge_request(2, 1, True, "Thank you for your help!")
    assert response == "Successfully updated approval status."


def test_view_all_requests():
    assert len(manager_dao.view_all_requests()) > 10


def test_manager_login():
    manager: Manager = manager_dao.login("toughguy12", "0921q83n54v18746")
    assert manager.man_name == "Tim Teebo"
