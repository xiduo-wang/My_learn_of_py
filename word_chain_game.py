import random

# List of English words for the game to choose from
# 游戏中电脑可选择的英文单词列表 (列表数据结构，存储多个字符串)
words = ["apple", "elephant", "tiger", "rabbit", "snake", "eagle", "dog", "cat", 
         "mouse", "zebra", "lion", "giraffe", "monkey", "bird", "frog", "fish",
         "turtle", "panda", "koala", "whale", "shark", "penguin", "duck", "wolf"]

# Display welcome message
# 显示欢迎信息 (print函数用于在控制台输出文本)
print("Welcome to the Word Chain Game!")
print("I will start with a random word.")
print("You must enter a word that starts with the last letter of my word.")
print("Let's begin!")
print("-" * 40)

# Generate a random word to start the game
# 生成一个随机单词开始游戏 (random.choice函数从列表中随机选择一个元素)
computer_word = random.choice(words)

# Game loop
# 游戏循环 (while True创建一个无限循环，直到满足退出条件)
while True:
    # Display the computer's word
    # 显示电脑的单词 (print函数输出信息)
    print(f"My word: {computer_word}")
    
    # Get the last letter of the computer's word
    # 获取电脑单词的最后一个字母 (字符串索引，-1表示最后一个字符)
    last_letter = computer_word[-1]
    
    # Prompt user for input
    # 提示用户输入 (input函数获取用户输入)
    user_word = input(f"Enter a word that starts with '{last_letter}': ")
    
    # Check if user wants to quit
    # 检查用户是否想退出游戏 (条件判断，字符串比较)
    if user_word.lower() == "quit":
        # Exit the game
        # 退出游戏 (break语句中断循环)
        print("Thanks for playing!")
        break
    
    # Check if the user's word starts with the correct letter
    # 检查用户的单词是否以正确的字母开头 (条件判断和字符串方法)
    if not user_word or user_word[0].lower() != last_letter.lower():
        # Invalid input message
        # 无效输入提示信息 (条件不满足时执行的代码块)
        print(f"Your word must start with the letter '{last_letter}'! Try again.")
        continue
    
    # User input is valid, now computer selects a new word
    # 用户输入有效，现在电脑选择新单词 (获取用户单词的最后一个字母)
    user_last_letter = user_word[-1]
    
    # Filter words that start with the user's word's last letter
    # 筛选以用户单词最后一个字母开头的单词 (列表推导式，条件筛选)
    possible_words = [word for word in words if word[0].lower() == user_last_letter.lower()]
    
    # Check if there are any matching words
    # 检查是否有匹配的单词 (条件判断，列表长度检查)
    if possible_words:
        # Choose a random word from possible words
        # 从可能的单词中随机选择一个 (random.choice函数随机选择)
        computer_word = random.choice(possible_words)
    else:
        # Computer has no matching words
        # 电脑没有匹配的单词 (条件不满足时执行的代码)
        print(f"I don't have any words starting with '{user_last_letter}'.")
        print("You win! Game over.")
        break 