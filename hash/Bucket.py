class Bucket():
    bucket_name : str
    bucket_id : str
    bucket_vector : list = []

    def __init__(self, bucket_name, bucket_id):
        self.bucket_name = bucket_name
        self.bucket_id = bucket_id
        self.bucket_vector = []