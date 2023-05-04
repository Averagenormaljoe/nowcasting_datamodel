"""

Switch to use metric_value.model_name instead of metric_value.model_id

Revision ID: caea7b5cf249
Revises: 37c68fd8e65c
Create Date: 2023-04-14 15:45:13.418891

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "caea7b5cf249"
down_revision = "37c68fd8e65c"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column("metric_value", sa.Column("model_name", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("metric_value", "model_name")
    # ### end Alembic commands ###
