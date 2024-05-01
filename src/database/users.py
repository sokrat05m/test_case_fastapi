
from datetime import timezone

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database.config import Base


class User(Base):
    __tablename__ = 'users_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    phone: Mapped[str] = mapped_column(String(30))
