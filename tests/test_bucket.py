from models.bucket import Bucket

bucket = Bucket()

bucket.dig(20)
bucket.update(8.5)
bucket.status()

print()

bucket.dig(25)
bucket.update(10)
bucket.status()

print()

bucket.dump()
bucket.status()