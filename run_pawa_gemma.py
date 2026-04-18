from transformers import pipeline

print("Loading model...")
pipe = pipeline(
    "text-generation",
    model="sartifyllc/Pawa-Gemma-Swahili-2B",
    model_kwargs={"local_files_only": True},
    device_map="auto",
)
print("Model ready!\n")

messages = []

print("Pawa-Gemma Swahili 2B — type 'exit' to quit, 'clear' to reset chat\n")

while True:
    user_input = input("Wewe: ").strip()

    if not user_input:
        continue
    if user_input.lower() in ("exit", "quit"):
        print("Kwaheri!")
        break
    if user_input.lower() == "clear":
        messages = []
        print("--- mazungumzo yamesafishwa ---\n")
        continue

    messages.append({"role": "user", "content": user_input})

    result = pipe(messages, max_new_tokens=200)

    # extract the last assistant reply
    reply = result[0]["generated_text"][-1]["content"]

    messages.append({"role": "assistant", "content": reply})

    print(f"\nModeli: {reply}\n")
