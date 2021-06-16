from typing import List
from daos.manager_dao import ManagerDao
from entities.manager import Manager
from entities.reimbursement import Reimbursement
from services.manager_service import ManagerService


class ManagerServiceImpl(ManagerService):

    def __init__(self, manager_dao: ManagerDao):
        self.manager_dao = manager_dao

    def login(self, user_name: str, password: str) -> Manager:
        return self.manager_dao.login(user_name, password)

    def view_all_requests(self) -> List[Reimbursement]:
        return self.manager_dao.view_all_requests()

    def judge_request(self, member_id: int, request_id: int, verdict: bool, comment: str) -> str:
        return self.manager_dao.judge_request(member_id, request_id, verdict, comment)

    def statistics(self) -> list:
        return self.manager_dao.statistics()

