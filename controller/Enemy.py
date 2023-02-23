from typing import List
from __database import get_session
from model.database import Enemy as EnemyModel
from utils import Debug, DebugLevel


class Enemy:
    @staticmethod
    async def get_by_id(target_id: int) -> EnemyModel:
        """
        Get the first result of Enemy by its id
        @param target_id: The id of the Enemy data
        @return: Enemy object
        """
        with get_session() as session:
            Enemy = session.query(EnemyModel).filter_by(id=target_id).first()

        return Enemy

    @staticmethod
    async def get_by_name(target_name: str) -> EnemyModel:
        """
        Get the first result of Enemy by its name
        @param target_name: The name of the Enemy data
        @return: Enemy object
        """
        with get_session() as session:
            Enemy = session.query(EnemyModel).filter_by(name=target_name).first()

        return Enemy
    
    @staticmethod
    async def get_all() -> List[EnemyModel]:
        """
        Get all result of Enemy data
        @return: List of Enemy object
        """
        with get_session() as session:
            Enemy = session.query(EnemyModel).all()
        return Enemy