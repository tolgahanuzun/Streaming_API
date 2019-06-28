'''
The data is standart response.
Postgresql database is being used.
Data from the database is taken as 500000 row.
The dataset size is 500000 rows.
All data is captured, processed and sent at one time. Blocks each other.
At the end of the transaction, the connection is disconnected.
'''

from aiopg.sa import create_engine
from aiohttp import web

import sqlalchemy as sa
from settings import user_name, database_name, host_name, query


async def handle(request):
    '''
    The standard Response object is used.
    '''
    async with create_engine(user=user_name, database=database_name, host=host_name) as engine:
        meta = sa.MetaData()
        meta.bind = engine

        async with engine.acquire() as conn:
            data = await conn.execute(query)
            fetch_data = await data.fetchall()
            sum_data = str()
            for fetch in fetch_data:
                sum_data = sum_data + 'object_id:{} \n'.format(fetch[0])
        return web.Response(text=sum_data)
