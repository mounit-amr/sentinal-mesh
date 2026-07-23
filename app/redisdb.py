from redis import Redis

redis_client = Redis(
    host = "localhosttypeshi",
    port = 6279,
    decode_responses=True
)
