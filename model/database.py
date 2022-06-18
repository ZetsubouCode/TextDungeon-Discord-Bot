from sqlalchemy import Column, DECIMAL, DateTime, Enum, ForeignKey, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Effect(Base):
    __tablename__ = 'effect'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    duration = Column(INTEGER(11), nullable=False)
    amount = Column(INTEGER(11), nullable=False)


class Enemy(Base):
    __tablename__ = 'enemy'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    hp = Column(INTEGER(11), nullable=False)
    mp = Column(INTEGER(11), nullable=False, server_default=text("0"))
    type = Column(Enum('BOSS', 'NORMAL'), nullable=False)
    description = Column(Text, nullable=False)


class Job(Base):
    __tablename__ = 'job'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    hp = Column(INTEGER(11), nullable=False)
    mp = Column(INTEGER(11), nullable=False, server_default=text("0"))
    deffend = Column(INTEGER(11), nullable=False)
    eva = Column(INTEGER(11), nullable=False)
    description = Column(Text, nullable=False)


class Progres(Base):
    __tablename__ = 'progress'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    last_layer = Column(INTEGER(11), nullable=False, server_default=text("1"))
    last_room = Column(INTEGER(11), nullable=False, server_default=text("1"))


class EnemyGroup(Base):
    __tablename__ = 'enemy_group'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    progress_id = Column(ForeignKey('progress.id'), primary_key=True, autoincrement=True, nullable=False, index=True)
    enemy_id = Column(ForeignKey('enemy.id'), primary_key=True, autoincrement=True, nullable=False, index=True)

    enemy = relationship('Enemy')
    progress = relationship('Progres')


class Move(Base):
    __tablename__ = 'move'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=False)
    damage = Column(INTEGER(11), nullable=False)
    effect_id = Column(ForeignKey('effect.id'), primary_key=True, autoincrement=True, nullable=False, index=True)

    effect = relationship('Effect')


class Player(Base):
    __tablename__ = 'player'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    job_id = Column(ForeignKey('job.id'), primary_key=True, autoincrement=True, nullable=False, index=True)
    discord_name = Column(Text, nullable=False)
    exp = Column(INTEGER(11), nullable=False, server_default=text("0"))
    level = Column(INTEGER(11), nullable=False, server_default=text("1"))
    add_attack = Column(INTEGER(11), nullable=False, server_default=text("0"))
    add_defend = Column(INTEGER(11), nullable=False, server_default=text("0"))
    add_eva = Column(INTEGER(11), nullable=False, server_default=text("1"))

    job = relationship('Job')


class Weapon(Base):
    __tablename__ = 'weapon'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    job_id = Column(ForeignKey('job.id'), primary_key=True, autoincrement=True, nullable=False, index=True)
    damage = Column(INTEGER(11), nullable=False)

    job = relationship('Job')


class Item(Base):
    __tablename__ = 'item'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    effect_id = Column(ForeignKey('effect.id'), primary_key=True, autoincrement=True, nullable=False, index=True)
    weapon_id = Column(ForeignKey('weapon.id'), nullable=False, index=True)
    name = Column(Text, nullable=False)
    type = Column(Enum('potion', 'key', 'weapon'), nullable=False)
    key_effect = Column(Enum('heal', 'burn', 'freeze', 'stun', 'damage', 'splash_damage', 'poison'))
    description = Column(Text, nullable=False)
    chance = Column(DECIMAL(10, 0), nullable=False)

    effect = relationship('Effect')
    weapon = relationship('Weapon')


class MoveSet(Base):
    __tablename__ = 'move_set'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    enemy_id = Column(ForeignKey('enemy.id'), primary_key=True, autoincrement=True, nullable=False, index=True)
    move_id = Column(ForeignKey('move.id'), primary_key=True, autoincrement=True, nullable=False, index=True)

    enemy = relationship('Enemy')
    move = relationship('Move')


class RunHistory(Base):
    __tablename__ = 'run_history'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    player_id = Column(ForeignKey('player.id'), primary_key=True, autoincrement=True, nullable=False, index=True)
    progress_id = Column(ForeignKey('progress.id'), primary_key=True, autoincrement=True, nullable=False, index=True)
    date_created = Column(DateTime, nullable=False, server_default=text("current_timestamp()"))
    finish_time = Column(DateTime)

    player = relationship('Player')
    progress = relationship('Progres')


class DetailRunHistory(Base):
    __tablename__ = 'detail_run_history'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    action = Column(Text, nullable=False)
    detail = Column(Text)
    run_history_id = Column(ForeignKey('run_history.id'), primary_key=True, autoincrement=True, nullable=False, index=True)

    run_history = relationship('RunHistory')


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True, nullable=False)
    player_id = Column(ForeignKey('player.id'), primary_key=True, autoincrement=True, nullable=False, index=True)
    item_id = Column(ForeignKey('item.id'), primary_key=True, autoincrement=True, nullable=False, index=True)
    quantity = Column(INTEGER(11), nullable=False)

    item = relationship('Item')
    player = relationship('Player')