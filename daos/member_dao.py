from abc import ABC, abstractmethod
from typing import List
from entities.member import Member
from entities.reimbursement import Reimbursement


class MemberDao(ABC):

    @abstractmethod
    def login(self, user_name: str, password: str) -> Member:
        pass

    @abstractmethod
    def view_member_requests(self, member_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def view_request(self, member_id: int, request_id: int) -> Reimbursement:
        pass

    @abstractmethod
    def create_request(self, reim: Reimbursement) -> str:
        pass
