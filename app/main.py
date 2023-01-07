from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, config
from app.database import engine
from app.routers import post, user, auth, vote

app = FastAPI()

origins = ["https://www.google.com",
           "https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# models.Base.metadata.create_all(bind=engine)

cursor = None
# try:
#     # conn = psycopg2.connect(
#     #     host="financedb.c2ricmkzarbg.ap-south-1.rds.amazonaws.com",
#     #     port=5432,
#     #     database="finance11",
#     #     user="postgres",
#     #     password="realmadrid"
#     # )

#     conn = psycopg2.connect(
#             host="localhost",
#             port=5432,
#             database="postgres",
#             user="postgres",
#             password="realmadrid",
#             cursor_factory=RealDictCursor
#         )
    
#     cursor = conn.cursor()
#     print("database connection successful")
# except Exception as err:
#     print("Connecting to database failed")
#     print("Error", err)

@app.get("/")
def root():
    return {"message": "Yes you have successfully reached this awesome API root"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello world !"}
