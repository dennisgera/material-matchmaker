"""Initial migration

Revision ID: 466a95f39e54
Revises: 
Create Date: 2024-01-14 18:01:52.127988

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '466a95f39e54'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('materials',
    sa.Column('id_material', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_material')
    )
    op.create_index(op.f('ix_materials_id_material'), 'materials', ['id_material'], unique=False)
    op.create_index(op.f('ix_materials_name'), 'materials', ['name'], unique=True)
    op.create_table('properties',
    sa.Column('id_property', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_property')
    )
    op.create_index(op.f('ix_properties_id_property'), 'properties', ['id_property'], unique=False)
    op.create_index(op.f('ix_properties_name'), 'properties', ['name'], unique=True)
    op.create_table('material_properties',
    sa.Column('id_material_property', sa.Integer(), nullable=False),
    sa.Column('id_material', sa.Integer(), nullable=False),
    sa.Column('id_property', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_material'], ['materials.id_material'], ),
    sa.ForeignKeyConstraint(['id_property'], ['properties.id_property'], ),
    sa.PrimaryKeyConstraint('id_material_property')
    )
    op.create_index(op.f('ix_material_properties_id_material_property'), 'material_properties', ['id_material_property'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_material_properties_id_material_property'), table_name='material_properties')
    op.drop_table('material_properties')
    op.drop_index(op.f('ix_properties_name'), table_name='properties')
    op.drop_index(op.f('ix_properties_id_property'), table_name='properties')
    op.drop_table('properties')
    op.drop_index(op.f('ix_materials_name'), table_name='materials')
    op.drop_index(op.f('ix_materials_id_material'), table_name='materials')
    op.drop_table('materials')
    # ### end Alembic commands ###
