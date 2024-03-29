"""add name to material_property

Revision ID: 790c7229f16f
Revises: 466a95f39e54
Create Date: 2024-01-15 08:53:07.697605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '790c7229f16f'
down_revision: Union[str, None] = '466a95f39e54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('material_properties', sa.Column('name', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('material_properties', 'name')
    # ### end Alembic commands ###
