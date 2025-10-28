def navigate(commands):
    active_pages = ['Home']
    page_index = 0
    for item in commands:
        if 'Visit' in item:
            item = item[6:]
            if item not in active_pages:
                active_pages.append(item)
                page_index = active_pages.index(item)
            else:page_index = active_pages.index(item)
        else:
            if item == 'Back':
                page_index-=1
                if page_index<0:page_index=0
            elif item == 'Forward':
                page_index+=1
                if page_index>(len(active_pages)-1):page_index=len(active_pages)-1
    answer = active_pages[page_index]
    print(answer)
    return answer
