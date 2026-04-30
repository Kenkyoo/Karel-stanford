from ai import call_gpt

def main():
    # TODO: your code here
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    response = call_gpt(f"Write a haiku about a person named {name} and the topic for {topic}")
    if response:
        print(response)
    else:
        print("Creating your haiku...")


if __name__ == "__main__":
    main()
