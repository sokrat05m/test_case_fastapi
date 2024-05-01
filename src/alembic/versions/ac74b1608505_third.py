"""third

Revision ID: ac74b1608505
Revises: f88b4759c69d
Create Date: 2024-04-30 13:22:48.897403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac74b1608505'
down_revision: Union[str, None] = 'f88b4759c69d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products_table', 'subcategory_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products_table', 'subcategory_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
