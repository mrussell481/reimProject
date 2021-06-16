from typing import List
from daos.member_dao import MemberDao
from entities.member import Member
from entities.reimbursement import Reimbursement
from utils.connection_util import connection


class MemberDaoImpl(MemberDao):

    def login(self, user_name: str, password: str) -> Member:
        cursor = connection.cursor()
        sql = """select * from site_member where mem_user = '{}' and mem_pass = '{}';""".format(user_name, password)
        cursor.execute(sql)
        record = cursor.fetchone()
        user = Member(*record)
        return user

    def view_member_requests(self, member_id: int) -> List[Reimbursement]:
        cursor = connection.cursor()
        sql = """select * from reimbursement where mem_id = '{}' order by rb_date;""".format(member_id)
        cursor.execute(sql)
        records = cursor.fetchall()
        request_list = []
        for x in records:
            request_list.append(Reimbursement(*x))
        return request_list

    #def view_request(self, member_id: int, request_id: int) -> Reimbursement:
    #    pass

    def create_request(self, reim: Reimbursement) -> str:
        cursor = connection.cursor()
        sql = """insert into reimbursement (rb_name, sender, reason, amount, rb_date, mem_id)
        values ('{}', '{}', '{}', {}, {}, {});""".format(reim.rb_name, reim.sender, reim.reason,
                                                                 reim.amount, reim.date, reim.fk_mem_id)
        cursor.execute(sql)
        connection.commit()
        return "Successfully added your reimbursement."
