from datetime import datetime
from typing import Annotated, Optional

from pydantic import Field

from app.orderdnu.merchant.merchant_enum import DeliveryEnum

MerchantIdField = Annotated[str, Field(examples=["5-C3C2T8MUVN4HLT"])]
ObjectIdField = Annotated[str, Field(examples=["64f6318231e3ac649c61d2e8"])]
UserNameField = Annotated[str, Field(examples=["nghia.nguyen4"])]
PasswordField = Annotated[str, Field(examples=["1234"])]
FullNameField = Annotated[str, Field(examples=["Nguyễn Bá Nghĩa"])]
ProductNameField = Annotated[str, Field(examples=["Cơm gà"])]
PriceField = Annotated[int, Field(examples=[40000])]
QuantityField = Annotated[int, Field(examples=[1])]
TotalPriceField = Annotated[int, Field(examples=[100_000])]
DateTimeField = Annotated[str, Field(examples=[datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')])]
NoteField = Annotated[str, Field(default="", examples=["Không hành"])]

OptionalUserNameField = Annotated[Optional[str], Field(default=None, examples=["nghia.nguyen4"])]
OptionalPasswordField = Annotated[Optional[str], Field(default=None, examples=["1234"])]
OptionalFullNameField = Annotated[Optional[str], Field(default=None, examples=["Nguyễn Bá Nghĩa"])]

DeliveryTypeField = Annotated[DeliveryEnum, Field(examples=[DeliveryEnum.GRAB])]
