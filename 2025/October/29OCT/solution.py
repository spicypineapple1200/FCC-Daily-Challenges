
def sort(emails):
    emails = sorted(emails)
    
    w_domain_order = sorted(set([item.split('@')[1].lower() for item in emails]))
    domain_order = sorted(set([item.split('@')[1].lower() for item in emails]))
    print(w_domain_order)
    
    name_order = sorted(set([item.split('@')[0] for item in emails]))
    print(domain_order)
    print(name_order)
    
    answer = []
    
    

    # answer = sorted(answer)
    # print(emails)
    print(answer)

# sort(["jill@mail.com", "john@example.com", "jane@example.com"])
# should return ["jane@example.com", "john@example.com", "jill@mail.com"].

sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"])
# should return ["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"].
