import senticnet

emo_extractor = Emo_extractor()

for w in disambiguate_dialog_df["Word"]:
    #wm=w.lower()

    if w in senticnet.senticnet.keys():
        emo_extractor.extract_emotion()
    elif w in senticnet.senticnet.values():
        emo_extractor.extract_emotion()
    elif w not in senticnet.senticnet.keys() and senticnet.senticnet.values() :
        check_w = wn.synsets(w)
        if check_w:
            word = wn.synsets(w)[0]
            check_hypernym = word.hypernyms()
            if check_hypernym :
                hypernym_word = word.hypernyms()[0]
                regex = re.compile("(?<=Synset\(')[^_.]+")
                regex_word = str(regex.findall(str(hypernym_word)))
                ok_word_1 = regex_word.replace("['", "")
                ok_word_2 = ok_word_1.replace("']", "")
                if ok_word_2 in senticnet.senticnet.keys() or senticnet.senticnet.values() :
                    emotion_1 = senticnet.senticnet[ok_word_2][4]
                    emotion_2 = senticnet.senticnet[ok_word_2][5]
                    list_1st_emotion.append(emotion_1)
                    list_2nd_emotion.append(emotion_2)
            else :
                list_1st_emotion.append("not found")
                list_2nd_emotion.append("not found")
        else:
            list_1st_emotion.append("not found")
            list_2nd_emotion.append("not found")

disambiguate_dialog_df["1st Emotion"] = list_1st_emotion
disambiguate_dialog_df["2nd Emotion"] = list_2nd_emotion

print(disambiguate_dialog_df)