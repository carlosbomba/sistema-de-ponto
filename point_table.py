from sqlalchemy.orm import declarative_base, column_property
from sqlalchemy import Column, String, Integer, DateTime, Boolean, LargeBinary, func
from sqlalchemy import func
import datetime

Base = declarative_base()

class PointTable(Base):
    #descrevendo o que temos no banco de dados
    __tablename__ = "dag_run"

    id = Column(Integer, primary_key=True)
    dag_id = Column(String, nullable=False)
    execution_date = Column(DateTime(timezone=True), nullable=False)
    state = Column(String, nullable=True)
    run_id = Column(String, nullable=False)
    external_trigger = Column(Boolean, nullable=True)
    conf = Column(LargeBinary, nullable=True)
    end_date = Column(DateTime(timezone=True), nullable=True)
    start_date = Column(DateTime(timezone=True), nullable=True)
    run_type = Column(String, nullable=False)
    last_scheduling_decision = Column(DateTime(timezone=True), nullable=True)
    dag_hash = Column(String, nullable=True)
    creating_job_id = Column(Integer, nullable=True)
    queued_at = Column(DateTime(timezone=True), nullable=True)
    data_interval_start = Column(DateTime(timezone=True), nullable=True)
    data_interval_end = Column(DateTime(timezone=True), nullable=True)
    log_template_id = Column(Integer, nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)

    datetime = column_property(func.to_char(execution_date, 'YYYY-MM-DD HH24:MI:SS'))
    elapsed = column_property(func.to_char(end_date - start_date, 'HH24:MI:SS'))
