import logging
from fastapi import APIRouter, BackgroundTasks


logger = logging.getLogger(__name__)

background_tasks_router = APIRouter(prefix="/jobs", tags=["jobs"])


def write_notification(email: str, message=""):
    with open("log.log", mode="a") as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)


@background_tasks_router.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
