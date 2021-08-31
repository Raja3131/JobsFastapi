import datetime, uuid
import model as jobss
from pg_db import database, jobs
from fastapi import FastAPI
from typing import List

app = FastAPI(
    docs_url="/docs",
    redoc_url="/api/v2/redocs",
    title="API",
    description="Job App",

)


# Start database connection
@app.on_event("startup")
async def startup():
    await database.connect()


# Disconnects database connection
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Recruiter View
# To List and see all the jobs By Recruiter
@app.get("/jobs", response_model=List[jobss.JobList], tags=["Jobs"])
async def find_all_jobs():
    query = jobs.select()
    return await database.fetch_all(query)


# Post New Job
@app.post("/jobs", response_model=jobss.JobList, tags=["Jobs"])
async def register_job(job: jobss.JobEntry):
    gID = str(uuid.uuid1())
    gDate = str(datetime.datetime.now())
    query = jobs.insert().values(
        id=gID,
        title=job.title,
        description=job.description,
        create_at=gDate,
    )

    await database.execute(query)  # execute query
    return {
        "id": gID,
        **job.dict(),
        "create_at": gDate,
        "status": "1"
    }


# To see particular Job by using job id
@app.get("/jobs/{jobId}", response_model=jobss.JobList, tags=["Jobs"])
async def find_job_by_id(jobId: str):
    query = jobs.select().where(jobs.c.id == jobId)
    return await database.fetch_one(query)


# update an existing job by its jobId
@app.put("/jobs", response_model=jobss.JobList, tags=["Jobs"])
async def update_jobs(job: jobss.JobUpdate):
    gDate = str(datetime.datetime.now())
    query = jobs.update(). \
        where(jobs.c.id == job.id). \
        values(
        title=job.title,
        description=job.description,
        create_at=gDate,
    )
    await database.execute(query)

    return await find_job_by_id(job.id)


# delete job by using id
@app.delete("/jobs/{jobId}", tags=["Jobs"])
async def delete_job(job: jobss.JobDelete):
    query = jobs.delete().where(jobs.c.id == job.id)
    await database.execute(query)

    return {
        "status": True,
        "message": "This Job has been deleted successfully."
    }


# Candidate View

# To view the jobs by Candidate
@app.get("/candidate/jobs", response_model=List[jobss.JobList], tags=["Jobs"])
async def find_all_jobs():
    query = jobs.select()
    return await database.fetch_all(query)


# Can apply for the job by using id
@app.post("candidate/jobs/{jobId}", response_model=jobss.JobList, tags=["Jobs"])
async def find_job_by_id(jobId: str):
    query = jobs.select().where(jobs.c.id == jobId)
    return await database.fetch_one(query)
