FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY biogpt.py ./

CMD ["biogpt.lambda_handler"]

