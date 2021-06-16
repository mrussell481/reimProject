from typing import List
from daos.member_dao import MemberDao
from entities.member import Member
from entities.reimbursement import Reimbursement
from services.member_service import MemberService


class MemberServiceImpl(MemberService):

    def __init__(self, member_dao: MemberDao):
        self.member_dao = member_dao

    def login(self, user_name: str, password: str) -> Member:
        return self.member_dao.login(user_name, password)

    def view_member_requests(self, member_id: int) -> List[Reimbursement]:
        return self.member_dao.view_member_requests(member_id)

    #def view_request(self, member_id: int, request_id: int) -> Reimbursement:
    #    pass

    def create_request(self, reim: Reimbursement) -> str:
        return self.member_dao.create_request(reim)
