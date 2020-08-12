import re

p = re.compile('^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')

def fun(test_case):
    return True if p.match(test_case) else False

def filter_mail(emails):
    return list(filter(fun, emails))



if __name__ == '__main__':
    f = open("data.txt", "r")

    n = int(f.readline().strip())
    emails = []
    for _ in range(n):
        emails.append(f.readline().strip())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)