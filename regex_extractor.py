import re

REGEX_PATTERNS = {
    "email": re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    ),
    "phone": re.compile(
        r"^(\+?\d{1,3}[-.\s]?)?(\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}$"
    ),
    "url": re.compile(
        r"^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[^\s]*)?$"
    ),
    "credit_card": re.compile(
        r"^(?:\d{4}[-\s]?){3}\d{4}$"
    ),
    "hashtags": re.compile(
        r"^#\w{1,100}$"
    )
}

def validate_input(input_type, user_input):
    """
    Validates user input against the appropriate regex pattern.
    """
    pattern = REGEX_PATTERNS.get(input_type)
    if not pattern:
        return "Unknown input type."

    if pattern.fullmatch(user_input.strip()):
        return f"Valid {input_type.replace('_', ' ')}"
    else:
        return f"Invalid {input_type.replace('_', ' ')}"

def main():
    print("=== Input Validator===")
    print("You can validate the following: email, phone, url, credit_card, hashtag")
    print("Type 'exit' at any time to quit.\n")

    while True:
        input_type = input("Enter type to validate (email/phone/url/credit_card/hashtag): ").strip().lower()
        if input_type == "exit":
            break
        elif input_type not in REGEX_PATTERNS:
            print("Invalid type. Choose from: email, phone, url, credit_card, hashtag\n")
            continue

        user_input = input(f"Enter the {input_type.replace('_', ' ')} to validate: ").strip()
        if user_input.lower() == "exit":
            break

        result = validate_input(input_type, user_input)
        print(result + "\n" + "-"*40)

    print("Goodbye!")

if __name__ == "__main__":
    main()

