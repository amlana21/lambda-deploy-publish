FROM public.ecr.aws/lambda/python:3.8
COPY main.py requirements.txt ./
RUN python3.8 -m pip install -r requirements.txt -t .
CMD ["main.lambda_handler"]
