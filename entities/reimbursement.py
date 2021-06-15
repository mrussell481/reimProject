class Reimbursement:
    def __init__(self, rb_id: int, rb_name: str, sender: str, reason: str, amount: float, date: int, approved: str,
                 comment: str, fk_mem_id: int):
        self.rb_id = rb_id
        self.rb_name = rb_name
        self.sender = sender
        self.reason = reason
        self.amount = amount
        self.date = date
        self.approved = approved
        self.comment = comment
        self.fk_mem_id = fk_mem_id

    def as_json_dict(self):
        return{
            "reimbursementId": self.rb_id,
            "reimbursementName": self.rb_name,
            "sender": self.sender,
            "reason": self.reason,
            "amount": self.amount,
            "date": self.date,
            "approved": self.approved,
            "comment": self.comment,
            "memberId": self.fk_mem_id
        }
