def mad_libs_generator():

    # INPUTS
    name = input("Name: ")
    adjective = input("Adjective: ")
    noun = input("Noun: ")
    title = input("Title: ")
    number = input("Number: ")
    body_part = input("Body part: ")

    # TEMPLATE
    template = ("\nHi, I'm " + name + " and I love writing. \nI took my time and wrote the longest " + noun +
                " ever! \nI am really " + adjective + " and pleased with my work. \nI title it '" + title +
                "' and it totals " + number + " pages. \nI ran out of printer paper, so I printed it on my " +
                body_part + " and, Jesus Christ, did it hurt.")
    return template

