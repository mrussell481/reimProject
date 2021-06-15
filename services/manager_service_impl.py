from typing import List
from daos.manager_dao import ManagerDao
from entities.manager import Manager
from entities.reimbursement import Reimbursement
from services.manager_service import ManagerService


class ManagerServiceImpl(ManagerService):

    def __init__(self, manager_dao: ManagerDao):
        self.manager_dao = manager_dao

    def login(self, user_name: str, password: str) -> Manager:
        pass

    def view_all_requests(self) -> List[Reimbursement]:
        pass

    def view_request(self, member_id: int, request_id: int) -> Reimbursement:
        pass

    def judge_request(self, member_id: int, request_id: int, verdict: str, comment: str) -> str:
        pass

    def statistics(self) -> list:
        pass

