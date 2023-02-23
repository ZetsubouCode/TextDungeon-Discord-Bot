from typing import List
from __database import get_session
from model.database import Effect as EffectModel
from utils import Debug, DebugLevel


class Effect:
    @staticmethod
    async def get_by_id(target_id: int) -> EffectModel:
        """
        Get the first result of Effect by its id
        @param target_id: The id of the Effect data
        @return: Effect object
        """
        with get_session() as session:
            Effect = session.query(EffectModel).filter_by(id=target_id).first()

        return Effect

    @staticmethod
    async def get_by_name(target_name: str) -> EffectModel:
        """
        Get the first result of Effect by its name
        @param target_name: The name of the Effect data
        @return: Effect object
        """
        with get_session() as session:
            Effect = session.query(EffectModel).filter_by(name=target_name).first()

        return Effect
    
    @staticmethod
    async def get_all() -> List[EffectModel]:
        """
        Get all result of Effect data
        @return: List of Effect object
        """
        with get_session() as session:
            Effect = session.query(EffectModel).all()
        return Effect