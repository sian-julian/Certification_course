def emoji_replace(text):

    for emotion in emoji:
        text=text.replace(emotion,emoji[emotion])
        
    print("after replacing:",text)


emoji={"sad":"😢","happy":"😃","love":"😍","cool":"😎"}
text=input("Enter a message:")
emoji_replace(text)