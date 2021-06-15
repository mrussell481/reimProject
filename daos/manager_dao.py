from abc import ABC, abstractmethod
from typing import List
from entities.manager import Manager
from entities.reimbursement import Reimbursement


class ManagerDao(ABC):

    @abstractmethod
    def login(self, user_name: str, password: str) -> Manager:
        pass

    @abstractmethod
    def view_all_requests(self) -> List[Reimbursement]:
        pass

    # Should be exactly the same as the member version of this method.
    @abstractmethod
    def view_request(self, member_id: int, request_id: int) -> Reimbursement:
        pass

    @abstractmethod
    def judge_request(self, member_id: int, request_id: int, verdict: str, comment: str) -> str:
        pass

    @abstractmethod
    def statistics(self) -> list:
        pass
