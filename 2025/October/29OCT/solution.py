def sort(emails):
    w_domain_order = sorted(set([item.split('@')[1].lower() for item in emails]))
    answer = []
    for w_domain in w_domain_order:
        name_list = []
        for email in emails:
            domain = email.split('@')[1]
            if domain.lower() == w_domain:
                name = email.split('@')[0]
                name_list.append(name)
            name_list = sorted(name_list, key=str.lower)
        answer+=name_list
        name_list = answer
        answer = []
        for w_domain in w_domain_order:
            for name in name_list:
                for email in emails:
                    domain = email.split('@')[1].lower()
                    if name in email and w_domain == domain and email not in answer:
                        answer.append(email)
    print(answer)
    return answer
