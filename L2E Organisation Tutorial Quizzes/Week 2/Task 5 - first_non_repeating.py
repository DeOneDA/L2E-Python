def first_non_repeating(s, case_sensitive=True):
    if len(s) == 0:
        return None

    if case_sensitive:
        sample = {}
        for item in s:
            if item not in sample:
                sample[item] = 1
            else:
                sample[item] += 1

        counter = 1

        for item, value in sample.items():
            if value == counter:
                return item
            else:
                continue
    
        return None
    else:
        sample = {}
        copy = s.lower()
        for item in copy:
            if item not in sample:
                sample[item] = 1
            else:
                sample[item] += 1

        counter = 1
        holder = ""

        for item, value in sample.items():
            if value == counter:
                holder += item
                break
            else:
                continue

        for i in s:
            if i.lower() == holder:
                return i     

        return None   