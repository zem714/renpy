#모든 경로는 game폴더에 만들 것!!


##반복되는 음악을 넣을 때
play music "경로/music.mp3"
보통은
play music "mp3/~/music.mp3"
로 한다.
끝에
fadein 숫자
를 넣도록 하자.
소리가 원래 크기의 소리가 될때까지 '숫자' 초가 걸린다.


##한번만 나오는 소리
play sound "경로/sound.mp3"
보통은
play sound "sound/~/sound.mp3"
로 경로를 만든다.

##어디서부터 어디까지
play sound "<from ? to ?>sound.mp3"

##소리, 노래 멈추기
stop music
stop sound 
끝에
fadeout 숫자
를 추가하면 점점 소리가 '숫자' 초 만큼 작아지면서 꺼짐.

#목소리, 음성을 넣고 싶을때.
talker "something"
voice "voice.mp3"
이렇게 넣으면 된다.