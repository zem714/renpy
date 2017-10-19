#이미지 추가하는 법.

이미지들은 game폴더의 images 폴더 안에 넣을 것.
새로운 폴더를 만들떄도 images 폴더 안에 만들 것.

##배경
image bg_name = "bg/bg_name.jpg"
배경은 jpg로 저장하고, bg폴더를 만들어서 그 곳 안에 둘 것.
그냥 그렇게하면 찾거나 저장할때 편하니까.
이렇게 선언해 놓은 것을 불러올 때에는
scene bg_name
으로 하면 될 것.

##캐릭터
image a normal = "ch/a/a__normal.png"
캐릭터 이미지는 반드시 png로!
배경을 투명화 하는 것을 잊지 말것.
이렇게 선언해 놓은 것을 불러올 때에는 
show a normal
을 사용하면됨.

캐릭터의 표정변화를 표현할때에는 절대로
show a_normal
을 쓰지 말것.

예를 들어 여러가지 표정,
image a normal = "~~~"
image a frown = "~~~"
image a cry = "~~~"
이렇게 선언해놓고,
show a_normal
show a_frown
show a_cry
하면 모두 겹친 상태로 존재하게 됨.
show a normal
show a frown
show a cry
하면 normal -> frown -> cry 로 사진에 변하게 됨.

##다른 알아두어야 할 것들

###트랜지션
트랜지션은 표현에 매우 중요!

배경을 위한 트랜지션과 캐릭터를 위한 트랜지션이 있다.

####배경

Fade(0.5,0.5,0.5)
-> 0.5초 동안 검은 화면이 되고, 0.5초 동안 검은화면 상태이고, 0.5초 동안 선언한 화면이 등장한다.

Dissolve(0.5) = dissolve
0.5초 동안 선언한 화면이 등장한다.
제목처럼 dissolve 는 0.5초 동안 일어나는 Dissolve 이다.

irisin / irisout
밖에서 안으로 화면이 바뀐다. / 중간에서 밖으로 화면이 바뀐다.

slideleft / slideright / slideup / slidedown
방향으로 화면이 들어온다.



####캐릭터
dissolve
거의 대부분 이거 쓴다.
배경의 dissolve 와 동일함.

move
지정한 위치로 캐릭터가 이동한다.

moveinright / moveintop / moveinleft / moveinbottom 
뱡향에서 캐릭터가 들어온다.

moveoutright / ~ / ~ / ~
방향으로 캐릭터가 나간다.



###캐릭터들의 포지션
대충 포지션을 3개 만들때를 정하면
define center = Position(xalign = 0.5)
define left = Position(xalign = 0.2)
define right = Position(xalign = 0.8)
를 추가해놓자.

xalign 은 사진의 중간 중점으로 해서 나오는 것이 아니다.
xalign = 0.0 을 하면 사진의 왼쪽 벽을
xalign = 1.0 을 하면 사진의 오른쪽 벽을
기준으로 하여 사진이 나온다. 
이해가 안가면 직접 해보도록 하자.
