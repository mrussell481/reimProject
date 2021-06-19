from typing import List
from daos.manager_dao import ManagerDao
from entities.manager import Manager
from entities.reimbursement import Reimbursement
from utils.connection_util import connection


class ManagerDaoImpl(ManagerDao):

    def login(self, user_name: str, password: str) -> Manager:
        cursor = connection.cursor()
        sql = """select * from manager where man_user = '{}' and man_pass = '{}';""".format(user_name, password)
        cursor.execute(sql)
        record = cursor.fetchone()
        user = Manager(*record)
        return user

    def view_all_requests(self) -> List[Reimbursement]:
        cursor = connection.cursor()
        sql = """select * from reimbursement order by rb_id desc;"""
        cursor.execute(sql)
        records = cursor.fetchall()
        request_list = []
        for x in records:
            request_list.append(Reimbursement(*x))
        return request_list

    def judge_request(self, member_id: int, request_id: int, verdict: bool, comment: str) -> str:
        cursor = connection.cursor()
        sql = """update reimbursement set approved = {} where mem_id = {} and rb_id = {};""".format(verdict,
                                                                                                      member_id,
                                                                                                      request_id)
        cursor.execute(sql)
        if len(comment) > 0:
            sql = """update reimbursement set man_comment = '{}' where mem_id = {} and rb_id = {}""".format(comment,
                                                                                                        member_id,
                                                                                                        request_id)
            cursor.execute(sql)
        connection.commit()
        return "Successfully updated approval status."

    def statistics(self) -> list:
        pass
