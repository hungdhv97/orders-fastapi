from typing import Annotated

from fastapi import Body, Query, Path

from app.common.annotation.openapi_examples import CREATE_MERCHANT_EXAMPLES, CREATE_USER_EXAMPLES, UPDATE_USER_EXAMPLES, \
    REGISTER_EXAMPLES, LOGIN_EXAMPLES
from app.orderdnu.auth.auth_model import RegisterRequest, LoginRequest
from app.orderdnu.merchant.merchant_model import CreateMerchantRequest
from app.orderdnu.user.user_model import CreateUserRequest, UpdateUserRequest

ClientMerchantIdPath = Annotated[str, Path(example="5-C3C2T8MUVN4HLT")]
ObjectIdPath = Annotated[str, Path(example="64f6318231e3ac649c61d2e8")]
UserNamePath = Annotated[str, Path(example="nghia.nguyen4")]

ObjectIdQuery = Annotated[str, Query(example="64f6318231e3ac649c61d2e8")]

CreateMerchantRequestBody = Annotated[CreateMerchantRequest, Body(openapi_examples=CREATE_MERCHANT_EXAMPLES)]
CreateUserRequestBody = Annotated[CreateUserRequest, Body(openapi_examples=CREATE_USER_EXAMPLES)]
LoginRequestBody = Annotated[LoginRequest, Body(openapi_examples=LOGIN_EXAMPLES)]
RegisterRequestBody = Annotated[RegisterRequest, Body(openapi_examples=REGISTER_EXAMPLES)]
UpdateUserRequestBody = Annotated[UpdateUserRequest, Body(openapi_examples=UPDATE_USER_EXAMPLES)]
