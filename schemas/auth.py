from pydantic import BaseModel, field_validator

class Register(BaseModel):
    name: str
    email: str
    password: str

    @field_validator("password")
    def check_password_length(cls, v):
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password terlalu panjang (maks 72 byte)")
        if len(v) < 6:
            raise ValueError("Password minimal 6 karakter")
        return v

class Login(BaseModel):
    email: str
    password: str