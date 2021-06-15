from typing import List
from daos.member_dao import MemberDao
from entities.member import Member
from entities.reimbursement import Reimbursement
from utils.connection_util import connection


class MemberDaoImpl(MemberDao):

    def login(self, user_name: str, password: str) -> Member:
        pass

    def view_member_requests(self, member_id: int) -> List[Reimbursement]:
        pass

    def view_request(self, member_id: int, request_id: int) -> Reimbursement:
        pass

    def create_request(self, reim: Reimbursement) -> str:
        pass
