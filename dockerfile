FROM python:slim

WORKDIR /work/
RUN chown 1001 /work \
    && chmod "g+rwX" /work \
    && chown 1001:root /work

COPY --chown=1001:root requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY --chown=1001:root . .

CMD [ "python", "-m" , "script.py"]