import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab size", encoder.n_vocab)

# Tokenization : Convert user input into numbers

text = "The cat sat on the mat"
tokens = encoder.encode(text)

print("Generate Tokens", tokens)

my_tokens = [976, 9059, 10139, 402, 290, 2450]
decode = encoder.decode(my_tokens)

print("Decode Tokens", decode)