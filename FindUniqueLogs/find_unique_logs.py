import re


# Function that prints only messages with certain severity or higher (and groups them together, so looking for
# i.e. warning is easier)
def print_texts_with_severity(texts, severity):
    # print errors
    for text in texts:
        if "ERROR" in text:
            print(text)

    if severity == "WARN" or severity == "INFO":
        # print warnings
        for text in texts:
            if "WARN" in text:
                print(text)

    if severity == "INFO":
        # print info
        for text in texts:
            if "INFO" in text:
                print(text)


# date would be always different we need to remove it and create set of every unique message
def get_unique_texts_from_file(file_name):
    texts = set()

    # date format
    expression = re.compile("\d{4} [a-zA-Z]{3} \d{1,2} \d\d:\d\d:\d\d\.\d{6}")
    with open(file_name) as file:
        for line in file:
            # find date format
            result = expression.match(line)
            date_len = len(result.group())
            # remove date
            texts.add(line[date_len:])

    return texts


messages = get_unique_texts_from_file('wpeframework.log')
print_texts_with_severity(messages, "WARN")

