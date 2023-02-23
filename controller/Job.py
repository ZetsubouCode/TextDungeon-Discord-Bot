from typing import List
from datetime import date
from __database import get_session
from model.database import Job as JobModel
from utils import Debug, DebugLevel


class Job:
    @staticmethod
    async def get_by_id(target_id: int) -> JobModel:
        """
        Get the first result of Job by its id
        @param target_id: The id of the Job data
        @return: Job object
        """
        with get_session() as session:
            Job = session.query(JobModel).filter_by(id=target_id).first()

        return Job

    @staticmethod
    async def get_by_name(target_name: str) -> JobModel:
        """
        Get the first result of Job by its name
        @param target_name: The name of the Job data
        @return: Job object
        """
        with get_session() as session:
            Job = session.query(JobModel).filter_by(name=target_name).first()

        return Job
    
    @staticmethod
    async def get_all() -> List[JobModel]:
        """
        Get all result of Job data
        @return: List of Job object
        """
        with get_session() as session:
            Job = session.query(JobModel).all()
        return Job