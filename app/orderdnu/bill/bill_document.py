from datetime import datetime

from mongoengine import Document, StringField, ReferenceField, FloatField, ListField, DateTimeField, EnumField

from app.orderdnu.bill.bill_enum import BillStatusEnum
from app.orderdnu.order.order_document import OrderDocument
from app.orderdnu.user.user_document import UserDocument


class BillDocument(Document):
    user = ReferenceField(UserDocument, required=True)
    orders = ListField(ReferenceField(OrderDocument))
    bill_date = DateTimeField(default=datetime.utcnow)
    total_bill_amount = FloatField()
    status = EnumField(BillStatusEnum, default=BillStatusEnum.UNPAID)
    notes = StringField()

    def calculate_total(self):
        total = 0
        for order in self.orders:
            total += order.total_price
        self.total_bill_amount = total
        self.save()
