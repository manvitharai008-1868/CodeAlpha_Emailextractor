import re

print("=" * 50)
print("      EMAIL EXTRACTOR USING PYTHON")
print("=" * 50)

try:
   
    with open("input.txt", "r") as file:
        content = file.read()

   
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

   
    emails = re.findall(pattern, content)

    if emails:
      
        with open("emails.txt", "w") as output:
            output.write("Extracted Email Addresses\n")
            output.write("-" * 30 + "\n")

            for email in emails:
                output.write(email + "\n")

        print("\nEmail addresses extracted successfully!\n")

        print("Extracted Email Addresses:")
        print("-" * 30)

        for email in emails:
            print(email)

        print("\nResults have been saved to emails.txt")

    else:
        print("No email addresses found in the file.")

except FileNotFoundError:
    print("Error: input.txt file not found.")