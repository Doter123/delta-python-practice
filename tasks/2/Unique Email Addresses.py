

emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]


result = set()

for email in emails:

    [name, domain] = email.split('@')

    if '+' in name:
        name = name.split('+')[0]

    name = name.replace('.','')

    result.add(name + '@' + domain)

print(len(result))




























# def parse(email):
#     local, domain = email.split('@')
#     local = local.split('+')[0].replace('.',"")
#     return f"{local}@{domain}"

# print(len(set(map(parse, emails))))