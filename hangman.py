import re
#CSVファイルに保存された単語をランダムに出力する関数定義

#ハングマンのアルゴリズムを記述した関数start_hangman()を定義
def start_hangman(word):
    #関数の引数に代入された文字列を一文字ずつ小文字に変換してリストに格納する
    word_list = list(word.lower())
    #文字列の文字数分アンダーバー(_)をリストに格納する
    secret_word_list = ["_"] * len(word)
    picture_of_hangman = ["",
                          "_________     ",
                          "|        |    ",
                          "|        O    ",
                          "|       /|\   ",
                          "|       / \   ",
                          "|             ",
                          "--------------"
                          ]
    num_of_wrong = 0 #失敗した回数を記録する変数
    print("ミニゲーム「ハングマン」を始めます")
    while "_" in secret_word_list or num_of_wrong < len(picture_of_hangman): #ゲームの手順を進めるループ
        print(" ".join(secret_word_list))
        char = input("アルファベット一文字予想してね！(半角英字で記入してください)：")
        #正規表現を利用して予想した一文字がアルファベットであるかどうかを確認している
        if not bool(re.match("[a-zA-Z]",char)) or len(char) != 1:
            print("不適切な入力です。")
            continue
        
        #大文字・小文字どちらから一文字入力しても変わらず処理するために、
        #入力した文字と正解の文字列を一文字ずつ格納したリストの要素をすべて小文字にして処理を行っている
        if char.lower() in word_list:
            print("正解です！")
            num_of_index = word_list.index(char.lower())
            secret_word_list[num_of_index] = word[num_of_index]
            word_list[num_of_index] = "$"
            if "_" not in secret_word_list:
                print("おめでとうございます\nあなたの勝ちです!")
                print(" ".join(secret_word_list))
                break
        else:
            print("不正解です")
            num_of_wrong += 1
            for i in range(num_of_wrong):
                print(picture_of_hangman[i])
            if num_of_wrong == len(picture_of_hangman):
                print("あなたの負けです!")
                print("正解は「{}」です".format(word))
                break
    print("ゲームを終了します!")
            
            
word = "Hello"
start_hangman(word)