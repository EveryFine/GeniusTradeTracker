FROM public.ecr.aws/docker/library/python:3.12

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 13180

ENTRYPOINT ["python", "main.py"]
