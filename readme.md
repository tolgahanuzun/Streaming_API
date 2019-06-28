# Standard and Streaming API examples with AIOHTTP library 


# How to install

```sh
git clone git@github.com:tolgahanuzun/Streaming_API.git
virtualenv -p python3 venv
source venv/bin/activate
cd Streaming_API
pip install -r requirement.txt
```

`vim settings.py`
and you need to edit the settings file yourself.


# How to run

#### Serve
```sh
python run.py
```


#### Client
- JWT needs it. You can remove it if you want.

```sh
curl -H 'Accept: text/plain' -H "Authorization: JWT eyJ0eX....."  -v http://0.0.0.0:8080/standard
```


```sh
curl -H 'Accept: text/plain' -H "Authorization: JWT eyJ0eX....."  -v http://0.0.0.0:8080/chunked
```


# Process analysis

Chunked data comes to you piece by piece.
In the standard, the data comes at once.
Incoming data sample.

![](/img/response_data.png)



## Standard Response

All data is captured, processed and sent at one time. Blocks each other. In this example, it corresponds to 500000 row.


- Up to 0.16 seconds no data flow occurs. The data comes after that second.

![](/img/standard_response.png)


## Streaming Response

The dataset size is 500000 rows. Data from the database is taken as 1000 row. Each group of data is processed and streamed without waiting.

- Up to 0.04 seconds no data flow occurs. The data comes after that second.

- Look out! The Streaming API finished before the Standard API started sending data. It didn't block itself because it sent and received data in pieces.

![](/img/chunked_response.png)


