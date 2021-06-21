from daos.member_dao import MemberDao
from daos.member_dao_impl import MemberDaoImpl
from entities.member import Member
from entities.reimbursement import Reimbursement


member_dao: MemberDao = MemberDaoImpl()


def test_member_login():
    member: Member = member_dao.login("realrocky46", "jkcbn43857qo")
    assert member.mem_name == "Rocky Holmes"


def test_view_member_requests():
    assert len(member_dao.view_member_requests(1)) > 6


def test_new_request():
    new_request = Reimbursement(0,
                                "Pytest Bug",
                                "Mizutani",
                                "Pytest can submit its own bugs!",
                                0,
                                893,
                                None,
                                None,
                                2)
    assert member_dao.create_request(new_request) == "Successfully added your reimbursement."
