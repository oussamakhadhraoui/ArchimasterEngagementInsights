"""3rd change

Revision ID: 4cc1607af8f4
Revises: 4dd47be2cd5c
Create Date: 2023-08-04 11:30:33.550600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cc1607af8f4'
down_revision = '4dd47be2cd5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetingTestCSV',
    sa.Column('MeetingTestID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('StartDate', sa.Date(), nullable=True),
    sa.Column('StartTime', sa.Time(), nullable=True),
    sa.Column('EndDate', sa.Date(), nullable=True),
    sa.Column('EndTime', sa.Time(), nullable=True),
    sa.Column('Title', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('MeetingTestID')
    )
    op.create_table('personTestCSV',
    sa.Column('PersonTestID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('FirstName', sa.String(length=256), nullable=True),
    sa.Column('LastName', sa.String(length=256), nullable=True),
    sa.Column('Email', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('PersonTestID')
    )
    op.create_table('attendanceTestCSV',
    sa.Column('AttendanceTestID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PersonTestID', sa.Integer(), nullable=True),
    sa.Column('MeetingTestID', sa.Integer(), nullable=True),
    sa.Column('AttendanceDuration', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['MeetingTestID'], ['meetingTestCSV.MeetingTestID'], ),
    sa.ForeignKeyConstraint(['PersonTestID'], ['personTestCSV.PersonTestID'], ),
    sa.PrimaryKeyConstraint('AttendanceTestID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attendanceTestCSV')
    op.drop_table('personTestCSV')
    op.drop_table('meetingTestCSV')
    # ### end Alembic commands ###
