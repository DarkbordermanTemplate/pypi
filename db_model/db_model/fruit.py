from sqlalchemy import INT, VARCHAR, Column

from .base import BASE


class Fruit(BASE):

    __tablename__ = "fruit"

    name = Column(VARCHAR, primary_key=True)
    count = Column(INT, nullable=False)

    def dumps(self):
        return {"name": self.name, "count": self.count}
