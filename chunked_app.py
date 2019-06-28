'''
The data is streamed.
Postgresql database is being used.
Data from the database is taken as 1000 row.
The dataset size is 500000 rows.
Each group of data is processed and streamed without waiting
At the end of the transaction, the connection is disconnected.
'''

from aiopg.sa import create_engine
from aiohttp import web

import sqlalchemy as sa
from settings import user_name, database_name, host_name, query



async def handle(request):
    '''
    The Response object needs to be StreamResponse.
    '''

    response = web.StreamResponse(
        status=200,
        reason='OK',
        headers={'Content-Type': 'text/plain', 'X-Accel-Buffering': 'no'},
    )
    response.enable_chunked_encoding()

    await response.prepare(request)

    async with create_engine(user=user_name, database=database_name, host=host_name) as engine:
        meta = sa.MetaData()
        meta.bind = engine

        async with engine.acquire() as conn:
            data = await conn.execute(query)
            while True:
                fetch_data = await data.fetchmany(1000)
                sum_data = str()
                for fetch in fetch_data:
                    sum_data = sum_data + 'object_id:{} \n'.format(fetch[0])
                await response.write(sum_data.encode())

        await response.write_eof()
        await response.close()
        return response
