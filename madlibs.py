"""
 story.text:
 One [adjective] day, my best friend and I decided to go to the [place]. 
We packed our [plural noun] and a bottle of [liquid] for the trip. When we got there, we saw a [adjective] [animal] trying to [verb] a [noun].
It was the most [adjective] thing we had ever seen! Then, a [famous person] appeared out of nowhere and shouted, "[funny phrase]!" We all [past tense verb] and lived [adverb] ever after.


"""
with open("story.txt","r") as f:
     story=f.read()
words=set()
start_of_word=-1
target_start="["
target_end="]"


for i,char in enumerate(story):
    if char==target_start:
        start_of_word=i

    elif char==target_end and start_of_word!=-1:
        word=story[start_of_word:i+1]
        words.add(word)
        start_of_word=-1
answers={}
for word in words:
    answer=input("enter a word for "+ word+ ":")
    answers[word]=answer
for word in words:
    story=story.replace(word,answers[word])

print(story)

 
