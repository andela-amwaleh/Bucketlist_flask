import os

POSTS_PER_PAGE = 20
MAX_PAGES = 100
if 'travis' is not os.environ:
	TEST_DB = 'postgresql://127.0.0.1/Bucket_test'
DATABASE_URI = 'postgresql://localhost/flask'
SECRET = "development-Key2"
