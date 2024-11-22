from dotenv import load_dotenv

load_dotenv()

from metaflow import Task, Flow, Run  # noqa: E402

# You can find your this info in the CLI logs
# If you run the Metaflow GUI it is also visible there
# Alternatively, if you use Outerbounds, find it in the dashboard
flow_name = "UseImageFlow"
run_id = "33566"
step_name = "run_in_container"
task_id = "310346"
task_pathspec = f"{flow_name}/{run_id}/{step_name}/{task_id}"

# use the Metaflow Client API
task = Task(task_pathspec)
EXTRACTION_PATH = f"package_{task_id}" # set EXTRACTION_PATH to your desired location
task.code.tarball.extractall(path=EXTRACTION_PATH)
