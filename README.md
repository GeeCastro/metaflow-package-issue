# Metaflow package issue

This example shows a minimal setup with which I found inconsistencies in the package uplodaed to a metaflow task.

When listing the packge content with
```bash
python flow.py package list
```
The command returns the content of the .venv folder - which is not ideal!

However when downlading the package content using the `download_metaflow_package.py` script as per this [tutorial](https://docs.outerbounds.com/download-code-package/), the .venv is not included.
