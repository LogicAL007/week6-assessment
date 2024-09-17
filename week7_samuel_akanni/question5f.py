#Kwargs
def samuel_calling(**details):
    responses = ', '.join(f"{key}: {value}" for key, value in details.items())
    return f"Samuel heard the Lord calling, and Eli guided him to respond: {responses}. Samuel answered, 'Speak, for your servant is listening.'"


print(samuel_calling(call="Samuel", guidance="Go back and lie down, if called again, say 'Speak, Lord'"))
