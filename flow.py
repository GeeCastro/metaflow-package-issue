import json

from metaflow import S3, batch
from metaflow.flowspec import FlowSpec
from metaflow.decorators import step


class UseImageFlow(FlowSpec):
    @batch
    @step
    def start(self) -> None:
        print("Starting flow")

        self.next(self.step_a)

    @batch
    @step
    def step_a(self) -> None:
        print("Saving json")
        with S3(run=self) as s3:
            message = json.dumps({"message": "hello world!"})
            url = s3.put("example_object.json", message)
            print("Message saved at", url)
        self.next(self.end)

    @step
    def end(self) -> None:
        print("Flow finished")


if __name__ == "__main__":
    UseImageFlow()
