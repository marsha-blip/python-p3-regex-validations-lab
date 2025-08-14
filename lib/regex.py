
import re

name_regex = re.compile(
    r"^[A-Z](?:[a-z]+(?:['\-.][A-Za-z]+)*|(?:['\-.][A-Za-z]+)+)"
    r"(?: [A-Z][a-z]*(?:['\-.][A-Za-z]+)*)*$"
)

phone_regex = re.compile(
    r"^(?:\d{10}|\(\d{3}\)\s*\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$"
)

email_regex = re.compile(
    r"^[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)




