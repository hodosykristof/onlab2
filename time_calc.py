def time_to_string(t_float):
    if t_float < 10:
        return "0" + str(t_float)
    else:
        return str(t_float)


def increase_time_by_seconds(datetime, seconds):
    split_date = datetime.split()
    date = split_date[0]
    time = split_date[1]
    split_time = time.split(':')
    hour = int(split_time[0])
    minute = int(split_time[1])
    sec = int(split_time[2])
    secs = int(float(seconds)) + hour * 3600 + minute * 60 + sec
    hour, minute = divmod(secs, 3600)
    minute, sec = divmod(secs - int(hour) * 3600, 60)

    hour_str = time_to_string(hour)
    min_str = time_to_string(minute)
    sec_str = time_to_string(sec)

    return date + " " + hour_str + ":" + min_str + ":" + sec_str
