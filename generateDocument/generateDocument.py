def generateDocument(characters, document):
    lst = list(characters)
    for idx in range(len(document)):
        doc_chr = document[idx]
        if doc_chr in lst:
            lst.remove(doc_chr)
            continue
        else:
            return False
    return True