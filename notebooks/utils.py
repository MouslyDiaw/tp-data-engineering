""" Utility functions """

import pendulum
from typing import Union

from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.decl_api import DeclarativeMeta


def recreate_database(meta_base: DeclarativeMeta, engine: Engine) -> None:
    """ Drop all tables and recreate them
    
    Args:
        meta_base (DeclarativeMeta): metadata base
        engine (Engine): sqlachemy engine
    
    Return:
        None

    """
    meta_base.metadata.drop_all(engine)
    meta_base.metadata.create_all(engine)

def dateparser(time_in_secs: Union[str, int, float]) -> pendulum.datetime:
    """Function to use for converting a sequence of string columns to datetime
    
    Args:
        time_in_secs (Union[str, int, float])

    Return:
        pendulum.datetime.DateTime: date time instance from a timestamp
        
    Notes:
        dateparser(1761962267) will return DateTime(2025, 11, 1, 1, 57, 47, tzinfo=Timezone('UTC'))
    """
    return pendulum.from_timestamp(int(time_in_secs))