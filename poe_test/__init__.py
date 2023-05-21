from pygpt4all import GPT4All_J

model = GPT4All_J('/Users/zack/Library/Application Support/nomic.ai/GPT4All/ggml-gpt4all-j-v1.3-groovy.bin')
for token in model.generate("How to use Spring boot quickly ?\n"):
    print(token, end='', flush=True)




